## Returning Values from Functions

You can make a function pass a value back to the calling code using the 
`return` keyword.

In many languages, a function without a `return` will behave as a statement
(it will not resolve to any value). In Python, however, all functions are
expressions (they resolve to some value). If you do not specify a `return` in
your code, then the function returns `None`.

Syntax:  
`return value_to_pass_back`

Making sure that your functions return values can add versatility to your code.

---

### Returning a Value

Unlike some languages, in Python, you do not have to declare a return type in 
the function signature.

All you do is add a `return` statement.

Since a value is returned, you can capture the function results in a variable.

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

Here's a way to refine the example from above to make the middle name optional.

This makes the function more versatile, since we don't need separate functions
for with and without middle names.

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
