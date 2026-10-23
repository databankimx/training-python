## Creating a List and Accessing Values

A list is an ordered collection of items. Each item has a position, and you can
reach any item by asking for its position.

The items in a list don't have to be the same type. One list can hold strings,
numbers, and even other lists, which makes lists very flexible.

---

### Syntax

* Surround a list with square brackets `[]`
* Separate items with commas `,`
  e.g.:

  ```python
  numbers = [1, 2, 3, 4, 5]
  number_names = ["one", "two", "three"]
  ```

---

### Indexing

List indexes start at zero, so the first item is at position `0`, not `1`. You
can also count backward from the end, which is handy when you don't know how long
the list is:

* The first item is always `list_name[0]`
* The last item is always `list_name[-1]`

Those two work no matter how long the list is.

---

> ### Why Do We Count From Zero?
>
> It looks like an odd choice, but it comes from how the computer finds an item.
>
> A Python list is an *array* of references. Each slot in the array holds a
> pointer to an object, and the objects can be any type. The array sits in one
> block of memory, and the list stores where that block begins.
>
> To find the item at position `n`, Python starts at the beginning of the block
> and moves forward `n` slots. Position `0` is zero slots away from the start, so
> it's the easiest place to find. That's the whole reason.
>
> Languages like C and C++ use the same idea, and there the slots are the size of
> the data type. An `int` is four bytes, so position `2` is eight bytes past the
> start. Python does the same thing, with pointer-sized slots.
>
> You don't need the memory details to use lists. Just remember that position `0`
> is the first item, and it's always the first.

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

If you ask for a position the list doesn't have, Python raises an `IndexError`.

This list has three items, at positions `0`, `1`, and `2`. Asking for position `3`
fails, because there's nothing there. Save this as `index_error.py` and run it to
see the error for yourself:

```python
my_list = [1, 2, 3]
print(my_list[3])
```

Output:

```
Traceback (most recent call last):
  File "...\index_error.py", line 2, in <module>
    print(my_list[3])
          ~~~~~~~^^^
IndexError: list index out of range
```

---
