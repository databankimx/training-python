## Ch 2 - Lesson 6: Stripping Excess Whitespace

Often data (especially from older systems) can be stored as fixed-length
blocks of text. Because of this, strings you work with may often contain
excess whitespace at the beginning (leading whitespace) or end (trailing 
whitespace) or both.

Python provides a set of simple functions to remove excess whitespace from
strings.

---

### Remove Leading Whitespace

To remove leading whitespace, use the `lstrip()` (left strip) function

```python
favorite_language = "    Python    "
print(f"[{favorite_language.lstrip()}]")
```

Output:

```
[Python    ]
```

---

To remove trailing whitespace, use the `rstrip()` (right strip) function

```python
favorite_language = "    Python    "
print(f"[{favorite_language.rstrip()}]")
```

Output:

```
[    Python]
```

---

To remove both leading and trailing whitespace, use the `strip()` function

```python
favorite_language = "    Python    "
print(f"[{favorite_language.strip()}]")
```

Output:

```
[Python]
```

---
