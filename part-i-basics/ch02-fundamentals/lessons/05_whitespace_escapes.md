## Ch 2 - Lesson 5: Whitespace Escape Characters

Sometimes there is a need to include characters in a string that are
otherwise used by the programming language or that cannot easily be
typed in the string itself.

Like most languages, Python provides a collection of *escape characters*,
which, when preceded by a backslash `\` will be replaced with the character
they are escaping in the resulting string.

---

### Python Supported String Escapes

| | |
|-|-|
| \t | tab |
| \n | newline |
| \r | carriage return |
| \\" | double-quote |
| \\\\ | backslash |
| \\' | single-quote |
| \b | backspace |
| \f | form-feed |
| \ooo | octal value (e.g.: \o777) |
| \xhh | hex value (e.g.: \xFFFF) |
| | |

---

### Code Examples:

```python
# Normal string
print("This is a normal string")

# Tab character
print("\tThis string is tab-indented")

# Normal string
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
