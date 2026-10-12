## Passing an Arbitrary Amount of Keyword Arguments

Like positional arguments, Python permits an arbitrary number of keyword
arguments to be passed to a function.

To implement this pattern, you declare one of the function's parameters with
two asterisks:

```python
def my_function(**kwargs):
    # Function code
```

You can precede the arbitrary keyword argument parameter with any number of 
positional arguments and (optionally) an arbitrary positional arguments
parameter. However, like arbitrary positional arguments, only the last 
parameter can be declared for arbitrary keyword arguments.

```python
def my_function(arg1, arg2, ..., *args, **kwargs):
    # Function code
```

Arbitrary keyword arguments are received by the function as a dictionary.

---

### A Function Accepting Arbitrary Keyword Arguments

Here, we are passing two positional arguments and two keyword arguments. The function interprets the keyword arguments as a dictionary.

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)
```

Output:

```
{'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
```

---

### Bonus: Reversing the Arbitrary Keywords Concept

Consider a function that takes several arguments:

```python
def sum_up(x, y, z):
    print(f"{x} + {y} + {z} = {x + y + z}")
```

#### Wrong Number of Arguments : TypeError

If we have a dictionary containing two of the arguments by name, we cannot 
simply pass the collection, even if it has the correct number of values, since 
it would only pass the dictionary as a single argument.

```python
sum_up(2, values)
```

Output:

```
Traceback (most recent call last):
  File "...\10_arbitrary_keyword_arguments.py", line 19, in <module>
    sum_up(2, values)
TypeError: sum_up() missing 1 required positional argument: 'z'
```

---

#### Splitting Out the Key:Value Pairs

When we prepend two asterisks to a dictionary, we're instructing Python to 
split it into its component key:value pairs and pass them as keyword arguments.

While `**param` in a function takes a group of separate variables and makes
them a single dictionary, `**arg` in a function call takes a single dictionary 
and splits it into separate keyword arguments.

So this pattern works:

```python
sum_up(2, **values)
```

The `2` is read into the function as positional argument `x`, and the
dictionary is passed as two keyword arguments: `y` and `z`.

Output:

```
2 + 3 + 4 = 9
```

---
