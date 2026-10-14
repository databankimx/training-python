## Create a New Database

Before we can store any data, we need a database to put it in.

> Note: For the examples below, assume that we have already connected to 
> the server.

---

### Create a Database

After connecting to the server, create the new database in which our 
information will reside.

The SQL query for this is:

```sql
CREATE DATABASE IF NOT EXISTS DbName
```

In Python, the process looks like this:

```python
name = settings["schema"]
if conn.is_connected():
    sql = f"CREATE DATABASE IF NOT EXISTS {name}"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print(f"Database '{name}' created successfully!\n")
```

Output:

```
Database 'mydatabase' created successfully!
```

You'll notice one significant difference between this and the previous
exercise: this call...

```python
conn.commit()
```

Whenever we write to or modify the database, we must call the `commit()`
method to finalize the changes.

---

### Verification

We can verify that the database was created by repeating the previous
lesson's list databases process:

```python
sql = "SHOW DATABASES"
cursor.execute(sql)
print("DATABASES:")
for database in cursor:
    print(f" - {database[0]}")
```

Output:

```
DATABASES:
 - information_schema
 - mydatabase
 - mysql
 - performance_schema
 - sys
 - world
```

We see our database in the list, so we have successfully created it.

---
