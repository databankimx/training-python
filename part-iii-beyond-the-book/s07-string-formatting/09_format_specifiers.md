## Format Specifiers

Within a curly-brace placeholder or expansion, there also exists a robust
sub-language of format specifiers.

These can be appended to a replacement field (following a colon `:`) to 
provide secondary formatting.

The syntax is as follows:

`:[[<fill>]<align>][<sign>][#][0][<width>][<group>][.<precision>][<type>]`

That looks insane!

But don't worry. That layout is just specifying the order in which you add 
the various optional format specifiers.

|Sub-Component|Effect|
|:-:|-|
|`:`|Separates the \<format_spec> from the rest of the replacement field|
|fill|Specifies a character to pad values that don't fill the field width|
|align|Specifies the justification of values that don't fill the field width|
|sign|Controls whether a leading sign is included for numeric values|
|`#`|Selects an alternate output form for certain presentation types|
|`0`|Pads with with zeros instead of ASCII space characters|
|width|Specifies the minimum width of the output|
|group|Specifies a grouping character for numeric output|
|.precision|Specifies number of decimal places for floating-point &<br>maximum width for string output|
|type|Specifies the conversion type|

---

### For Example

These can be used with any of the formatting methodologies we've seen 
previously.

This prints out `pi` to two decimal places, padded on the left with zeros out
to a total of 6 characters:

```python
pi = 3.14159
print("%06.2f" % pi)            # string-modulo
print("{:06.2f}".format(pi))    # string.format()
print(f"{pi:06.2f}")            # f-string
```

Output:

```
003.14
003.14
003.14
```

For the remainder of the lessons in this topic, I will use f-strings. But, as
you can see, the format specifiers use the same syntax for any formatting
mechanism.

---
