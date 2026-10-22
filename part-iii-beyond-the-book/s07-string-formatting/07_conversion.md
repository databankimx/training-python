## The Conversion Flag `!`

A conversion flag, written as an exclamation mark `!` in a placeholder, changes
how a value is converted to a string before it's inserted. Python accepts three
conversion flags:

|Flag|Conversion|
|:-:|-|
|`!s`|`str()`, the same as no conversion|
|`!r`|`repr()`|
|`!a`|`ascii()`|

Other letters don't work after `!`. Trying one raises an error:

```python
print("{!d}".format(42))
```

Output:

```
ValueError: Unknown conversion specifier d
```

The type letters from the string-modulo operator, such as `d`, `f`, and `x`,
belong after a colon instead. These are format specifiers, covered in the
[format specifiers lesson](./09_format_specifiers.md) and the
[data types lesson](./10_type_specifiers.md):

```python
print("{:x}".format(255))
```

Output:

```
ff
```

---

### Converting Dates

Here is an example where we can look at the difference between the `str()` and
`repr()` representations of a date value:

```python
from datetime import datetime

now = datetime.now()
print("{!s}".format(now))
print("{!r}".format(now))
```

Output:

```
2024-08-18 12:00:07.141226
datetime.datetime(2024, 8, 18, 12, 0, 7, 141226)
```

The timestamp will be different each time you run it.

Note: If we did not specify a conversion, we would get the same output as 
`!s`.

> Note: the code file turns off a Pylint warning (`consider-using-f-string`) on
> these `print` lines. Those comments stay in the code file.

---

### Escaping Non-ASCII Characters

A common issue for programmers is encountering characters that are not in the
current character set while parsing text.

Using the `ascii()` representation of the string, we can escape non-ASCII 
characters into their hexadecimal forms:

```python
invalid_string = "Thisö stringö haö invalidö charactersö."
print("{!a}".format(invalid_string))
```

Output:

```
'This\xf6 string\xf6 ha\xf6 invalid\xf6 characters\xf6.'
```

---
