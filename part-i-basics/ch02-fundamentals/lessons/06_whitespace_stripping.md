## Stripping Excess Whitespace

Data often arrives with extra space stuck to it. Older systems are the worst
offenders. They store everything in fixed-length fields, so a name that's four
letters long sits in a field sized for twenty, with sixteen spaces of padding.
The data is technically correct, and practically annoying.

Python gives you a few simple functions to clean that up.

> **What counts as whitespace?** More than you'd think. Spaces, tabs, and
> newlines all count. A line read from a file usually ends with a newline, and
> the stripping functions will quietly remove it for you.

---

> **Why the brackets?** Every example below wraps its result in square brackets,
> on purpose. Spaces are invisible, so without the brackets you couldn't tell
> what was removed. With them, you can see exactly where each string starts and
> ends, and the spaces that survive are easy to spot.

### Remove Leading Whitespace

Leading whitespace is the stuff at the start of a string. To remove it, use
`lstrip()`, which stands for "left strip."

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

Trailing whitespace is the stuff at the end. To remove it, use `rstrip()`,
or "right strip."

```python
favorite_language = "    Python    "
print(f"[{favorite_language.rstrip()}]")
```

Output:

```
[    Python]
```

---

### Remove Both Ends

When you want both gone, use `strip()` by itself.

```python
favorite_language = "    Python    "
print(f"[{favorite_language.strip()}]")
```

Output:

```
[Python]
```

---

### Only the Ends Get Trimmed

These functions only work on the ends of the string. Any whitespace in the middle
stays exactly where it is:

```python
message = "    Hello   World    "
print(f"[{message.strip()}]")
```

Output:

```
[Hello   World]
```

Three spaces between the words? Still there. `strip()` is a tidy-up at the
edges, not a general cleaning service.

---

### Keep the Result

Like the case methods in the last lesson, these return a new string. The original
stays as it was, so save the result if you want to keep it:

```python
favorite_language = "    Python    "
cleaned = favorite_language.strip()
print(f"[{cleaned}]")
```

Output:

```
[Python]
```

---

