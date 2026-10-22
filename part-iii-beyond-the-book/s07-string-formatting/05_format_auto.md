## String `.format()` Using Auto (Ordered) Matching

You can also forgo both indices and keywords and use empty curly brace pairs.
In this pattern, the values passed will be substituted with the placeholders
in the order they appear.

---

### Single Item

Here is an example using a single auto-matched argument:

```python
template = "Hello, {}!"
values = ("World",)
print(template.format(*values))
```

or

```python
"Hello, {}!".format("World")
```

Output:

```
Hello, World!
```

---

### Multiple Arguments

Here is an example using multiple auto-matched arguments:

```python
qty, item, price = 5, "bananas", 0.39
total = round(qty * price, 2)
template = "{} {} cost ${}"
values = (qty, item, total)
print(template.format(*values))
```

or

```python
qty, item, price = 5, "bananas", 0.39
total = round(qty * price, 2)
print("{} {} cost ${}".format(qty, item, total))
```

Output:

```
5 bananas cost $1.95
```

> Note: the code file turns off a Pylint warning (`consider-using-f-string`) on
> these `print` lines. Those comments stay in the code file.

---

### Counting Matters

Automatic matching uses the arguments in order, so the count has to fit the
template. Extra arguments are silently ignored, which can hide a mistake:

```python
print("{}".format(1, 2))
```

Output:

```
1
```

Too few arguments is different. It raises an `IndexError`, so the mistake
shows up immediately. Automatic numbering also can't be mixed with numbered
placeholders such as `{0}`, as the [`.format()` lesson](./02_string_format.md)
showed.

---
