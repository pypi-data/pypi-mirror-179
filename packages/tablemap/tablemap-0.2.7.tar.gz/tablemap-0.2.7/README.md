# About

Tablemap is a handy little Python data wrangling tool for whom Pandas or SQL feel clunky when problems
touch just one small step further than their routine, ordinary circle.

While a table is nothing but a list of dictionaries, often times Pandas looks like a long way around. 
It can wait till it's really required.

Some people might be happy if only they can easily chain up some processes they do on tables 
without worrying too much about the memory. Less on stackoverflow.com for arcane pandas spells. This is for those. 

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

The right hand side of the assignment can be a list of dictionaries, an iterator that yields dictionaries or an object fetched from the connection, for example, `conn['t1']` on which you can chain up some methods such as `map`, `by`, `concat`, and so on.

Each dictionary represents a row in a table. For instance `{'col1': a, 'col2': 4}` is a row with two columns, `col1` and `col2`.


To browse database tables,

```python
print(conn['t1'].list())

# or if you want to save some memory,
for r in conn['t1'].iter():
    print(r)
```


If you prefer GUI, you can open up the file `sample.db` with softwares like [SQLiteStudio](https://sqlitestudio.pl/) or [DB Browser for SQLite](https://sqlitebrowser.org/). 

Once you clean up the table, you may begin the analysis with pandas.

```python
import pandas as pd

df = pd.DataFrame(conn['t1'].iter())
conn['t1_copy'] = df.to_dict('records')
```

## Methods for table manipulation
+ ### `map`

We'd like to filter rows with `col2 > 2` and add 1 to `col2` for some reason.

```python
def add1(r):
    if r['col2'] > 2:
        r['col2'] += 1
        return r

conn['t1_1'] = conn['t1'].map(add1)
```

The argument for map is a dictionary-yielding generator or an ordinary function that
returns a dictionary, a list of dictionaries, or None. It takes a single dictionary as an argument 
or a list of dictionaries (multiple rows) when the previous process is `by`.

+ ### `by`

To sort and group `t1` by `col1` before summing up `col2`,

```python
def sumup(rs):
    r0 = rs[0]
    r0['col2_sum'] = sum(r['col2'] for r in rs)
    del r0['col2']
    return r0

conn['t1_col2sum_groupby_col1'] = conn['t1'].by('col1')\
    .map(sumup)
```

`by` takes columns as arguments (multiple args for multiple columns) for grouping and the next process (map in this case) takes on each group (a list of dictionaries).

+ ### `order` and `group`

Actually `by` is a combination of `order` and `group`, you may fine control by separating these processes, 

```python
conn['t1_col2sum_groupby_col1'] = conn['t1']\
    .order('col1', 'col2 desc').group('col1')\
    .map(sumup)
```

Now `map` takes a list of dictionaries where col2 is sorted in a descending order.


+ ### `concat`

To concatenate `t1` with itself,  

```python
conn['t1_double'] = conn['t1'].concat(conn['t1'])
```

which is the same as

```python
conn['t1_double'] = conn['t1'].concat(table1)

```


Tables for concatenation must have the same columns.

+ ### `filter` and `update`

```python
conn['t1_1'] = conn['t1']\
    .filter(lambda r: r['col2'] > 2)\
    .update(
        col2=lambda r: r['col2'] + 1,
        col3=lambda r: r['col1'] + str(r['col2'])
    )
```

Columns are updated sequentially, so `col3` has `a5` and `a6` not `a4` and `a5`.

`filter` works for groups as well.

```python
conn['t1_2'] = conn['t1'].by('col1').filter(lambda rs: len(rs) > 1)
```

+ ### `select` and `deselect` 
You can pass columns to `select` or `deselect` to pick up or to delete specific columns in a table

```python
conn['t1_1'] = conn['t1'].update(col3=lambda r: r['col2'] + 1)\
    .deselect('col1', 'col3')
```

+ ### `distinct`
To group the table `t1` by `col1` and to leave only the first row in each group, (removing duplicates) 

```python
conn['t1_1'] = conn['t1'].distinct('col1')
```
Again, you can pass multiple columns to `distinct`

+ ### `fold`

To sum up `col2` grouped by `col1`,

```python
conn['t1_col2sum_groupby_col1'] = conn['t1'].by('col1')\
    .fold(col2_sum=lambda rs: sum(r['col2'] for r in rs))
    .deselect('col2')
```
`fold` is `update` for groups. However `fold` can't update columns sequentially by nature because it works on groups and creates a single row, so it updates concurrently. In other words, the previous updates do not affect the following ones when there are multiple updates in one `fold` method.

+ ### `inner_join`, `left_join`, `right_join`, and `full_join`

To merge tables,

```python
conn['t1_col3'] = conn['t1'].by('col1')\
    .full_join(conn['t2'].by('col1'))
```

All of the four join methods share the same interface, they must be grouped before they are joined together.

If both of the tables have the same columns, the columns of the table on the left-hand side will remain except for `right_join` in which the right-hand side columns stay.

To do the cross join, consider passing a (lexical) closure on map to avoid repetitive table fetching.

```python
def fn():
    table2 = conn['t2'].list()
    def innerfn(rs):
        ...do some work using table2
        yield something
    return innerfn

conn['some_table'] = conn['t1'].by('col1').map(fn())
```


<!-- [Documentation]
(https://tablemap.readthedocs.io/en/latest/index.html)
 -->