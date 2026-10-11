## Creating a List and Accessing Values

Lists are ordered collections of items. Items in a Python list do not need to
be of the same data type.

---

### Syntax

- Surround a list with square brackets `[]`
- Separate items with commas `,`

```python
numbers = [1, 2, 3, 4, 5]
number_names = ["one", "two", "three"]
```

---

### Indexing

List indices are zero-based and support backward-indexing, so:

- First item is always `list_name[0]`
- Last item is always `list_name[-1]`

...regardless of list length.

---

> ### Why Do We Count From Zero, Not One?
>
> In many languages, a list is built on an underlying `array`. The array
> variable holds a pointer to where the array starts in memory. The index
> defines how far to move from that starting point, in units the size of
> the element type.
>
> For a C++ `int` (4 bytes):
>
> | Index | Location |
> |:-:|:-:|
> | `0` | `start + 0 * 4 = start + 0` |
> | `1` | `start + 1 * 4 = start + 4` |
> | `2` | `start + 2 * 4 = start + 8` |
>
> Since the first element is at the starting location, its offset is zero -
> hence index zero.
>
> Python's `list` is actually a linked list, where each element contains a
> value and a link to the next element. The first element is still at the
> start of the structure, so it still has index zero.

---

### Examples

```python
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[1].title())
print(bicycles[-2].upper())

message = f"My favorite bicycle was a {bicycles[0].title()}."
print(message)
```

Output:

```
['trek', 'cannondale', 'redline', 'specialized']
trek
specialized
Cannondale
REDLINE
My favorite bicycle was a Trek.
```

---

### Avoid Index Errors

Requesting an index that does not exist produces an `IndexError`:

```python
my_list = [1, 2, 3]
print(my_list[3])
```

Output:

```
Traceback (most recent call last):
  File "...\creating_a_list.py", line 2, in <module>
    print(my_list[3])
          ~~~~~~~^^^
IndexError: list index out of range
```

---
