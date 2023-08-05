"""A data wrangling tool which requires no knowledge of Pandas or SQL.
"""

import os
import signal
import sqlite3
import tempfile
from contextlib import contextmanager
from inspect import isgeneratorfunction
from itertools import chain, groupby, product
from pathlib import Path, PurePath


class Conn:
    """Connection to a SQL database file.

    Example:
        conn = Conn('sample.db')
    """

    def __init__(self, dbfile):
        # dbfile must be a filename(str), can't be :memory:
        if PurePath(dbfile).is_absolute():
            self._dbfile = dbfile
        else:
            self._dbfile = os.path.join(os.getcwd(), dbfile)

        self._dbconn = None

    def __getitem__(self, tname):
        return _InstructionContainer(self, tname)

    def __setitem__(self, tname, val):
        with _connect(self._dbfile) as c:
            self._dbconn = c
            _delete(c, tname)
            _insert(c, tname, _inst2iter(val))


class _InstructionContainer:
    """Holds instructions to transform a table by chaining methods.

    This is a private class. Instead of directly creating an instance of
    this class, use Conn.__getitem__
    """

    def __init__(self, conn, tname):
        self._conn = conn
        self._insts = [{
            'cmd': 'fetch',
            'tname': tname,
        }]
        self._genfns = [_build_initgen(conn, tname, [])]

    # each column may contain asc or desc
    # ex) 'col1 desc', 'col2 asc'
    def order(self, *cols):
        if len(self._insts) == 1 and self._insts[-1]['cmd'] == 'fetch':
            tname = self._insts[-1]['tname']
            # replace the previous generator
            self._genfns[0] = _build_initgen(self._conn, tname, cols)
            self._insts.append({
                'cmd': 'order',
                'cols': cols
            })
            return self

        pgen = self._genfns[-1]

        def gen():
            try:
                tmpdbfd, tmpdb = tempfile.mkstemp()
                with _connect(tmpdb) as c:
                    _insert(c, 'temp', pgen())
                    yield from _fetch(c, 'temp', cols)
            finally:
                # must close the file descriptor to delete it
                os.close(tmpdbfd)
                if Path(tmpdb).is_file():
                    os.remove(tmpdb)

        self._genfns.append(gen)
        self._insts.append({
            'cmd': 'order',
            'cols': cols
        })
        return self

    def _map_group(self, fn):
        pgen = self._genfns[-1]
        fn = _fn2gen(fn)

        def gen():
            for _, rs in pgen():
                yield from fn(rs)

        self._genfns.append(gen)
        self._insts.append({
            'cmd': '_map_group',
            'fn': fn
        })
        return self

    def _map_single(self, fn):
        pgen = self._genfns[-1]
        fn = _fn2gen(fn)

        def gen():
            for r in pgen():
                yield from fn(r)

        self._genfns.append(gen)
        self._insts.append({
            'cmd': '_map_single',
            'fn': fn
        })
        return self

    # itertools.groupby generates iterator groups, so to turn each into a list
    def _group2list(self):
        pgen = self._genfns[-1]

        def gen():
            for k, rs in pgen():
                yield k, list(rs)

        self._genfns.append(gen)
        self._insts.append({
            'cmd': '_group2list'
        })
        return self

    def group(self, *cols):
        pgen = self._genfns[-1]

        def gen():
            yield from groupby(pgen(), _keyfn(cols))

        self._genfns.append(gen)
        self._insts.append({
            'cmd': 'group',
            'cols': cols
        })
        return self

    def _merge(self, fn, other):
        pgen = self._genfns[-1]

        def gen():
            yield from _step(fn, pgen(), _inst2iter(other))

        self._genfns.append(gen)
        self._insts.append({
            'cmd': '_merge',
            'fn': fn,
            'other': other
        })
        return self

    def concat(self, other):
        pgen = self._genfns[-1]

        def gen():
            for r in pgen():
                yield r
            for r in _inst2iter(other):
                yield r

        self._genfns.append(gen)
        self._insts.append({
            'cmd': 'concat',
            'other': other
        })
        return self

    def map(self, fn):
        if self._insts[-1]['cmd'] == 'group':
            return self._group2list()._map_group(fn)
        return self._map_single(fn)

    def by(self, *cols):
        # need to cut out 'desc', 'asc'
        cols_for_group = [col.split()[0] for col in cols]
        return self.order(*cols).group(*cols_for_group)

    def filter(self, pred):
        def gen1(r):
            if pred(r):
                yield r

        def gen2(rs):
            if pred(rs):
                yield from rs

        return self.map(gen2 if self._insts[-1]['cmd'] == 'group' else gen1)

    def update(self, **kwargs):
        def updatefn(r):
            for k, v in kwargs.items():
                r.update({k: v(r)})
            yield r

        return self.map(updatefn)

    def fold(self, **kwargs):
        def foldfn(rs):
            r0 = rs[0].copy()
            for k, v in kwargs.items():
                r0.update({k: v(rs)})
            yield r0

        return self.map(foldfn)

    def select(self, *cols):
        def selectfn(r):
            yield {col: r[col] for col in cols}

        return self.map(selectfn)

    def deselect(self, *cols):
        cols = set(cols)

        def deselectfn(r):
            yield {k: v for k, v in r.items() if k not in cols}

        return self.map(deselectfn)

    def inner_join(self, other):
        def innerjoin_fn(rs1, rs2, _left, _center, _right):
            if rs1 != [] and rs2 != []:
                for r1, r2 in product(rs1, rs2):
                    r1.update(r2)
                    yield r1

        return self._merge(innerjoin_fn, other)

    def left_join(self, other):
        def leftjoin_fn(rs1, rs2, _left, _center, right):
            if rs1 != [] and rs2 != []:
                for r1, r2 in product(rs1, rs2):
                    r1.update(r2)
                    yield r1

            elif rs1 != [] and rs2 == []:
                for r1 in rs1:
                    for col in right:
                        r1[col] = None
                    yield r1

        return self._merge(leftjoin_fn, other)

    def right_join(self, other):
        def rightjoin_fn(rs1, rs2, left, _center, _right):
            if rs1 != [] and rs2 != []:
                for r1, r2 in product(rs1, rs2):
                    r2.update(r1)
                    yield r2

            elif rs1 == [] and rs2 != []:
                for r2 in rs2:
                    for col in left:
                        r2[col] = None
                    yield r2

        return self._merge(rightjoin_fn, other)

    def full_join(self, other):
        def fulljoin_fn(rs1, rs2, left, _center, right):
            if rs1 != [] and rs2 != []:
                for r1, r2 in product(rs1, rs2):
                    r1.update(r2)
                    yield r1

            elif rs1 != [] and rs2 == []:
                for r1 in rs1:
                    for col in right:
                        r1[col] = None
                    yield r1

            elif rs1 == [] and rs2 != []:
                for r2 in rs2:
                    d = {col: None for col in left}
                    d.update(r2)
                    yield d

        return self._merge(fulljoin_fn, other)

    def distinct(self, *columns):
        def distinctfn(rs):
            yield next(rs)

        return self.by(*columns)._map_group(distinctfn)

    def iter(self):
        yield from self._genfns[-1]()

    def list(self):
        return list(self.iter())


