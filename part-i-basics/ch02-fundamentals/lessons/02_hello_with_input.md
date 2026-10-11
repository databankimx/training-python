## Ch 2 - Lesson 2: "Hello `name`" with User Input

### Get input from the user

Python allows you to accept text entered by the user via the `input()`
function:

```python
name = input("Please enter your name: ")
```

---

### Add the input to a greeting

There are several ways to construct a string including user input.

For each example below, assume the user entered `John` as the name.

#### Concatenate strings using the `+` operator

```python
name = input("Please enter your name: ")
print("Hello " + name)
```

Output:

```
Hello John
```

---

#### Print multiple strings using `,` in `print()`

```python
name = input("Please enter your name: ")
print("Hello", name)
```

Output:

```
Hello John
```

---

#### Using the `format()` function

```python
name = input("Please enter your name: ")
print("Hello {0}".format(name))
```

Output:

```
Hello John
```

---

#### Using f-strings (Python 3.6+)

f-strings make formatted strings much more readable. You can think of them
as Python's equivalent of string interpolation in other languages.

```python
name = input("Please enter your name: ")
print(f"Hello {name}")
```

Output:

```
Hello John
```

> **Digging Deeper:**
>
> In some scenarios you may want to use `format()` instead of an f-string.
> f-strings are evaluated immediately when the line is reached, while
> `format()` is not evaluated until it is called. This can matter when a
> formatted string is only used conditionally.

---
