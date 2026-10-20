## String Formatting

Perhaps nothing in programming evolves as quickly as the mechanisms for
formatting strings, and Python is no exception.

Developers are always hunting for straightforward ways to do things like:

* Embed a variable value in a string
* Format a number to a specific number of decimal places
* Align data printed to the screen
* And so on

---

### Evolution of Formatting Methods

Python has gone through a number of evolutions in this regard:

* C-Like Placeholders (`%d`, `%s`, etc.)
* The String-Modulo Operator `<template> % (<values_tuple>)`
* The String `.format()` function
* Interpolated f-strings
* And a Robust Sub-Language of Format Specifiers

---

### Topics

This section covers the following topics:

* [The String-Modulo Operator `%`](./01_string_modulo.md)  
  
* [The `string.format()` Function](./02_string_format.md)
    * [Using Indices](./03_format_indices.md)
    * [Using Keyword Arguments](./04_format_keywords.md)
    * [Automatic - Using Empty Braces](./05_format_auto.md)
    * [Reusing Placeholders](./06_reuse_placeholders.md)
    * [The Conversion Attribute](./07_conversion.md)
* [Formatted Literals (f-strings)](./08_f_strings.md)
* [Format Specifiers](./09_format_specifiers.md)
    * [Data Types](./10_type_specifiers.md)
    * [Digit Grouping](./11_digit_grouping.md)
    * [Decimal Places](./12_decimal_places.md)
    * [Signed Numbers](./13_signs.md)
    * [Width, Fill, and Alignment](./14_width_fill_align.md)
    * [Zero Padding](./15_zero_padding.md)
    * [Nested Formatters](./16_nested_formatters.md)

---
