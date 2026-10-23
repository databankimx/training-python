## `any()` and `all()`

`any()` and `all()` each take an iterable and return a single `True` or `False`:

* `any(items)` is `True` if at least one item is true.
* `all(items)` is `True` only if every item is true.

The code for this lesson is in [the_any_and_all.py](./the_any_and_all.py):

```python
scores = [88, 92, 75]
print(any(score > 90 for score in scores))
print(all(score > 80 for score in scores))
```

---

### Testing a Condition Across a Collection

The argument to `any()` and `all()` is often a generator expression, which tests
each item and yields `True` or `False` for it:

```python
scores = [88, 92, 75]
print(any(score > 90 for score in scores))
print(all(score > 80 for score in scores))
```

Output:

```
True
False
```

`any()` is `True` because 92 is above 90. `all()` is `False` because 75 is not
above 80.

These two functions read more clearly than a loop with a flag variable, so you'll
see them often in conditions.

---

### Empty Collections

An empty collection has no items to fail, so `all()` is `True` for it. It has no
items to succeed, so `any()` is `False`:

```python
print(any([]))
print(all([]))
```

Output:

```
False
True
```

This surprises many people, so keep it in mind when a list might be empty.

---

### Short-Circuiting

Both functions stop as soon as the answer is known. `any()` stops at the first true
item, and `all()` stops at the first false item. Later items are never checked:

```python
def loud(value: int) -> bool:
    """Report that a value was checked, then test it"""
    print("checking", value)
    return value > 10

print(any(loud(n) for n in [5, 20, 30]))
```

Output:

```
checking 5
checking 20
True
```

The value 30 is never checked, because 20 already made `any()` return `True`.
This also means the generator is only run as far as it needs to be.

---

### Try It

Use `all()` to check whether every name in a list starts with a capital letter.
Then change one name to lowercase and predict the result before you run the code.

---
