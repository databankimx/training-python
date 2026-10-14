## Adding a Table to the Database

We need a table for `customers` in the database that contains the 
following data about each customer:

* `name`: A string of up to 255 characters containing the customer name
* `address`: A string of up to 255 characters containing the customer 
  address

---

### The Add Table Query

The SQL for adding a new table to the database is as follows:

```sql
CREATE TABLE table_name (column_name TYPE, ...)
```

For our table, the query will look something like this:

```sql
CREATE TABLE IF NOT EXISTS customers (
    name VARCHAR(255),
    address VARCHAR(255)
)
```

Putting that into Python, we have this:

```python
if conn.is_connected():
    sql = "CREATE TABLE IF NOT EXISTS customers " + \
          "(name VARCHAR(255), address VARCHAR(255))"
    cursor = conn.cursor()
    cursor.execute(sql)
```

---

### Verification

Let's verify that the table was created using SQL: `SHOW TABLES`

```python
if conn.is_connected():
    cursor = conn.cursor()
    sql = "SHOW TABLES"
    cursor.execute(sql)
    print("TABLES:")
    for table in cursor:
        print(f" - {table[0]}")
```

Output:

```
TABLES:
 - customers
```

---

### Adding an ID Column

In almost all circumstances, a table should include a column that acts as
an identifier for each row's value(s). This is called a *primary key*.

This identifier will be used when matching rows against other data tables.
Obviously, as an identifier, the values in this column must be unique.

The SQL syntax for adding a primary key looks like this:

```sql
ADD COLUMN column_name INT AUTO_INCREMENT PRIMARY KEY
```

We're going to modify the table we've already added. The syntax for that
looks like this:

```sql
ALTER TABLE table_name
```

For our example, the SQL will look like this:

```sql
ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY
```

Putting that into code, we'll do this:

```python
if conn.is_connected():
    sql = "ALTER TABLE customers " + \
          "ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
    cursor = conn.cursor()
    cursor.execute(sql)
```

---

### Verification

Let's verify that we successfully added all three columns.

SQL:

```sql
SHOW COLUMNS in customers
```

Python:

```python
if conn.is_connected():
    sql = "SHOW COLUMNS in customers"
    cursor = conn.cursor()
    cursor.execute(sql)
    print("COLUMNS in `customers`:")
    for column in cursor:
        print(f"- {column[0]} {column[1]}")
```

Output:

```
COLUMNS in `customers`:
- name varchar(255)
- address varchar(255)
- id int
```

---
