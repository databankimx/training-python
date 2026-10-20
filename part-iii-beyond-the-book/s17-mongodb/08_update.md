## Update (Modify) Records

It's also important to be able to modify records in place in the database.

PyMongo provides the `update_one()` and `update_many()` methods to
facilitate record modifications.

Recall that after the previous lesson, we have these records in the
collection:

```
Documents in collection:
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

As usual, in all examples below, we will assume that we have already
accessed the collection as `col`.

---

### Update a Single Record

To update a record, we pass two arguments to the `update_one()` method:

* `query`: dictionary to match record(s)
* `update`: dictionary with `key` = `$set` and `value` = dictionary of field
  values to update.

If multiple records match the query, only the first will be updated.

```python
query = { "address": "Valley 345" }
update = { "$set": { "address": "Canyon 123" } }
print(f"Updating single document matching: `{query}`")
print(f"  with new values: `{update['$set']}`")
res = col.update_one(query, update)
print(f"Updated {res.modified_count} document(s)\n")
print("Documents in collection:")
for doc in col.find({}, {"_id": 0}):
    print(doc)
```

Output:

```
Updating single document matching: `{'address': 'Valley 345'}`
  with new values: `{'address': 'Canyon 123'}`
Updated 1 document(s)

Documents in collection:
{'name': 'John', 'address': 'Highway 37'}
{'name': 'Amy', 'address': 'Apple st 652'}
{'name': 'Michael', 'address': 'Canyon 123'}
{'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'name': 'Betty', 'address': 'Green Grass 1'}
{'name': 'Susan', 'address': 'One way 98'}
{'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'name': 'Ben', 'address': 'Park Lane 38'}
{'name': 'William', 'address': 'Central st 954'}
{'name': 'Chuck', 'address': 'Main Road 989'}
```

---

### Update Multiple Records

The `update_many()` method takes the same arguments as `update_one()`, but
all matching records will be updated.

```python
query = { "address": { "$regex": "^O" } }
update = { "$set": { "name": "Minnie" } }
print(f"Updating multiple document matching: `{query}`")
print(f"  with new values: `{update['$set']}`")
res = col.update_many(query, update)
print(f"Updated {res.modified_count} document(s)\n")
print("Documents in collection:")
for doc in col.find({}, {"_id": 0}):
    print(doc)
```

Output:

```
Updating multiple documents matching: `{'address': {'$regex': '^O'}}`
  with new values: `{'name': 'Minnie'}`
Updated 2 document(s)

Documents in collection:
{'name': 'John', 'address': 'Highway 37'}
{'name': 'Amy', 'address': 'Apple st 652'}
{'name': 'Michael', 'address': 'Canyon 123'}
{'name': 'Minnie', 'address': 'Ocean blvd 2'}
{'name': 'Betty', 'address': 'Green Grass 1'}
{'name': 'Minnie', 'address': 'One way 98'}
{'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'name': 'Ben', 'address': 'Park Lane 38'}
{'name': 'William', 'address': 'Central st 954'}
{'name': 'Chuck', 'address': 'Main Road 989'}
```

---
