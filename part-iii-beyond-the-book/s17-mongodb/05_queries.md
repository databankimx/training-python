## Filtering with Queries

When applying a filter query to a `find()` call, you ca substitute a
dictionary for a value in order to further refine the query.

As usual, in all examples below, we will assume that we have already
accessed the collection as `col`.

---

### Simple Value Query

In the previous lesson, we used a simple key-value pair dictionary to
filter a `find()`.

```python
query = {"name": "John"}
proj = {"_id": 0}
print(f"Performing simple query: {query}")
for doc in col.find(query, proj):
    print(doc)
```

Output:

```
Performing simple query: {'name': 'John'}
{'name': 'John', 'address': 'Highway 37'}
```

---

### Comparison Query

In place of a value in the filter dictionary, we can implement a second
dictionary that contains a comparison to a value.

Comparison sub-queries take the form `{comparison: value}`, where the
comparisons include:

* `$gt`: greater than value
* `$ge`: greater than or equal to value
* `$lt`: less than value
* `$le`: less than or equal to value

```python
query = {"address": {"$gt": "S"}}
proj = {"_id": 0}
print(f"Performing advanced query: {query}")
for doc in col.find(query, proj):
    print(doc)
```

Output:

```
Performing advanced query: {'address': {'$gt': 'S'}}
{'name': 'Michael', 'address': 'Valley 345'}
{'name': 'Richard', 'address': 'Sky st 331'}
{'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'name': 'Viola', 'address': 'Sideway 1633'}
```

---

### Regex Query

You can also use a regular expression value in the sub-query dictionary by
specifying the `$regex` key.

```python
query = {"address": {"$regex": "^S"}}
proj = {"_id": 0}
print(f"Performing advanced query: {query}")
for doc in col.find(query, proj):
    print(doc)
```

Output:

```
Performing regex query: {'address': {'$regex': '^S'}}
{'name': 'Richard', 'address': 'Sky st 331'}
{'name': 'Viola', 'address': 'Sideway 1633'}
```

---