def _insert_statement(name, d):
    """insert into foo values (:a, :b, :c, ...)

    Notice the colons.
    """
    keycols = ', '.join(":" + c.strip() for c in d)
    return "insert into %s values (%s)" % (name, keycols)


def _create_statement(tname, cols):
    """Create table if not exists foo (...)

    Note:
        Every type is numeric.
    """
    schema = ', '.join([col + ' ' + 'numeric' for col in cols])
    return "create table if not exists %s (%s)" % (tname, schema)


def _dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def _keyfn(cols):
    if len(cols) == 1:
        col = cols[0]
        return lambda r: r[col]
    return lambda r: [r[col] for col in cols]


def _delete(c, tname):
    c.cursor().execute(f'drop table if exists {tname}')


def _insert(c, tname, rs):
    rs = iter(rs)
    try:
        r0 = next(rs)
    except StopIteration:
        raise ValueError(f"No row to insert in {tname}") from None
    else:
        cols = list(r0)

        c.cursor().execute(_create_statement(tname, cols))
        istmt = _insert_statement(tname, r0)
        c.cursor().executemany(istmt, chain([r0], rs))


def _fetch(c, tname, cols):
    if cols:
        query = f"select * from {tname} order by {','.join(cols)}"
    else:
        query = f"select * from {tname}"

    yield from c.cursor().execute(query)


# ordinary function to generator function
def _fn2gen(f):
    def gen(r):
        x = f(r)
        if isinstance(x, dict):
            yield x
        elif x is not None:
            yield from x

    return f if isgeneratorfunction(f) else gen


def _spy(it):
    val = next(it)
    return val, chain([val], it)


def _step(fn, krs1, krs2):
    empty = object()
    try:

        k1, rs1 = next(krs1)
        k2, rs2 = next(krs2)

        r1, rs1 = _spy(rs1)
        r2, rs2 = _spy(rs2)

        cols1 = list(r1)
        cols2 = list(r2)

        left = [c for c in cols1 if c not in cols2]
        # common columns
        center = [c for c in cols1 if c in cols2]
        right = [c for c in cols2 if c not in cols1]

        while True:
            if k1 == k2:
                yield from fn(rs1, rs2, left, center, right)
                k1 = k2 = empty
                k1, rs1 = next(krs1)
                k2, rs2 = next(krs2)
            elif k1 < k2:
                yield from fn(rs1, [], left, center, right)
                k1 = empty
                k1, rs1 = next(krs1)
            else:
                yield from fn([], rs2, left, center, right)
                k2 = empty
                k2, rs2 = next(krs2)

    except StopIteration:
        # unconsumed
        if k1 is not empty:
            yield from fn(rs1, [], left, center, right)
        if k2 is not empty:
            yield from fn([], rs2, left, center, right)

        for _, rs1 in krs1:
            yield from fn(rs1, [], left, center, right)
        for _, rs2 in krs2:
            yield from fn([], rs2, left, center, right)


def _inst2iter(obj):
    return obj.iter() if isinstance(obj, _InstructionContainer) else iter(obj)


def _build_initgen(conn, tname, cols):
    def initgen():
        try:
            yield from _fetch(conn._dbconn, tname, cols)
        # in case conn._dbconn is either None or closed connection
        except (AttributeError, sqlite3.ProgrammingError):
            with _connect(conn._dbfile) as c:
                conn._dbconn = c
                yield from _fetch(c, tname, cols)
    return initgen


@contextmanager
def _connect(db):
    conn = sqlite3.connect(db)
    conn.row_factory = _dict_factory
    try:
        yield conn
    finally:
        # If users enter ctrl-c during the database commit,
        # db might be corrupted. (won't work anymore)
        with _delayed_keyboard_interrupts():
            conn.commit()
            conn.close()


@contextmanager
def _delayed_keyboard_interrupts():
    signal_received = []

    def handler(sig, frame):
        nonlocal signal_received
        signal_received = (sig, frame)
    # Do nothing but recording something has happened.
    old_handler = signal.signal(signal.SIGINT, handler)

    try:
        yield
    finally:
        # signal handler back to the original one.
        signal.signal(signal.SIGINT, old_handler)
        if signal_received:
            # do the delayed work
            old_handler(*signal_received)
