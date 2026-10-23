## Examples of String Literals

In Python, a string (a series of characters) can be wrapped in double quotes
(`"`) or single quotes (`'`).

Some languages treat the two differently. Python doesn't. Use whichever you
like, as long as you're consistent within a single string.

---

### You can enclose a `"string"` in double-quotes

```python
message = "This is a string"
print(message)
```

---

### You can also enclose a `'string'` in single-quotes

```python
message = 'This is also a string'
print(message)
```

---

### Including double-quotes in your strings

When you wrap a string in single quotes, double quotes inside it are just
characters. Python doesn't mind.

```python
message = 'I told my friend, "Python is my favorite language!"'
print(message)
```

---

Wrap the string in double quotes instead, and a double quote inside it would
end the string early. To keep it, put a backslash in front of it. That's an
*escape sequence*, and it tells Python, "This quote is part of the text, not
the end of it."

```python
message = "I told my friend, \"Python is my favorite language!\""
print(message)
```

---

### Including single-quotes in your strings

The same rule works the other way around. Wrap a string in double quotes, and
single quotes inside it are just characters.

```python
message = "The language 'Python' is named after Monty Python, not the snake."
print(message)
```

---

Single quotes inside single quotes need the same treatment: a backslash in
front of each one.

```python
message = 'The language \'Python\' is named after Monty Python, not the snake.'
print(message)
```

---

### Avoiding Syntax Errors

Leave an unescaped quote of the same kind inside a string, and you get a syntax
error. Consider this code:

```python
message = 'One of Python's strengths is its diverse community'
print(message)
```

> Note: VS Code will help you out here. Look at the code above. The syntax
> highlighting colors much of the text as if it were Python, and the `print()`
> call as if it were part of a string.
>
> Any time you see that, you probably have a mismatched quote somewhere.

Here's what Python sees. The string starts at the first single quote and ends
at the apostrophe in `Python's`. Python then tries to read `s strengths is its
diverse community'` as code. It can't, so it stops with a `SyntaxError`:

```
File "...\string_error.py", line 1
    message = 'One of Python's strengths is its diverse community'
                                                                 ^
SyntaxError: unterminated string literal (detected at line 1)
```

There are two ways out. You can wrap the string in double quotes...

```python
message = "One of Python's strengths is its diverse community"
```

... or you can escape the apostrophe.

```python
message = 'One of Python\'s strengths is its diverse community'
```

Either works. Pick the one that makes the code easier to read.

---
