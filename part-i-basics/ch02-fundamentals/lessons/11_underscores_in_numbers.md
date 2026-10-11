## Underscores as Number Grouping Symbols

In any numerical value, you can include underscores which are ignored by
the Python interpreter. They can appear anywhere in the number (except at
the beginning or end), but are most commonly used where commas would
appear for grouping.

e.g.: `1000` = `1_000` = `10_00`, etc.

Since Python integers have no maximum value, grouping with underscores
becomes especially useful for keeping large numbers readable.

---

```python
thousand = 1_000
million  = 1_000_000
billion  = 1_000_000_000
trillion = 1_000_000_000_000
```

... is much more readable than:

```python
thousand = 1000
million  = 1000000
billion  = 1000000000
trillion = 1000000000000
```

---
