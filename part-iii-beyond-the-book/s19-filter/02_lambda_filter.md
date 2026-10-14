## Using a Lambda Function as a Filter

In the previous lesson, we wrote a named function to decide which values to
keep. For a short, simple condition, we can pass a lambda to `filter()`
instead. The code for this lesson is in
[02_lambda_filter.py](./02_lambda_filter.py).

---

### Filtering Numbers

Here is a lambda that keeps only the even numbers:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda n: not n % 2, numbers))
print(f"Even numbers: {evens}")
```

Output:

```
Even numbers: [2, 4, 6, 8, 10]
```

The lambda takes one value and returns `True` or `False`. `filter()` calls it
for each item and keeps the items where the result is `True`. The `list()`
call turns the result into a list, because `filter()` returns an iterator.

---

### Filtering Strings

The same pattern works for any condition. Here we keep only the words that are
longer than four letters:

```python
words = ["fig", "apple", "kiwi", "banana"]
long_words = list(filter(lambda w: len(w) > 4, words))
print(f"Words longer than 4 letters: {long_words}")
```

Output:

```
Words longer than 4 letters: ['apple', 'banana']
```

---

### Using `None` as the Filter

If you pass `None` instead of a function, `filter()` keeps the items that are
true when Python evaluates them. Values such as `0`, `""`, and `None` are false:

```python
truthy = list(filter(None, [0, 1, "", "a", None, 2]))
print(f"Values that are true: {truthy}")
```

Output:

```
Values that are true: [1, 'a', 2]
```

---

### When to Use a Lambda

A lambda is a good choice when the condition is short and used only once. If
the condition is long, or you need it in more than one place, a named function
is easier to read and test, as we saw in the previous lesson.

---

### Try It

Use a lambda to keep only the numbers from 1 to 20 that are divisible by 3.
Check your result by printing it in a Python shell.

---
