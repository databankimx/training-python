## Create a MongoDB Database

When working with MongoDB, it's useful to validate that the database with 
which you need to interact exists.

---

### Get Settings and Connect

We'll use our `login.py` code to obtain the settings and database client
objects:

```python
from login import get_settings, get_client

settings = get_settings()
client = get_client()
print("MongoDB server is connected")
```

Output:

```
MongoDB server is connected
```

---

### Create the Database

In `pymongo`, we can create a database exactly the same way we would access
one that already exists.

`MongoClient[database_name]` creates the database if it does not exist and 
connects to it.

```python
db_name = settings["db_name"]
db = client[db_name]
print(f"Created database: `{db.name}`")
```

Output:

```
Created database: `mydatabase`
```

---

### List Databases

In `pymongo`, we can use the `list_database_names()` function to check if
our intended database exists.

```python
databases = client.list_database_names()
for db in databases:
    print(f"• {db}")
print(f"\n{db_name}", end = " ")
if db_name in db_names:
    print("exists")
else:
    print("does not exist")
client.close()
```

Output:

```
Available databases:
• admin
• config
• local

`mydatabase` does not exist
```

It may come as a surprise that the database we created does not appear when
we call the `list_database_names()` function.

This happens because In MongoDB, a database is not created until it 
contains some content.

Creating the collection (table) and inserting a record will complete the
database creation process.

Come back and re-run this code after you complete the next two lessons.

---
