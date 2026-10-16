## Removing the Collection and Database

To perform a final cleanup of our practice work, we'll review how to remove
the collection and database from MongoDB.

For the examples below, we'll assume that we have already obtained the 
`MongoClient` as `client` and `Database` as `db`

---

### Drop Collection

To remove the collection from the database, we'll use the
`drop_collection()` method on the `Database` object.

Note: We could also use the `drop()` method on the `Collection` object.

```python
col_name = settings["col_name"]

print(f"Collections in database `{db.name}`:")
for name in db.list_collection_names():
    print(f"• {name}")
print()

print(f"Removing collections: `{col_name}`...")
if col_name in db.list_collection_names():
    db.drop_collection(col_name)
    print(f"Collection '{col_name}' removed successfully.")
else:
    print(f"Collection '{col_name}' does not exist.")
print()

print(f"Collections in database `{db.name}`:")
for name in db.list_collection_names():
    print(f"• {name}")
```

Output:

```
Collections in database `mydatabase`:
• customers

Removing collections: `customers`...
Collection 'customers' removed successfully.

Collections in database `mydatabase`:
```

The `customers` collection no longer exists

---

### Drop Database

To remove the database, we'll use the `drop_database()` method on the
`MongoClient` object.

```python
db_name = settings["db_name"]

print("Available databases:")
for name in client.list_database_names():
    print(f"• {name}")

print(f"Removing database: `{db_name}`...")
client.drop_database(db_name)
print(f"Database '{db_name}' removed.\n")

print("Available databases:")
for name in client.list_database_names():
    print(f"• {name}")
```

Output:

```
Available databases:
• admin
• config
• local

Removing database: `mydatabase`...
Database 'mydatabase' removed.

Available databases:
• admin
• config
• local
```

Note that just as when we started, once the database no longer contains a 
collection and at least one record, it does not appear in the list, even 
before we drop it.

---

### More Practice

Now, we've restored the system to its original state. You can go back and
re-run the previous lessons or practice with additional data on your own.

---
