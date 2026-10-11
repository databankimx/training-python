## Ch 2 - Lesson 7: Removing String Prefixes and Suffixes

The 3rd edition textbook introduces two additional string manipulation
functions: `removeprefix()` and `removesuffix()`. Both were added in
Python 3.9.

---

### Remove a Prefix

The `removeprefix()` function removes a specified string from the beginning
of a string. It does not modify the original string.

```python
no_starch_url = "https://nostarch.com"
print(no_starch_url.removeprefix("https://"))
```

Output:

```
nostarch.com
```

---

### Remove a Suffix

The `removesuffix()` function removes a specified string from the end of a
string. It does not modify the original string.

```python
no_starch_url = "https://nostarch.com"
print("No Starch protocol:", no_starch_url.removesuffix("://nostarch.com"))
```

Output:

```
No Starch protocol: https
```

---
