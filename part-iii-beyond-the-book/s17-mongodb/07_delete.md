## Deleting Records from a MongoDB Database

From time to time, you will need to remove records from the database.

The `Collection` object exposes the `delete_one()` and `delete_many()` 
methods to accomplish this task:

As usual, in all examples below, we will assume that we have already
accessed the collection as `col`.

---

### Delete a Single Record

Like the `find()` methods, the `delete_one()` method accepts a query to
identify matching record(s). Using `delete_one()`, if multiple records
match the query, only one record will be removed.

```python
query = { "address": "Mountain 21" }
print(f"Deleting document matching query: {query}")
result = col.delete_one(query)
print(f"Deleted {result.deleted_count} document(s)\n")
print("Remaining documents in collection:")
for doc in col.find({}, {"_id": 0}):
    print(doc)
```

Output:

```
Deleting document matching query: {'address': 'Mountain 21'}
Deleted 1 document(s)

Remaining documents in collection:
{'name': 'John', 'address': 'Highway 37'}
{'name': 'Amy', 'address': 'Apple st 652'}
{'name': 'Michael', 'address': 'Valley 345'}
{'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'name': 'Betty', 'address': 'Green Grass 1'}
{'name': 'Richard', 'address': 'Sky st 331'}
{'name': 'Susan', 'address': 'One way 98'}
{'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'name': 'Ben', 'address': 'Park Lane 38'}
{'name': 'William', 'address': 'Central st 954'}
{'name': 'Chuck', 'address': 'Main Road 989'}
{'name': 'Viola', 'address': 'Sideway 1633'}
```

---

### Delete Multiple Records

The `delete_many()` method functions just like the `delete_one()` method
except that it deletes all records matching the given query.

```python
query = {"address": {"$regex": "^S"}}
print(f"Deleting document(s) matching query: {query}")
result = col.delete_many(query)
print(f"Deleted {result.deleted_count} document(s)\n")
print("Remaining documents in collection:")
for doc in col.find({}, {"_id": 0}):
    print(doc)
```

Output:

```
Deleting document(s) matching query: {'address': {'$regex': '^S'}}
Deleted 2 document(s)

Remaining documents in collection:
{'name': 'John', 'address': 'Highway 37'}
{'name': 'Amy', 'address': 'Apple st 652'}
{'name': 'Michael', 'address': 'Valley 345'}
{'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'name': 'Betty', 'address': 'Green Grass 1'}
{'name': 'Susan', 'address': 'One way 98'}
{'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'name': 'Ben', 'address': 'Park Lane 38'}
{'name': 'William', 'address': 'Central st 954'}
{'name': 'Chuck', 'address': 'Main Road 989'}
```

---

### Delete All Records from a Collection

To delete all documents in a collection, we would pass an empty query
dictionary to the `delete_many()` method:

```python
col.delete_many({})
```

I have included an example in the sample code file but have not executed it,
so we can continue to work with the existing record set.

---
