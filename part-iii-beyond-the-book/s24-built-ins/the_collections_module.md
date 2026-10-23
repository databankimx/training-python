## The `collections` Module

The `collections` module provides container types that go beyond the built-in
`list`, `dict`, and `tuple`. This lesson covers four of them that come up often.

The code for this lesson is in [the_collections_module.py](./the_collections_module.py):

```python
from collections import Counter, defaultdict, deque, namedtuple

letters = Counter("mississippi")
print(letters)
print(letters.most_common(2))

groups = defaultdict(list)
for name, dept in [("Ana", "sales"), ("Ben", "tech"), ("Cy", "sales")]:
    groups[dept].append(name)
print(dict(groups))

queue = deque(["first", "second"])
queue.append("third")
queue.appendleft("zero")
print(queue.popleft())
print(queue)

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)
print(p)
```

---

### `Counter`: Counting Items

`Counter` takes any iterable and counts how often each item appears. Its
`most_common()` method returns the most frequent items with their counts:

```python
letters = Counter("mississippi")
print(letters)
print(letters.most_common(2))
```

Output:

```
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
[('i', 4), ('s', 4)]
```

The counts are shown in descending order. The two items with four occurrences
are tied, so they appear in the order they were first seen in the string.

---

### `defaultdict`: Missing Keys Get a Default

With a plain `dict`, adding to a list under a new key first requires creating the list.
A `defaultdict` creates it for you, using the factory you pass in. Here the factory is `list`:

```python
groups = defaultdict(list)
for name, dept in [("Ana", "sales"), ("Ben", "tech"), ("Cy", "sales")]:
    groups[dept].append(name)
print(dict(groups))
```

Output:

```
{'sales': ['Ana', 'Cy'], 'tech': ['Ben']}
```

The first time `"sales"` is used, `groups["sales"]` is missing, so `defaultdict`
calls `list()` to create an empty list and then the `append()` runs on it.

> Note: `dict.setdefault()` does the same job, and it's covered in the lesson on
> [`setdefault()`](./the_setdefault_function.md).

---

### `deque`: A Fast Queue

A `list` is quick to add to and remove from its end, but slow to remove from its start,
because every other item has to move. A `deque` is quick at both ends:

```python
queue = deque(["first", "second"])
queue.append("third")
queue.appendleft("zero")
print(queue.popleft())
print(queue)
```

Output:

```
zero
deque(['first', 'second', 'third'])
```

`popleft()` removes and returns the item at the front. A `deque` is the right
choice for a first-in, first-out queue.

---

### `namedtuple`: A Tuple with Names

A `namedtuple` is a tuple whose fields can be read by name, as well as by position.
It's useful when a tuple holds a small fixed record:

```python
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)
print(p)
```

Output:

```
3 4
Point(x=3, y=4)
```

A `namedtuple` is still immutable, like any tuple. For a record you need to
change, a `dataclass` is the better choice.

---

### Try It

Use `Counter` to count the words in a sentence. Then use `most_common(3)` to show
the three most frequent words.

---
