## Passing an Arbitrary Amount of Arguments

Python allows you to define a function that takes an arbitrary amount of 
arguments.

To implement this pattern, you declare one of the function's parameters with
an asterisk:

```python
def my_function(*args):
    # Function code
```

You can declare standard, positional parameters before the arbitrary parameter
but not after, and only one parameter can be declared as arbitrary length.

The function receives the arbitrary arguments as a list.

---

### A Function that Accepts an Arbitrary Number of Arguments

Here, the function accepts any number of arguments as a list of `toppings`.

```python
def make_pizza_simple(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza_simple("pepperoni")
make_pizza_simple("mushrooms", "green peppers", "extra cheese")
```

Output:

```
Making a pizza with the following toppings:
- pepperoni

Making a pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

---

### Passing a List as Arbitrary Arguments

If you have a list to pass as the arbitrary arguments, prepending an asterisk
to it splits the list into its components. For example:

```python
make_pizza_simple(*["mushrooms", "sausage", "black olives"])
```

Output:

```
Making a pizza with the following toppings:
- mushrooms
- sausage
- black olives
```

---

### Positional and Arbitrary Arguments

Here, the function accepts a required positional argument and an arbitrary
number of additional arguments:

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")
```

Output:

```
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

---

### Bonus: The Reverse of Arbitrary Arguments

Consider a function that takes several positional arguments.

```python
def sum_up(x, y, z):
    print(f"{x} + {y} + {z} = {x + y + z}")
```

#### Wrong Number of Arguments : TypeError

If we have a collection of values, we cannot simply pass the collection, even
if it has the correct number of values, since it would only pass the list as
a single argument.

```python
values = [2, 3, 4]
sum_up(values)
```

```
Traceback (most recent call last):
  File "...\09_arbitrary_arguments.py", line 38, in <module>
    sum_up(values)
TypeError: sum_up() missing 2 required positional arguments: 'y' and 'z'
```

---

#### Splitting the Values

When we prepend an asterisk to a list, we're instructing Python to split it
into its component values and pass them.

While `*param` in a function takes a group of separate variables and makes
them a single list, `*arg` in a function call takes a single list and splits it
into separate arguments.

So this pattern works:

```python
values = [2, 3, 4]
sum_up(*values)
```

Output:

```
2 + 3 + 4 = 9
```

---
