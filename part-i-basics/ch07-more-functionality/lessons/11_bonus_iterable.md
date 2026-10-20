## Bonus Lesson: Using `iter()`

Iteration is a key to the processing of collections of information. We have
already looked at iteration in the form of loops, but sometimes, it is 
necessary to approach iteration with more direct, granular control.

For this, Python exposes the `iter()` function, which returns an `iterator`
object, which in turn exposes a `next()` function to perform iterations.

Using `iter()` offers several advantages over loops:

* Efficient Iteration: When traversing a collection, access one element at 
  a time instead of loading the entire collection into memory.
* Lazy Evaluation: Generate values only as needed, which is useful when 
  dealing with infinite (or very large) sequences.
* Granular Control: Perform each iteration only when your code indicates 
  that it is needed, and stop iterating when desired.

---

### TypeError with `iter()`

The `iter()` function will throw a TypeError if the argument passed is not
an iterable type.

```python
iter(None)
```

Output:

```
Traceback (most recent call last):
  File "...\11_bonus_iterable.py", line 40, in <module>
    main()
  File "...\11_bonus_iterable.py", line 25, in main
    iter(None)
TypeError: 'NoneType' object is not iterable
```

---

### Checking if a Variable is Iterable

To avoid these errors, it is useful to check if a variable is iterable. We
can accomplish this using a `try`/`except` block.

```python
from typing import Iterable

def is_iterable(obj: any) -> Iterable|None:
    """Check if the given object is iterable"""
    try:
        return iter(obj)
    except TypeError:
        return None

x = None
if not (iter_obj := is_iterable(x)):
    print(f"`{type(x).__name__}` is not iterable.\n")
```

Output:

```
'NoneType' is not iterable
```

We're now able to identify if an object is iterable and generate an 
iterator from it. Now we need to use the `next()` method to perform the
iterations.

---

### The `StopIteration` Error

There is a problem with simply calling `next()` in a loop without checking if the iterator has more elements.

```python
arr = [1, 2, 3]
if not (iter_obj := is_iterable(arr)):
    print(f"`{type(arr).__name__}` is not iterable.\n")
    exit()
while True:
    print(next(iter_obj))
```

Output:

```
1
2
3
Traceback (most recent call last):
  File "...\11_bonus_iterable.py", line 41, in <module>
    main()
  File "...\11_bonus_iterable.py", line 29, in main
    print(next(iter_obj))
          ^^^^^^^^^^^^^^
StopIteration
```

Once the iterator is exhausted, calling `next()` will raise a `StopIteration` error.

---

### Fixing the `StopIteration` Problem

We could use a `for` loop or a counter variable to limit the number of
iterations, and that would work fine for types like `list` or `tuple`,
but if we're working with something like a text file (type:
`TextIOWrapper`) the lazy-load behavior of the iterator means we don't
know how many iterations to perform in advance.

We can fix this issue by again using a `try`/`except` block.

```python

arr = [1, 2, 3]
if not (iter_obj := is_iterable(arr)):
    print(f"`{type(arr).__name__}` is not iterable.\n")
    exit()
while True:
    try:
        print(next(iter_obj))
    except StopIteration:
        break
```

Output:

```
1
2
3
```

---
