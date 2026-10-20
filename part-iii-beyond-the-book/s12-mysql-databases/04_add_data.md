## Add Data to a Table

Now that we have a database and a table, we're ready to add some data.

---

### The `INSERT` Query:

The basic syntax for inserting new rows into a database table is:

```sql
INSERT INTO table_name (col_1, col_2, ...) VALUES (val_1, val_2, ...)
```

If we want to insert a record with

* `name` = "John"
* `address` = "Highway 21"

The query looks like this:

```sql
INSERT INTO customers (name, address) VALUES ('John', 'Highway 21')
```

---

### Parameterization

If the values are stored in variables, it can be tempting to embed them
directly into the SQL like this:

```python
sql = f"INSERT INTO customers (name, address) VALUES ({name}, {address})"
```

But this is a problem. We never want to embed variable data in a SQL
query, because it's possible that the variable data could include SQL
commands (a security attack known as *SQL Injection*).

To prevent SQL injection, we need to parameterize the query.
Parameterization involves two steps:

1. Replace the values with a placeholder symbol `%s`.
2. Substitute the values back in your Python code.

When values are substituted in using parameterization, Python will 
automatically convert anything in the value that could be interpreted as
SQL commands into escaped plain text.

In Python, we pass the values to the parameterized SQL as a tuple:

```python
values = ("John", "Highway 21")
if conn.is_connected():
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()
    print(f"{cursor.rowcount} row(s) inserted.")
    print(f"Last inserted ID: {cursor.lastrowid}\n")
```

Output:

```
1 row(s) inserted.
Last inserted ID: 1
```

---

### Adding Multiple Rows

The process to add multiple rows is the same as a single row except for
two items:

1. Use the `cursor.executemany()` function instead of `cursor.execute()`
2. Pass values as a list of tuples

```python
values = [
    ("Peter", "Lowstreet 4"),
    ("Amy", "Apple st 652"),
    ("Hannah", "Mountain 21"),
    ("Michael", "Valley 345"),
    ("Sandy", "Ocean blvd 2"),
    ("Betty", "Green Grass 1"),
    ("Richard", "Sky st 331"),
    ("Susan", "One way 98"),
    ("Vicky", "Yellow Garden 2"),
    ("Ben", "Park Lane 38"),
    ("William", "Central st 954"),
    ("Chuck", "Main Road 989"),
    ("Viola", "Sideway 1633")
]
if conn.is_connected():
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    cursor = conn.cursor()
    cursor.executemany(sql, values)
    conn.commit()
    print(f"{cursor.rowcount} row(s) inserted.")
    print(f"Last inserted ID: {cursor.lastrowid}\n")
```

Output:

```
13 row(s) inserted.
Last inserted ID: 2
```

Note: The `cursor.lastrowid` value from a call to `executemany()` will be
the ID of the first of the multiple added rows.

---

### Add One More Row

Just for good measure, let's add another row:

```python
values = ("Michelle", "Blue Village")
if conn.is_connected():
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()
    print(f"{cursor.rowcount} row(s) inserted.")
    print(f"Last inserted ID: {cursor.lastrowid}\n")
```

Output:

```
1 row(s) inserted.
Last inserted ID: 15
```

You can see that we've now inserted 15 rows into the table

---
