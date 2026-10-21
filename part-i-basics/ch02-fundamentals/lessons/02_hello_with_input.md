## "Hello `name`" with User Input

### Get input from the user

Python can ask the user for text with the `input()` function:

```python
name = input("Please enter your name: ")
```

Whatever the user types comes back as a string, even if it looks like a number.
If they type `42`, you get the text `"42"`, not the number 42. We'll deal with
turning text into numbers in Chapter 7, so for now, keep your input as text.

---

### Add the input to a greeting

There are several ways to build a string that includes user input. Nobody's
favorite, but you'll see all of them in the wild.

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

Plus signs glue strings together. It works fine, right up until you forget a
space or try to add a number. Then it doesn't.

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

`print()` adds a space between the things you hand it, so you don't have to.

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

The `{0}` is a placeholder. The `format()` method fills it with the first value
you pass in. Older code uses this a lot, so it's worth recognizing.

---

#### Using f-strings (Python 3.6+)

f-strings make formatted strings much easier to read. If you've used string
interpolation in another language, this is Python's version of it.

```python
name = input("Please enter your name: ")
print(f"Hello {name}")
```

Output:

```
Hello John
```

Put the `f` in front of the quotes, and any variable in braces gets swapped for
its value. This is the form you'll use most from here on.

> **Digging Deeper:**
>
> f-strings and `format()` both build a string, but they work differently. An
> f-string is filled in right where it's written. `format()` works on a template
> string, so you can store the template and fill it in later, perhaps several
> times with different values. That's handy when the same message gets reused,
> and it's why you'll sometimes see templates saved in variables.

---


