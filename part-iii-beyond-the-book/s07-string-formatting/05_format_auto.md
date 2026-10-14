## String `.format()` Using Auto (Ordered) Matching

You can also forego both indices and keywords and use empty curly brace pairs.
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
total = qty * price
template = "{} {} cost ${}"
values = (qty, item, total)
print(template.format(*values))
```

or

```python
qty, item, price = 5, "bananas", 0.39
total = qty * price
print("{} {} cost ${}".format(qty, item, total))
```

Output:

```
5 bananas cost $1.95
```

---
