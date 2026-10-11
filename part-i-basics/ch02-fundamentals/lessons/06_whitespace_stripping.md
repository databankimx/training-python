## Ch 2 - Lesson 6: Stripping Excess Whitespace

Data from older systems is often stored as fixed-length blocks of text,
resulting in strings with excess whitespace at the beginning (leading) or
end (trailing) or both.

Python provides simple functions to remove this excess whitespace.

---

### Remove Leading Whitespace

```python
favorite_language = "    Python    "
print(f"[{favorite_language.lstrip()}]")
```

Output:

```
[Python    ]
```

---

### Remove Trailing Whitespace

```python
favorite_language = "    Python    "
print(f"[{favorite_language.rstrip()}]")
```

Output:

```
[    Python]
```

---

### Remove Both

```python
favorite_language = "    Python    "
print(f"[{favorite_language.strip()}]")
```

Output:

```
[Python]
```

---
