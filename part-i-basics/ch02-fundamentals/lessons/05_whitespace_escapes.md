## Ch 2 - Lesson 5: Whitespace Escape Characters

Sometimes there is a need to include characters in a string that are
otherwise used by the programming language or that cannot easily be typed.

Like most languages, Python provides *escape characters* - when preceded by a
backslash `\`, they are replaced with the character they represent in the
resulting string.

---

### Python Supported String Escapes

| Escape | Meaning |
|-|-|
| `\t` | tab |
| `\n` | newline |
| `\r` | carriage return |
| `\"` | double-quote |
| `\\` | backslash |
| `\'` | single-quote |
| `\b` | backspace |
| `\f` | form-feed |
| `\ooo` | octal value (e.g. `\o777`) |
| `\xhh` | hex value (e.g. `\xFFFF`) |

---

### Code Examples

```python
print("Normal")
print("---")

print("\tTabbed")
print("---")

print("Line\nbreak")
print("---")

print("\"double\" quotes")
print("---")

print('\'single\' quotes')
```

Output:

```
Normal
---
        Tabbed
---
Line
break
---
"double" quotes
---
'single' quotes
```

---
