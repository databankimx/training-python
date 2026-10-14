## Removing Tables and Database

We're going to remove the database and tables we created during this 
lesson just to clean up after ourselves.

---

### Removing a Table with `DROP TABLE`

It is rare that you would remove tables from a production database, but
during the design and development process, you may add and remove tables multiple times over.

The syntax to remove a table from a database is:

```sql
DROP TABLE table_name
```

To suppress errors in case the table is already removed, we can add the
`IF EXISTS` condition:

```sql
DROP TABLE IF EXISTS table_name
```

---

#### The Code

So, cleaning up our tables will look like this:

```python
if conn.is_connected():
    tables = ["customers", "users", "products"]
    for table in tables:
        sql = f"DROP TABLE IF EXISTS {table}"
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print(f"Table {table} dropped")
```

Output:

```
Table customers dropped
Table users dropped
Table products dropped
```

---

#### Validation

We can verify that the tables were dropped with the same code we used to
list tables in the create tables lesson:

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
```

No tables are listed any more.

---

### Removing a Database with `DROP DATABASE`

Sometimes you need to remove a database in its entirety from the MySQL
server.

The syntax to remove a database is:

```sql
DROP DATABASE database_name
```

To suppress errors in case the database is already removed, we can add the
`IF EXISTS` condition:

```sql
DROP DATABASE IF EXISTS database_name
```

---

#### The Code

So, cleaning up our tables will look like this:

```python
if conn.is_connected():
    db = "mydatabase"
    sql = f"DROP DATABASE IF EXISTS {db}"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print(f"Database {db} dropped")
```

Output:

```
Database mydatabase dropped
```

---

#### Validation

We can verify that the database was dropped with the same code we used to
list databases in the create database lesson:

```python
if conn.is_connected():
    cursor = conn.cursor()
    sql = "SHOW DATABASES"
    cursor.execute(sql)
    print("DATABASES:")
    for table in cursor:
        print(f" - {table[0]}")
```

Output:

```
DATABASES:
 - information_schema
 - mysql
 - performance_schema
 - sys
 - world
```

We no longer see 'mydatabase' listed.

---
