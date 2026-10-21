## Returning Values from Functions

A function can pass a value back to the code that called it, using the `return` keyword.

In many languages, a function without a `return` behaves like a statement, so it doesn't produce a
value. In Python, every function call is an expression, so it always produces a value. If your function
doesn't have a `return`, the value it produces is `None`.

Syntax:
`return value_to_pass_back`

Making sure your functions return values adds versatility to your code.

> **About the `.py` file:** it includes a `pause()` helper that waits for you to press Enter between
> the examples, so you can read each result before the next one appears.

---

### Returning a Value

Unlike some languages, Python doesn't require you to declare a return type in the function signature.
All you do is add a `return` statement.

Since the function returns a value, you can store the result in a variable.

```python
def get_formatted_name_simple(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

def get_formatted_name_middle(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_simple("jimi", "hendrix")
print(musician)
musician = get_formatted_name_middle("john", "lee", "hooker")
print(musician)
```

Output:

```
Jimi Hendrix
John Lee Hooker
```

---

### A More Versatile Example

Here's a way to refine the example above so the middle name is optional.

This makes the function more versatile, because you don't need separate functions for names with and
without a middle name.

```python
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)
musician = get_formatted_name("john", "hooker", "lee")
print(musician)
```

Output:

```
Jimi Hendrix
John Lee Hooker
```

---

