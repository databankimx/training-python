## Bonus Lesson: Using `iter()`

Iteration is at the heart of processing collections of data. So far, we've used loops to iterate.
Sometimes you need more direct, step-by-step control over iteration. For that, Python provides the
`iter()` function, which returns an *iterator* object. An iterator has a `next()` function that
produces the next item.

A `for` loop calls `iter()` for you behind the scenes. Calling `iter()` yourself gives you control over
each step:

* Lazy evaluation: an iterator produces values only when you ask for them. That's useful for very large
  or endless sequences, and for files, where you don't want to load everything into memory at once.
* Granular control: you decide when each iteration happens, and when to stop.

---

### TypeError with `iter()`

The `iter()` function raises a `TypeError` if you pass it something that isn't iterable.

```python
iter(None)
```

Output:

```
Traceback (most recent call last):
  File "...\iter_none.py", line 1, in <module>
    iter(None)
    ^^^^^^^^^^
TypeError: 'NoneType' object is not iterable
```

---

### Checking if a Variable is Iterable

To avoid that error, check whether a variable is iterable first. A `try`/`except` block does the job:

```python
def is_iterable(obj):
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
`NoneType` is not iterable.
```

Now we can tell whether an object is iterable, and create an iterator from it. Next, we need to call
`next()` to perform the iterations.

---

### The `StopIteration` Error

Calling `next()` in a loop without checking whether the iterator has more items causes a problem:

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
  File "...\stop_iteration.py", line 6, in <module>
    print(next(iter_obj))
          ^^^^^^^^^^^^^^
StopIteration
```

Once an iterator runs out, calling `next()` raises a `StopIteration` error.

---

### Fixing the `StopIteration` Problem

You could use a `for` loop or a counter to limit the number of iterations. That works fine for a `list`
or a `tuple`. But for something like a text file (type: `TextIOWrapper`), the iterator loads lazily, so
you can't know in advance how many iterations there will be.

The fix is another `try`/`except` block, this time around the `next()` call:

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

> **About the `.py` file:** it includes `show_iteration()`, a helper that prints a collection and any
> collections nested inside it. It uses recursion, a function that calls itself, which is covered in
> Chapter 8. Read it for now as a preview of what iterators can do.

---

