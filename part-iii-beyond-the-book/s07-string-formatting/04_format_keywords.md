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

If the keyword doesn't match, you get a `KeyError` instead:

```python
"Hello, {name}!".format(nam="World")
```

Output:

```
KeyError: 'name'
```

---

### Multiple Keywords

Here is an example using multiple keyword arguments:

```python
qty, item, price = 5, "bananas", 0.39
total = round(qty * price, 2)
template = "{num} {name} cost ${price}"
keywords = {"num": qty, "name": item, "price": total}
print(template.format(**keywords))
```

or

```python
qty, item, price = 5, "bananas", 0.39
total = round(qty * price, 2)
print("{num} {name} cost ${price}".format(num=qty, name=item, price=total))
```

Output:

```
5 bananas cost $1.95
```

We round the total to two decimal places, for the same reason as in the indices
lesson: `5 * 0.39` is `1.9500000000000002` in floating point.

> Note: the code file turns off a Pylint warning (`consider-using-f-string`) on
> these `print` lines. Those comments stay in the code file.

---
