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

The right-hand side of the assignment can be a list of dictionaries, an iterator that yields dictionaries, or an object fetched from the connection, for example, `conn['t1']` on which you can chain up some methods such as `map`, `update`, `by`, `chain`, and so on.

Each dictionary represents a row in a table. For instance `{'col1': 'a', 'col2': 4}` is a row with two columns, `col1` and `col2`.


To browse tables in the database,

```python
rs = conn['t1']
print(rs)

# which is equivalent to  
print(rs.list())

# or if you want to see only part of it 
rs1 = rs.islice(3, 5)
print(rs1)

# rs, unchanged. Check the sizes of them. 
print(rs.size(), rs1.size())
```

If you prefer GUI, you can open up the file `sample.db` with software like [SQLiteStudio](https://sqlitestudio.pl/) or [DB Browser for SQLite](https://sqlitebrowser.org/). 

Once you clean up the table, you may wish to begin the analysis with pandas.

```python
import pandas as pd

df = pd.DataFrame(conn['t1'].list())
conn['t1_copy'] = df.to_dict('records')
```

## Rows objects
`conn['t1']` is a `Rows` object. Rows objects can be created in two ways

1. Pass a table name to Conn object, `Conn['t1']` 
2. Directly pass a list of dictionaries or a dictionary yielding iterator, `Rows(t1)`

Passing a column name to a Rows object returns a list of elements for the column, `Rows(t1)['col1'] == ['a', 'a', 'b']`

A Rows object represents a list of dictionaries and they have a few methods to chain up to transform a table.

*** 

## Methods for table manipulation

+ ### `chain`

To concatenate `t1` with itself,  

```python
conn['t1_double'] = conn['t1'].chain(conn['t1'])
```

A list of dictionaries or an iterator that yields dictionaries can be passed as an argument as well.

```python
conn['t1_double'] = conn['t1'].chain(t1)

```

Tables for concatenation must have the same columns. The order of the columns is not important.


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

A lambda expression is a nameless function. In the expression `lambda r: r['col2'] > 2`, the parameter `r` represents a single dictionary and the whole expression returns an evaluated value of `r['col'] > 2` for each iteration.

Columns are updated sequentially, so `col3` has `a5` and `a6`, not `a4` and `a5`.


+ ### `by` and `fold`

To sum up `col2` grouped by `col1`,

```python
conn['t1_col2sum_groupby_col1'] = conn['t1'].by('col1')\
    .fold(
        col2_sum=lambda rs: sum(rs['col2']),
        col2_min=lambda rs: min(rs['col2']),
        col2_max=lambda rs: max(rs['col2']),
    )
```

`by` takes columns as arguments (multiple args for multiple columns) for grouping and the next process (`fold` in this case) takes on each group (a Rows object) 

While `update` works on a dictionary, `fold` does on a Rows object. (`fold` folds n rows to one row.)

`fold` must be preceded by grouping methods such as `by` or `windowed` which shows up soon.

+ ### `rename`

To replace old column names with new ones,

```python
conn['t1_1'].rename(
    c2min='col2_min',
    c2max='col2_max'
)
```

+ ### `join`

To merge tables,

```python
conn['t2'] = [
    {'col1': 'b', 'col3': -1},
    {'col1': 'c', 'col3': 3},
    {'col1': 'b', 'col3': ''},
]

conn['t1_col3'] = conn['t1'].by('col1')\
    .join(conn['t2'].by('col1'), 'full')
```

There are 4 join types, 'inner', 'left', 'right', and 'full'. The default is 'left' 

Tables must be grouped to be joined.

If the table `t1` and `t2` have columns with the same name, `t1` columns will be updated with `t2` columns. 

Empty strings represent missing values.

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
print(conn['t1'].islice(2))
```

`islice` takes the same parameters as in [`itertools.islice`](https://docs.python.org/3/library/itertools.html#itertools.islice).

Grouping methods like `by` cannot come right before `islice` (Technically easy but it will only add confusion)

+ ### `takewhile` and `dropwhile`

You can pass predicates to `takewhile` or `dropwhile` to do what these names suggest.

Again, grouping methods cannot come before these methods.


+ ### `map`

When `update` or `fold` is not strong enough, you can deal with a row or Rows directly.

```python
def sumup(rs):
    tot = sum(rs['col2'])
    # you don't always have to pass a function to `update`, same for `fold`
    return rs.islice(1).update(col2_sum=tot)

conn['t1_col2sum_groupby_col1'] = conn['t1'].by('col1')\
    .map(sumup)\
    .deselect('col2')
```

The argument for `map` is a function that returns a Rows object or a single dictionary, or None. It takes a single dictionary as an argument or a Rows object when the previous process is `by`(`group`) or `windowed`.



+ ### `zip` and `zip_longest`
Like `chain`, zip takes a list of dictionaries or an iterator that yields dictionaries or a Row object as an argument. The argument updates the Rows object row by row until either one of the sequences is depleted. 

With `zip`, the above `sumup` can be rewritten as

```python
def sumup(rs):
    rs2 = [{'col2_sum': sum(rs['col2'])}]
    return rs.zip(rs2)
```

You may append an index column.

```python
conn['t1_1'] = conn['t1'].zip({'idx': i} for i in range(100))
```

+ ### `windowed`
When you need to group a chunk of consecutive rows,

```python
conn['t1_1'] = conn['t1'].windowed(4, 2).fold(
    sum=lambda rs: sum(rs['col2'])
)
```

`fold` takes the first 4 consecutive rows and the next 4 starting from the 3rd (skipping 2 rows) and so on. When rows less than or equal to 4 are left, it will be the last. 

+ ### `order` and `group`

Actually, `by` is a combination of `order` and `group`, you can control more precise by separating these processes, 

```python
conn['t1_col2sum_groupby_col1'] = conn['t1']\
    .order('col1', 'col2 desc').group('col1')\
    .map(sumup)
```

Now, `map` takes a list of dictionaries where col2 is sorted in descending order.

The keyword `desc` can be either upper-cased, lower-cased or mixed. 

The ascending order is the default.


## Some remarks 

- `by` (or `group`. Again, `by` is a combination of `order` and `group`) and `windowed` are the only grouping methods. 
    1. `join` must be preceded by `by` (must be ordered before grouping, so `group` without `order` is not allowed). 
    2. `fold` must be preceded by `group`(`by`) or `windowed`. 
    3. `map` may or may not be preceded by `group`(`by`) or `windowed`. (`map` is allowed to take a single row as well.)
    4. No other cases are allowed for grouping to build tables. Therefore `by` cannot be preceded by `windowed` although it makes sense semantically. 

- To do the cross-join, consider passing a (lexical) closure on the method `map` to avoid repetitive table fetching.

```python
def fn():
    table2 = conn['t2'].list()
    def innerfn(rs):
        ...do some work using table2
        return something 
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
        return rs.update(n=n)
    return innerfn 

conn['t1_1'] = conn['t1'].by('col1').map(cnt())

```
Might not be that useful in any way though.


- `Rows` methods do not update objects directly. They create a new object every time a `Rows` method is invoked.

So the following code works as expected.
```python
rs = conn['t1']
rs.by('col1').fold(col2_tot=sum(rs['col2']))
```
In expression `sum(rs['col2'])`, `rs` represents a `Rows` object when the statement `rs = conn['t1']` is evaluated. Methods like `by` or `fold` in the statement do not affect `rs` in `sum(rs('col2'))`.

Take a close look at the next code snippet.

```python
def tempfn1(rs):
    # The original rs is not updated
    # Only newrs holds the instruction to update the column 'col2' 
    # (The update instruction will not be executed in the next statement, 
    # newrs simply keeps the instruction here for the time it's really needed, 
    # like for example, database insertion or content print-out)
    newrs = rs.update(col2=lambda r: r['col2'] + 1)
    return newrs.order('col2').zip(rs.order('col2 desc').rename(col2_1='col2'))

conn['t1_1'] = conn['t1'].by('col1').map(tempfn1)

``` 

- Since column names are dictionary keys, they are case-sensitive. However, column names in Sqlite3 are case-insensitive by default. To avoid confusion, it is strongly recommended that you keep them lower-cased, and spaces stripped. 
<!-- [Documentation]
(https://tablemap.readthedocs.io/en/latest/index.html)
 --> 
