## Python Formatted Literals (f-strings)

The most recent major enhancement to string formatting, as of this writing, is
formatted literals (or *f-strings*), added in Python 3.6.

Often referred to as *string interpolation* (or variable substitution/
expansion), f-strings allow us to place variable names and/or expressions
directly in curly braces in a string, replacing the necessity of placeholders.

If we compare the different eras of string formatting, it's easy to see that
f-strings result in more easily readable code.

Consider these three identical formatted strings:

```python
item, qty, price = "bananas", 5, 0.39
total = round(price * qty, 2)

# string-modulo operator
s = "%d %s cost $%.2f" % (qty, item, total)

# `string.format()` function
s = "{} {} cost ${}".format(qty, item, total)

# f-string
s = f"{qty} {item} cost ${total}"
```

In each case the result value in `s` is:

```
5 bananas cost $1.95
```

But with the inline variable names, the f-string is far and away the easiest 
to understand.

> Note: Python 3.14 added template strings (`t"..."`), which are a related but
> separate feature. They produce a template object that can be processed before it's
> turned into a string, rather than a finished string.

---

### Technical Note: Evaluation Timing

An f-string is filled in as soon as the line that contains it runs. Its value is
fixed at that point, and the expressions inside the braces are evaluated then:

```python
name = "Scott"
greeting = f"Hello, {name}!"
name = "Saul"
print(greeting)
```

Output:

```
Hello, Scott!
```

Changing `name` afterward doesn't change `greeting`, because the f-string was
already filled in.

A `.format()` call works the same way when you call it right away, but you can
store the template itself and fill it in later:

```python
template = "Hello, {}!"
name = "Scott"
print(template.format(name))
name = "Saul"
print(template.format(name))
```

Output:

```
Hello, Scott!
Hello, Saul!
```

The template is only a plain string until `.format()` is called, so one template
can be reused with different values. An f-string can't be reused that way, since
it's filled in where it's written. That's a design difference, not a speed
difference, and both methods fill in the string when the line runs.

---

### Simple Example

Here's a simple example

```python
name = "World"
f_string = f"Hello, {name}!\n"
print(f_string)
```

Output:

```
Hello, World!

```

---

### Multiple Variables

Here's an example with multiple variables

```python
item, qty, price = "bananas", 5, 0.39
total = round(price * qty, 2)
f_string = f"{qty} {item} cost ${total}\n"
print(f_string)
```

Output:

```
5 bananas cost $1.95

```

---

### Converting Dates

Like string formatting, f-strings support using the conversion operator to
specify the `str()` or `repr()` string...

```python
from datetime import datetime

now = datetime.now()
print(f"{now!s}")
print(f"{now!r}\n")
```

Output:

```
2024-08-18 12:22:23.902714
datetime.datetime(2024, 8, 18, 12, 22, 23, 902714)

```

---

### Escaping Non-ASCII Characters

... or the `ascii()` string for that matter.

```python
invalid_string = "Thisö stringö hadö invalidö charactersö."
print(f"{invalid_string!a}")
```

Output:

```
'This\xf6 string\xf6 had\xf6 invalid\xf6 characters\xf6.'
```

---
