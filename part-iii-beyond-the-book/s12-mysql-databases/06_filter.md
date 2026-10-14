## Filtering Results with a `WHERE` clause

Often, there will be many more records in a table than we want or need.

We can filter the results to only include those that match criteria we
set in a `WHERE` clause.

---

### A `WHERE` Equal Clause

We can retrieve only records where a column equals a specified value:

```sql
SELECT * FROM table WHERE column = value
```

```python
if conn.is_connected():
    sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
```

Output:

```
('Ben', 'Park Lane 38', 11)
```

> Note: We can also use any of the logical comparison operators:
> |operator|meaning|
> |:-:|-|
> |`<`|less than|
> |`<=`|less than or equal|
> |`>`|greater than|
> |`>=`|greater than or equal|
> |`!=` or `<>`|note equal|

---

### A `WHERE` Like Clause

We can retrieve only records where a column contains a specified value as
part of its value.

For this we use the term `LIKE` instead of a logic operator and one or 
more wild card characters `%`

|usage|meaning|
|-|-|
|`value%`|starts with|
|`%value`|ends with|
|`%value%`|contains|

For our scenario, we'll use a query like this:

```sql
SELECT * FROM customers WHERE address LIKE '%way%'
```

```python
if conn.is_connected():
    sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
    cursor = conn.cursor()
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
```

Output:

```
('John', 'Highway 21', 1)
('Susan', 'One way 98', 9)
('Viola', 'Sideway 1633', 14)
```

You see that this brought back all rows where the address contains the
term "way" anywhere in the value.

---

### Parameterization

We previously discussed parameterization of values when populating data.
The same tactic is just as vital when retrieving data. You should never
include a where clause without parameterizing the values.

The technique is similar:

```python
if conn.is_connected():
    sql = "SELECT * FROM customers WHERE address =%s"
    params = ("Yellow Garden 2",)
    cursor = conn.cursor()
    cursor.execute(sql, params)
    for row in cursor.fetchall():
        print(row)
```

Output:

```
('Vicky', 'Yellow Garden 2', 10)
```

---
