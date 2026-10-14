## The Conversion Operator `!`

If we recall back to the string-modulo operator topic, we'll recall this 
table:

|Placeholder|Meaning||Placeholder|Meaning|
|:-:|-|-|:-:|-|
|`%d`|`int` (decimal)||`%i`|`int` (decimal)|
|`%o`|`int` (octal)||`%%`|`%` sign if no value|
|||etc. ...|||

Any value that can be used with the `%` operator can be used in conjunction 
with a `string.format()` placeholder to trigger conversion of the value being
substituted to the desired type.

|Placeholder|Meaning||Placeholder|Meaning|
|:-:|-|-|:-:|-|
|`!d`|`int` (decimal)||`!i`|`int` (decimal)|
|`!o`|`int` (octal)||`!%`|`%` sign if no value|
|`!x`|`int` (hexadecimal: lower)||`!X`|`int` (hexadecimal: UPPER)|
|`!e`|`float` (sci.notation with `e`)||`!E`|`float` (sci.notation with `E`)|
|`!f`|`float` (decimal)||`!F`|`float` (decimal)|
|`!g`|`float` (general)||`!G`|`float` (general)|
|`!r`|`str` (as `repr()`)||`!s`|`str` (as `str()`)|
|`!a`|`str` (as `ascii()`)||||

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

Note: If we did not specify a conversion, we would get the same out put as 
`!s`.

---

### Replacing Invalid Characters

A common issue for programmers is encountering characters that are not in the
current character ser while parsing text.

Using the `ascii()` representation of the string, we can replace non-ASCII 
characters with their corresponding hexadecimal values:

```python
invalid_string = "Thisö stringö haö invalidö charactersö."
print("{!a}".format(invalid_string))
```

Output

```
'This\xf6 string\xf6 had\xf6 invalid\xf6 characters\xf6.'
```

---
