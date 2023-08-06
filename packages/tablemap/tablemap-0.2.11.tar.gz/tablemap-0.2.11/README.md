# About

Tablemap is a handy little Python data wrangling tool for whom Pandas or SQL feel clunky when problems
touch just one small step further than their routine, ordinary circle.

While a table is nothing but a list of dictionaries, oftentimes Pandas looks like a long way around. 
It can wait till it's required.

Some people might be happy if only they can easily chain up some processes they do on tables 
without worrying too much about memory. Less on stackoverflow.com for arcane pandas spells. This is for those. 

# Installation

Requires only built-in Python libraries.

```
pip install tablemap
```


# Tutorial

## Saving tables in the database

Let's create a table `t1` in `sample.db`. 

```python
from tablemap import Conn

t1 = [
    {'col1': 'a', 'col2': 4},
    {'col1': 'a', 'col2': 5},
    {'col1': 'b', 'col2': 1},
]

conn = Conn('sample.db')
conn['t1'] = t1
```

The right-hand side of the assignment can be a list of dictionaries, an iterator that yields dictionaries, or an object fetched from the connection, for example, `conn['t1']` on which you can chain up some methods such as `map`, `by`, `concat`, and so on.

Each dictionary represents a row in a table. For instance `{'col1': 'a', 'col2': 4}` is a row with two columns, `col1` and `col2`.


To browse database tables,

```python
print(conn['t1'].list())

# or if you want to save some memory,
for r in conn['t1'].iter():
    print(r)
```


