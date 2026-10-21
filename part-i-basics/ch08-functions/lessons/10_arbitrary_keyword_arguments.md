## Passing an Arbitrary Number of Keyword Arguments

Just as Python lets you pass an arbitrary number of positional arguments, it lets you pass an arbitrary
number of keyword arguments.

To set this up, put two asterisks in front of one of the function's parameters:

```python
def my_function(**kwargs):
    # Function code
```

You can place any number of standard positional parameters before the keyword parameter, and optionally
an arbitrary positional parameter as well. As with arbitrary positional arguments, only the last
parameter can collect arbitrary keyword arguments.

```python
def my_function(arg1, arg2, ..., *args, **kwargs):
    # Function code
```

The function receives arbitrary keyword arguments as a dictionary.

---

### A Function that Accepts Arbitrary Keyword Arguments

Here, we pass two positional arguments and two keyword arguments. The function collects the keyword
arguments into a dictionary.

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

### Bonus: Reversing the Arbitrary Keyword Idea

Consider a function that takes three arguments:

```python
def sum_up(x, y, z):
    """Calculate the sum of three numbers."""
    print(f"{x} + {y} + {z} = {x + y + z}")
```

#### Wrong Number of Arguments: TypeError

Suppose you have a dictionary that holds two of the values, keyed by parameter name:

```python
values = {"y": 3, "z": 4}
```

If you pass the dictionary as a single argument, Python treats it as the first value, `x`, and
`z` has nothing to receive it:

```python
sum_up(2, values)
```

Output (sample output; the file name and line number depend on your program):

```
Traceback (most recent call last):
  File "...\10_arbitrary_keyword_arguments.py", line 19, in <module>
    sum_up(2, values)
TypeError: sum_up() missing 1 required positional argument: 'z'
```

---

#### Splitting Out the Key-Value Pairs

When you put two asterisks in front of a dictionary in a function call, Python splits it into its
key-value pairs and passes each pair as a keyword argument.

The two uses of the asterisks are related. In a function definition, `**param` gathers keyword arguments
into a single dictionary. In a function call, `**arg` takes a single dictionary and splits it into
separate keyword arguments.

So this pattern works:

```python
sum_up(2, **values)
```

The `2` goes to the positional parameter `x`, and the dictionary supplies `y` and `z` as keyword
arguments.

Output:

```
2 + 3 + 4 = 9
```

> **About the `.py` file:** the `TypeError` line is commented out, so the file runs to the end. Uncomment
> it to see the error.

---

