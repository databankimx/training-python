## Removing String Prefixes and Suffixes

Python 3.9 added two methods for trimming text from the ends of a string:
`removeprefix()` and `removesuffix()`. Each one removes a piece of text from
one end, and each one returns a new string. Like the case and strip methods, the
original stays exactly as it was.

At first glance, they seem a little pointless. The older `lstrip()` and
`rstrip()` already trim the ends of a string. So why bother?

Because `lstrip()` and `rstrip()` don't take a piece of text. They take a *set
of characters*, and they remove any of those characters from that end until they
hit one that isn't in the set. That's easy to get wrong:

```python
print("pepper".lstrip("pep"))  # r
```

`lstrip("pep")` removed every `p` and `e` it found from the left, and stopped at
the `r`. You probably wanted `per`. Many editors will underline that call, and
the underline is fair. The argument looks like a prefix, but `lstrip()` treats it
as a set of characters. `removeprefix()` does what it says:

```python
print("pepper".removeprefix("pep"))  # per
```

It removes the exact text `pep` once. If the prefix isn't there, the string comes
back unchanged. `removesuffix()` does the same job at the end of a string.

---

### Remove a Prefix

The `removeprefix()` method removes the given text from the beginning of a
string, if it's there.

```python
no_starch_url = "https://nostarch.com"
# Remove the protocol from the beginning of the URL
print(no_starch_url.removeprefix("https://"))
```

Output:

```
nostarch.com
```

---

### Remove a Suffix

The `removesuffix()` method removes the given text from the end of a string, if
it's there.

```python
no_starch_url = "https://nostarch.com"
# Remove the domain from the end of the URL
print("No Starch protocol:", no_starch_url.removesuffix("://nostarch.com"))
```

Output:

```
No Starch protocol: https
```

A filename is another good fit. Strip the extension, and keep the name:

```python
filename = "report.txt"
print(filename.removesuffix(".txt"))
```

Output:

```
report
```

---

Like the other string methods, both of these leave the original string alone.
Save the result in a variable if you want to keep it.

---
