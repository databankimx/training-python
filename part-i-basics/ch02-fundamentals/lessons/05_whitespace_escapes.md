## Whitespace Escape Characters

Sometimes you need a character in a string that Python would otherwise read as
part of the code, or one you can't easily type. A tab, for example, or a line
break in the middle of a sentence.

Python handles these with *escape characters*. You write a backslash (`\`)
followed by a letter or number, and Python swaps the pair for the character it
stands for when the string is created.

---

### Python Supported String Escapes

| Escape | What it gives you |
|-|-|
| `\t` | tab |
| `\n` | newline |
| `\r` | carriage return |
| `\"` | double quote |
| `\'` | single quote |
| `\\` | backslash |
| `\b` | backspace |
| `\f` | form feed |
| `\ooo` | a character from its octal code, such as `\101` for `A` |
| `\xhh` | a character from its two-digit hex code, such as `\x41` for `A` |
| `\uxxxx` | a character from its four-digit hex code, such as `\u00e9` for é |

You don't need to memorize this table. Most people use `\n`, `\t`, `\"`, and
`\\` for years and never touch the rest. Keep the table handy for the odd day
you need it.

---

### Code Examples:

```python
# Normal string
print("This is a normal string")

# Tab character
print("\tThis string is tab-indented")

# Newline
print("This string contains a\nline break")
```

Output:

```
This is a normal string
        This string is tab-indented
This string contains a
line break
```

---

### Escaping the Backslash

Because the backslash starts an escape, a literal backslash needs an escape of
its own. Type one backslash, and Python thinks you're starting a sequence:

```python
print("C:\\Users\\scott")
```

Output:

```
C:\Users\scott
```

If you forget and write `"C:\Users\scott"`, Python reads `\U` as the start of a
Unicode escape. That escape expects eight hex digits, and `sers` isn't one, so
Python stops with an error.

---

### Raw Strings for Windows Paths

Windows uses backslashes in file paths, which makes escaping a pain. Put an `r`
in front of the quotes, and Python leaves the backslashes alone:

```python
path = r"C:\new\folder\report.txt"
print(path)
```

Output:

```
C:\new\folder\report.txt
```

Without the `r`, that path gets chewed up. `\n` becomes a line break, `\f`
becomes a form feed, and `\r` becomes a carriage return. You'd get a mess, not
a folder. Raw strings are the easy fix for paths, and they're what
you'll see in most Windows code.

One catch: a raw string can't end with a single backslash, because the closing
quote would be escaped. If you need that, use a regular string with `\\`.

---

