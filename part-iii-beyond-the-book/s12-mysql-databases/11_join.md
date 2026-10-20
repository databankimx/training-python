## Getting Data from Multiple Tables

> **Important Note!**  
> Please execute the pre-lesson code in
> [prep_tables.py](./prep_tables.py) before running any code in this 
> lesson. This will create and populate the additional tables we'll need
> in order to practice joins.

Frequently, it is necessary to query for information from more than one 
table at a time.

It's possible to perform sub-queries (where we would `SELECT` from the
results of another `SELECT` query), but these can be awkward to code and
often perform poorly.

Instead, we will use `JOIN` clauses.

---

### Sample Data

We have added two tables containing the following data:

`users`

|id|name|fav|
|-|-|-|
|1|John|154|
|2|Peter|154|
|3|Amy|155|
|4|Hannah||
|5|Michael||

`products`

|id|name|
|-|-|
|154|Chocolate Heaven|
|155|Tasty Lemons|
|156|Vanilla Dreams|

---

### Common Values

Reviewing the sample data, we can see that items in the `fav` column of
the `users` table match up with `id` values in `products`.

We use these data relationships (from which *relational databases* get
their name) to define the conditions for a join.

---

### Syntax and Structure of a `JOIN` Clause

The basic syntax for a `JOIN` looks like this:

```sql
SELECT table_1.col_1, table_2.col_2, ...
FROM table_1
JOIN_TYPE JOIN table_2 ON table_1.some_col = table_2.some_col
```

There are three different types of `JOIN` clauses:

|Type|Row is returned if...|
|-|-|
|`INNER JOIN`|Both tables have matched values for the compared column|
|`LEFT OUTER JOIN`|All rows from the left (first) table, whether or not the right table has a value|
|`RIGHT OUTER JOIN`|All rows from the right (second) table, whether or not the left table has a value|

---

### An `INNER JOIN`

Let's retrieve users' names and favorite flavors using an inner join.

```sql
SELECT users.name, products.name
FROM users
INNER JOIN products ON users.fav = products.id
```

```python
if conn.is_connected():
    sql = "SELECT users.name, products.name FROM users " + \
          "INNER JOIN products ON users.fav = products.id"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
```

Output:

```
('John', 'Chocolate Heaven')
('Peter', 'Chocolate Heaven')
('Amy', 'Tasty Lemons')
```

You can see that the only rows returned are where there is a match 
between the `users.fav` and `products.id` columns.

---

### A `LEFT OUTER JOIN`

Let's retrieve users' names and favorite flavors using a left outer join.

```sql
SELECT users.name, products.name
FROM users
LEFT OUTER JOIN products ON users.fav = products.id
```

```python
if conn.is_connected():
    sql = "SELECT users.name, products.name FROM users " + \
          "LEFT OUTER JOIN products ON users.fav = products.id"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
```

Output:

```
('John', 'Chocolate Heaven')
('Peter', 'Chocolate Heaven')
('Amy', 'Tasty Lemons')
('Hannah', None)
('Michael', None)
```

You can see that all rows from the `users` table are returned, regardless of whether there is a match to the `products` table.

---

### A `RIGHT OUTER JOIN`

Let's retrieve users' names and favorite flavors using a right outer 
join.

```sql
SELECT users.name, products.name
FROM users
RIGHT OUTER JOIN products ON users.fav = products.id
```

```python
if conn.is_connected():
    sql = "SELECT users.name, products.name FROM users " + \
          "RIGHT OUTER JOIN products ON users.fav = products.id"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
```

Output:

```
('Peter', 'Chocolate Heaven')
('John', 'Chocolate Heaven')
('Amy', 'Tasty Lemons')
(None, 'Vanilla Dreams')
```

You can see that all rows from the `products` table are returned, regardless of whether there is a match to the `users` table.

---
