## String `.format()` Using Keywords

Much like arbitrary keyword arguments in any function, the main difference
here is that the keyword arguments are treated like a dictionary as opposed to
a tuple.

---

### Single Keyword

Here is an example using a single keyword argument:

```python
template = "Hello, {name}!"
keywords = {"name": "World"}
print(template.format(**keywords))
```

or

```python
"Hello, {name}!".format(name="World")
```

Output:

```
Hello, World!
```

Be careful not to mix this up with f-strings, where a name in curly braces
represents a variable to be interpolated into the string. Here it is the name
of a keyword argument.

---

### Multiple Keywords

Here is an example using multiple keyword arguments:

```python
qty, item, price = 5, "bananas", 0.39
total = qty * price
template = "{num} {name} cost ${price}"
keywords = {"num": qty, "name": item, "price": total}
print(template.format(**keywords))
```

or

```python
qty, item, price = 5, "bananas", 0.39
total = qty * price
print("{num} {name} cost ${price}".format(num=qty, name=item, price=total))
```

Output:

```
5 bananas cost $1.95
```

---
