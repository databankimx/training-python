## C-Like Placeholders and the String-Modulo Operator

Drawing from languages like C and C++, there is a long tradition of using
placeholders composed of a percent sign `%` and a single character 
representing the data type for which it is holding a place in a string
template and then incorporating the values.

In early versions of Python, these were the primary means of incorporating
variable values into a string. The mechanism is still supported in Python 3,
but newer methods are preferred, as the following lessons show.

---

### The Placeholders

Here is a list of supported placeholders:

|Placeholder|Meaning||Placeholder|Meaning|
|:-:|-|-|:-:|-|
|`%d`|`int` (decimal)||`%i`|`int` (decimal)|
|`%o`|`int` (octal)||`%%`|a literal `%` sign|
|`%x`|`int` (hexadecimal: lower)||`%X`|`int` (hexadecimal: UPPER)|
|`%e`|`float` (sci.notation with `e`)||`%E`|`float` (sci.notation with `E`)|
|`%f`|`float` (decimal)||`%F`|`float` (decimal)|
|`%g`|`float` (general)||`%G`|`float` (general)|
|`%r`|`str` (as `repr()`)||`%s`|`str` (as `str()`)|
|`%a`|`str` (as `ascii()`)||||

---

### The String-Modulo Operator

The mechanism for substituting values for the placeholders is the string-modulo
operator `%`, whose syntax looks like this:

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

A single value should still be wrapped in a tuple, as in `("World",)`. The
operator reads the right-hand side as a tuple, so a bare value can be
misinterpreted, especially if the value is itself a tuple.

---

### Multiple Placeholders

You can include multiple placeholders (of varying types), as long as each maps
to a value in the tuple.

And on floating-point numbers, you can even specify the number of decimal 
places with `%.<n>f`, where `<n>` is the number of places. The placeholder
`%.2f` shows two decimal places.

```python
item, qty, price = "bananas", 10, 0.39
template = "%d %s cost $%.2f"
values = (qty, item, price * qty)
print(template % values)
```

Output:

```
10 bananas cost $3.90
```

---

The [`.format()` method](./02_string_format.md) and [f-strings](./08_f_strings.md)
cover the newer approaches, which you'll see more often in current code.

---
