## Removing String Prefixes/Suffixes

The 3rd edition textbook introduces two additional string manipulation 
functions.

Both were added in Python 3.9.

---

### Remove a Prefix

The `removeprefix()` function allows you to remove specified characters at 
the beginning of a string.

Note: This does not modify the existing string.

```python
no_starch_url = "https://nostarch.com"
# Remove the protocol from the beginning of a URL
print(no_starch_url.removeprefix("https://"))
```

Output:

```
nostarch.com
```

---

### Remove a Suffix

The `removesuffix()` function allows you to remove specified characters at 
the end of a string.

Note: This does not modify the existing string.

```python
no_starch_url = "https://nostarch.com"
# Remove the protocol from the beginning of a URL
print("No Starch protocol:", no_starch_url.removesuffix("://nostarch.com"))
```

Output:

```
No Starch protocol: https
```

---
