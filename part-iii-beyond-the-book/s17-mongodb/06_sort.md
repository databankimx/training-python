## Sorting Query Results

One important function when working with a database is the ability to sort
the query results.

The `Cursor` object returned by the `find()` functions in PyMongo exposes
a `sort()` method to do exactly this.

As usual, in all examples below, we will assume that we have already
accessed the collection as `col`.

---

### Sorting a Result Set

To sort the results of a query, we pass one or more field names to the
`sort()` function.

```python
field = "name"
print(f"Sorting documents by field: {field}")
for doc in col.find({}, {"_id": 0}).sort(field):
    print(doc)
```

OUtput:

```
Sorting documents by field: name
{'name': 'Amy', 'address': 'Apple st 652'}
{'name': 'Ben', 'address': 'Park Lane 38'}
{'name': 'Betty', 'address': 'Green Grass 1'}
{'name': 'Chuck', 'address': 'Main Road 989'}
{'name': 'Hannah', 'address': 'Mountain 21'}
{'name': 'John', 'address': 'Highway 37'}
{'name': 'Michael', 'address': 'Valley 345'}
{'name': 'Richard', 'address': 'Sky st 331'}
{'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'name': 'Susan', 'address': 'One way 98'}
{'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'name': 'Viola', 'address': 'Sideway 1633'}
{'name': 'William', 'address': 'Central st 954'}
```

---

### Reversing a Sort

The `sort()` method accepts an optional argument specifying the sort order.

This argument can accept either the PyMongo constant or its value:

* ASCENDING: 1
* DESCENDING: -1

```python
field = "name"
print(f"Sorting documents by field: {field} (reversed)")
for doc in col.find({}, {"_id": 0}).sort(field, -1):
    print(doc)
```

Output:

```
Sorting documents by field: name (reversed)
{'name': 'William', 'address': 'Central st 954'}
{'name': 'Viola', 'address': 'Sideway 1633'}
{'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'name': 'Susan', 'address': 'One way 98'}
{'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'name': 'Richard', 'address': 'Sky st 331'}
{'name': 'Michael', 'address': 'Valley 345'}
{'name': 'John', 'address': 'Highway 37'}
{'name': 'Hannah', 'address': 'Mountain 21'}
{'name': 'Chuck', 'address': 'Main Road 989'}
{'name': 'Betty', 'address': 'Green Grass 1'}
{'name': 'Ben', 'address': 'Park Lane 38'}
{'name': 'Amy', 'address': 'Apple st 652'}
```

---
