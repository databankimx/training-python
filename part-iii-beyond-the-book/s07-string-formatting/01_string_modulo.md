## C-Like Placeholders and the String-Modulo Operator

Drawing from languages like C and C++, there is a long tradition of using
placeholders composed of a percent sign `%` and a single character 
representing the data type for which it is holding a place in a string |
template and then incorporating the values.

In early versions of Python, these were the primary means of incorporating
variable values into string.

---

### The Placeholders

Here is a list of supported placeholders:

|Placeholder|Meaning||Placeholder|Meaning|
|:-:|-|-|:-:|-|
|`%d`|`int` (decimal)||`%i`|`int` (decimal)|
|`%o`|`int` (octal)||`%%`|`%` sign if no value|
|`%x`|`int` (hexadecimal: lower)||`%X`|`int` (hexadecimal: UPPER)|
|`%e`|`float` (sci.notation with `e`)||`%E`|`float` (sci.notation with `E`)|
|`%f`|`float` (decimal)||`%F`|`float` (decimal)|
|`%g`|`float` (general)||`%G`|`float` (general)|
|`%r`|`str` (as `repr()`)||`%s`|`str` (as `str()`)|
|`%a`|`str` (as `ascii()`)||||

---

### The String-Modulo Operator

In Python (prior to v2.6), the mechanism for substituting values for the
placeholders was the string-modulo operator `%`, whose syntax looked like 
this:

```python
template = "string containing placeholders"
values = (tuple, containing, values)
string = template % values
```

---

### Simple Example

A simple example of this is a template containing a single placeholder.

Here, we have a template containing a placeholder for a string, and a tuple 
containing a single string value.

```python
template = "Hello, %s!"
values = ("World",)
print(template % values)
```

Output:

```
Hello, World!
```

---

### Multiple Placeholders

You can include multiple placeholders (of varying types), as long as each maps
to a value in the tuple.

And on floating-point numbers, you can even specify the number of decimal 
places using `.000f` where `000` is the number of decimal places.

```python
item, qty, price = "bananas", 10, 0.39
template = "%d %s cost $%.2f"
values = (qty, item, price * qty)
print(template % values)
```

Output:

```
6 bananas cost $3.90
```

---
