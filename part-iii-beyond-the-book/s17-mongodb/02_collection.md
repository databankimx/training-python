## Create a MongoDB Collection

Data in a MongoDB database is stored in collections, so our next step is to 
create a MongoDB collection.

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

### Get Database and Create Collection

Now that we have a client connected, we can access the database and create
a collection. Creating a collection from a MongoDB database is the same as
creating a MongoDB database from a client: `database[collection_name]`

```python
db = client[settings["db_name"]]
print(f"Connected to database: `{db.name}`\n")

collection = db[settings["col_name"]]
print(f"Created collection: `{collection.name}`")
```

Output:

```
Connected to database: `mydatabase`

Created collection: `customers`
```

---

### List the Collections in the Database

From the database object, we can execute the `list_collection_names()`
method to provide a list of its collections:

```python
print(f"Collections in database `{db.name}`:")
for collection in collections:
    print(f"• {collection}")
print()
col_name = settings["col_name"]
print(f"Collection `{col_name}`", end=" ")
if col_name in collections:
    print("exists\n")
else:
    print("does not exist\n")
```

Output:

```
Collections in database `mydatabase`:

Collection `customers` does not exist
```

Just like the database is incomplete until a collection is added, the 
collection is incomplete until it contains at least one record, which is
why it does not yet appear in the list:

---
