## Insert a Record

The final step in creating our database is to add some data to the
collection.

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

### Get Database and Collection

Now we can access the database and collection in preparation for inserting
data.

```python
db = client[settings["db_name"]]
print(f"Connected to database: `{db.name}`\n")
col = db[settings["col_name"]]
print(f"Connected to collection: `{col.name}`")
```

Output:

```
Connected to database: `mydatabase`

Connected to collection: `customers`
```

---

### Insert a Record into the Collection

In MongoDB, we can pass a new record (document) as a dictionary.

To insert a single record into the collection, we can call the 
`insert_one(doc)` method.

The result object contains a property `inserted_id` from which we can 
verify the ID that the record was stored as.

```python
doc = { "name": "John", "address": "Highway 37" }

print(f"Inserting document into collection...\n{data}")
result = col.insert_one(data)
id = result.inserted_id
print(f"Document inserted successfully as ID: `{id}`")
```

Output:

```
Inserting document into collection...
{'name': 'John', 'address': 'Highway 37'}
Document inserted successfully as ID: `66eee383db7a839efd6eac63`
```

> Note: MongoDB will add a unique ID automatically when the document is
> inserted. If you wish to override this behavior, you can specify the
> `_id` in the dictionary for the document:
>
> e.g.: `{ "_id": 1, "name": "John", "address": "Highway 37" }`

---

### Insert Multiple Documents into a Collection

The `insert_many(docs)` method allows us to insert multiple documents
at the same time.

```python
docs = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
]
print("Inserting multiple documents into collection...")
for doc in data:
    print(f"• {doc}")
_ = col.insert_many(data)
print("Documents inserted successfully.\n")
```

Output:

```
Inserting multiple documents into collection...
• {'name': 'Amy', 'address': 'Apple st 652'}
• {'name': 'Hannah', 'address': 'Mountain 21'}
• {'name': 'Michael', 'address': 'Valley 345'}
• {'name': 'Sandy', 'address': 'Ocean blvd 2'}
• {'name': 'Betty', 'address': 'Green Grass 1'}
• {'name': 'Richard', 'address': 'Sky st 331'}
• {'name': 'Susan', 'address': 'One way 98'}
• {'name': 'Vicky', 'address': 'Yellow Garden 2'}
• {'name': 'Ben', 'address': 'Park Lane 38'}
• {'name': 'William', 'address': 'Central st 954'}
• {'name': 'Chuck', 'address': 'Main Road 989'}
• {'name': 'Viola', 'address': 'Sideway 1633'}
Documents inserted successfully.
```

---

### Validation

Make sure to go back and re-run the previous two lessons:

[Creating a Database](./01_create_db.py)

Output:

```
...

Available databases:
• admin
• config
• local
• mydatabase

`mydatabase` exists
```

Now that we have added a collection and a record, the database appears in
the list.

. . . . . . . . . .

[Creating a Collection](./02_collection.py)

Output:

```
...

Collections in database `mydatabase`:
• customers

Collection `customers` exists
```

Now that we have added a record, the collection appears in the database.

---
