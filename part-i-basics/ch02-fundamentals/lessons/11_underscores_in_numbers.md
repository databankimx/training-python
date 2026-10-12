## Underscores as Number Grouping Symbols

In any numerical value, you can include underscores (which are ignored by 
the Python interpreter).

They can appear anywhere in the number (except the beginning and end, which
must be digits), but are most frequently used where commas would appear for 
grouping.

e.g.:     `1000` = `1_000` = `10_00`, etc.

Recalling that integers in Python have no max value, grouping with underscores
can be very useful in making sure that numbers are readable.

---

Code example:

Code like this ...

```python
thousand = 1_000
million  = 1_000_000
billion  = 1_000_000_000
trillion = 1_000_000_000_000
# ...
```

... is much more readable than code like this ...

```python
thousand = 1000
million  = 1000000
billion  = 1000000000
trillion = 1000000000000
# ...
```

---
