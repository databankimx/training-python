## Find Data

PyMongo provides the `find_one()` and `find()` methods to retrieve data 
from the database.

For the exercises below, we'll assume that we have already obtained a
collection `col` by connecting to the database.

---

### Retrieve the First Record

The `find_one()` method retrieves the first record from the collection.

If you are familiar with SQL:

```sql
-- `collection.find_one()` is similar to
SELECT * FROM collection LIMIT 1;
```

```python
print("Find One Record:")
res = col.find_one()
print(res)
```

Output:

```
Find One Record:
{'_id': ObjectId('66...c63'), 'name': 'John', 'address': 'Highway 37'}
```

---

### Retrieve All Records in the Collection

The `find_all()` method retrieves all records from the collection.

If you are familiar with SQL:

```sql
-- `collection.find()` is similar to
SELECT * FROM collection;
```

```python
print("Find All Records:")
for doc in col.find():
    print(doc)
```

Output:

```
Find All Records:
{'_id': ObjectId('66...c63'), 'name': 'John', 'address': 'Highway 37'}
{'_id': ObjectId('66...c64'), 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': ObjectId('66...c65'), 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': ObjectId('66...c66'), 'name': 'Michael', 'address': 'Valley 345'}
{'_id': ObjectId('66...c67'), 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': ObjectId('66...c68'), 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': ObjectId('66...c69'), 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': ObjectId('66...c6a'), 'name': 'Susan', 'address': 'One way 98'}
{'_id': ObjectId('66...c6b'), 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': ObjectId('66...c6c'), 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': ObjectId('66...c6d'), 'name': 'William', 'address': 'Central st 954'}
{'_id': ObjectId('66...c6e'), 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': ObjectId('66...c6f'), 'name': 'Viola', 'address': 'Sideway 1633'}
```

---

### Filter Results

The `find_one()` and `find()` functions accept several optional arguments,
the first of which is `filter`, which takes a dictionary containing values
to match when searching the collection.

```sql
-- `collection.find({"key": "value"})` is similar to
SELECT * FROM collection WHERE key = 'value';
```

```python
f = {"name": "John"}
print(f"Find Records with Filter {f}:")
for doc in col.find(f):
    print(doc)
```

Output:

```
Find Records with Filter {'name': 'John'}:
{'_id': ObjectId('66...c63'), 'name': 'John', 'address': 'Highway 37'}
```

---

### Ignore Columns

The second optional argument is the `projection`, in which we can specify
what fields are returned. This accepts a dictionary containing fields as
keys and `0` to exclude a field from being returned. By default, all other
fields in the `projection` contain `1`, so that does not need to be
specified.

Since our collection contains three fields: `_id`, `_name`, and `address`:

```sql
-- `col.find({}, {"_id": 0})` is similar to
SELECT name, address FROM collection;
```

If we pass the `projection` positionally we must either pass a filter or an
empty dictionary to indicate no filtering.

```python
f = {}
p = {"_id": 0}
print("Find All Records (excluding `_id`):")
for doc in col.find(f, p):
    print(doc)
```

Output:

```
Find All Records (excluding `_id`):
{'name': 'John', 'address': 'Highway 37'}
{'name': 'Amy', 'address': 'Apple st 652'}
{'name': 'Hannah', 'address': 'Mountain 21'}
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