If you prefer GUI, you can open up the file `sample.db` with software like [SQLiteStudio](https://sqlitestudio.pl/) or [DB Browser for SQLite](https://sqlitebrowser.org/). 

Once you clean up the table, you may begin the analysis with pandas.

```python
import pandas as pd

df = pd.DataFrame(conn['t1'].iter())
conn['t1_copy'] = df.to_dict('records')
```

## Methods for table manipulation

+ ### `concat`

To concatenate `t1` with itself,  

```python
conn['t1_double'] = conn['t1'].concat(conn['t1'])
```

A list of dictionaries or an iterator that yields dictionaries can be passed as an argument as well.

```python
conn['t1_double'] = conn['t1'].concat(t1)

```

Tables for concatenation must have the same columns. Order of the columns is not important.


+ ### `filter` and `update`
Each row is simply a dictionary with column names as keys, so you can access a column value by passing a column name to the row(dictionary). To create new columns or update the existing ones,

```python
conn['t1_1'] = conn['t1']\
    .filter(lambda r: r['col2'] > 2)\
    .update(
        col2=lambda r: r['col2'] + 1,
        col3=lambda r: r['col1'] + str(r['col2'])
    )
```

Columns are updated sequentially, so `col3` has `a5` and `a6`, not `a4` and `a5`.


+ ### `by` and `fold`

To sum up `col2` grouped by `col1`,

```python
conn['t1_col2sum_groupby_col1'] = conn['t1'].by('col1')\
    .fold(col2_sum=lambda rs: sum(r['col2'] for r in rs))\
```

`by` takes columns as arguments (multiple args for multiple columns) for grouping and the next process (`fold` in this case) takes on each group (a list of dictionaries).

While `update` works on a dictionary, `fold` does on a list of dictionaries.

Since `fold` turns a list of dictionaries into a single dictionary, it must be preceded by grouping methods such as `by` or `windowed` which shows up soon.

If the function in `fold` returns an iterable (list, tuple, and so on. Not str, str is considered a single value), multiple columns suffixed with numbers (starting from 0) are automatically created.

```python
def minmax(col):
    def fn(rs):
        xs = [r[col] for r in rs]
        return [min(xs), max(xs)]
    return fn

conn['t1_1'] = conn['t1'].by('col1').fold(
    sum=lambda rs: sum(r['col2'] for r in rs),
    mm=minmax('col2')
)
```

Now the columns of the table `t1_1` are `col1` (grouping columns are automatically created), `sum`, `mm0`, and `mm1` because `minmax('col2')` returns a list of size 2.

+ ### `rename`

To replace old column names with new ones,

```python
conn['t1_1'].rename(
    min='mm0',
    max='mm1'
)
```

+ ### `inner_join`, `left_join`, `right_join`, and `full_join`

To merge tables,

```python
conn['t2'] = [
    {'col1': 'b', 'col3': -1},
    {'col1': 'c', 'col3': 3},
    {'col1': 'b', 'col3': ''},
]

conn['t1_col3'] = conn['t1'].by('col1')\
    .full_join(conn['t2'].by('col1'))
```

All of the four join methods share the same interface, they must be grouped before they are joined together.

For the columns that are in both tables, the left-hand side columns remain except for `right_join` where the right-hand side columns do.

Empty columns are represented as empty string.

+ ### `distinct`
To group the table `t1` by `col1` and to leave only the first row in each group, (removing duplicates) 

```python
conn['t1_1'] = conn['t1'].distinct('col1')
```
You can pass multiple columns to `distinct` as in `by`

+ ### `select` and `deselect` 
You can pass columns to `select` or `deselect` to pick up or delete specific columns in a table

```python
conn['t1_1'] = conn['t1'].update(col3=lambda r: r['col2'] + 1)\
    .deselect('col1', 'col2')
```


+ ### `islice`

To take the first 2 rows from table `t1`,

```python
for r in conn['t1'].islice(2).iter():
    print(r)
```
`islice` takes the same parameters as in [`itertools.islice`](https://docs.python.org/3/library/itertools.html#itertools.islice).

Grouping methods like `by` cannot come right before `islice` (Technically easy but it will only add confusion)

+ ### `takewhile` and `dropwhile`

You can pass predicates to `takewhile` or `dropwhile` to do what these names suggest.

Again, grouping methods cannot come before these methods.



+ ### `map`

When `update` or `fold` is not strong enough, you can deal with a row or rows directly.

```python
def sumup(rs):
    r0 = rs[0]
    r0['col2_sum'] = sum(r['col2'] for r in rs)
    del r0['col2']
    return r0

conn['t1_col2sum_groupby_col1'] = conn['t1'].by('col1')\
    .map(sumup)
```

The argument for `map` is a dictionary-yielding generator or an ordinary function that returns a dictionary, a list of dictionaries, or None. It takes a single dictionary as an argument or a list of dictionaries (multiple rows) when the previous process is `by` or `windowed`.


+ ### `windowed`
When you need to group a chunk of consecutive rows,

```python
conn['t1_1'] = conn['t1'].windowed(4, 2).fold(
    sum=lambda rs: sum(r['col2'] for r in rs),
    mm=minmax('col2')
)
```

`fold` takes the first 4 consecutive rows and the next 4 starting from the 3rd (skipping 2 rows) and so on. When rows less than or equal to 4 are left, it will be the last. This time, the columns of the table `t1_1` are `sum`, `mm0`, and `mm1`.

+ ### `order` and `group`

Actually, `by` is a combination of `order` and `group`, you can control more precise by separating these processes, 

```python
conn['t1_col2sum_groupby_col1'] = conn['t1']\
    .order('col1', 'col2 desc').group('col1')\
    .map(sumup)
```

Now, `map` takes a list of dictionaries where col2 is sorted in descending order.


## Some remarks 

- `by` (or `group`. Again, `by` is a combination of `order` and `group`) and `windowed` are the only grouping methods. 
    1. The 4 joining methods must be preceded by `by` (must be ordered before grouping, so `group` without `order` is not allowed). 
    2. `fold` must be preceded by `group`(`by`) or `windowed`. 
    3. `map` may or may not be preceded by `group`(`by`) or `windowed`. (`map` is allowed to take a single row as well.)
    4. No other cases are allowed for grouping to build tables in the database. Therefore `by` cannot be preceded by `windowed` although it makes sense semantically. 

- `windowed` overlap rows. Those overlapped rows are copied before you apply functions in `fold` or `map`. So don't worry about the row modifications. 

- To do the cross-join, consider passing a (lexical) closure on the method `map` to avoid repetitive table fetching.

```python
def fn():
    table2 = conn['t2'].list()
    def innerfn(rs):
        ...do some work using table2
        yield something
    return innerfn

conn['some_table'] = conn['t1'].by('col1').map(fn())
```
- If you want to add an index column for each group,

```python
def cnt():
    n = 0 
    def innerfn(rs):
        nonlocal n
        n += 1
        for r in rs:
            r['n'] = n
            yield r 
    return innerfn 

conn['t1_1'] = conn['t1'].by('col1').map(cnt())

```
Might not be useful in any way though.

<!-- [Documentation]
(https://tablemap.readthedocs.io/en/latest/index.html)
 -->
