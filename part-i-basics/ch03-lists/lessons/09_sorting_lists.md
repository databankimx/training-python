## Sorting and Reversing Lists

Python provides several functions for sorting and reversing lists. The key
decision is whether to modify the original list or work with a copy.

| Function | Effect |
|-|-|
| `list.sort()` | Sorts the list in place (permanent) |
| `sorted(list)` | Returns a sorted copy; original unchanged |
| `list.reverse()` | Reverses the list in place (permanent) |
| `reversed(list)` | Returns an iterator over a reversed copy |

---

### Sorting In-Place

`list.sort()` modifies the list permanently.

```python
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)
```

Output:

```
['audi', 'bmw', 'subaru', 'toyota']
['toyota', 'subaru', 'bmw', 'audi']
```

You **cannot** sort a mixed-type list - types can only compare against
themselves:

```python
my_list = [5, "banana", 1, "date"]
my_list.sort()  # TypeError
```

---

### Sorting a Copy

`sorted()` returns a sorted copy and leaves the original unchanged.

```python
cars = ["bmw", "audi", "toyota", "subaru"]
print(sorted(cars))
print(cars)  # unchanged
```

Output:

```
['audi', 'bmw', 'subaru', 'toyota']
['bmw', 'audi', 'toyota', 'subaru']
```

Both `sort()` and `sorted()` accept `reverse=True` and a `key` argument
(covered in a later lesson).

---

### Reversing In-Place

`list.reverse()` reverses the order without sorting. The change is permanent.

```python
cars = ["bmw", "audi", "toyota", "subaru"]
cars.reverse()
print(cars)
```

Output:

```
['subaru', 'toyota', 'audi', 'bmw']
```

---

### Reversing a Copy

`reversed()` returns an iterator. Convert it to a list before printing.

```python
cars = ["bmw", "audi", "toyota", "subaru"]
print(list(reversed(cars)))
print(cars)  # unchanged
```

Output:

```
['subaru', 'toyota', 'audi', 'bmw']
['bmw', 'audi', 'toyota', 'subaru']
```

---

### Remembering Which Is Which

> The functions that end in the letter **d** - `sorted()` and `reversed()` -
> are the ones that create a **d**uplicate copy instead of modifying the
> original.

---

### List Length

`len()` returns the number of items in a list.

```python
cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))
```

Output:

```
4
```

---
