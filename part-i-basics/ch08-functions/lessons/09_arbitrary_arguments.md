## Passing an Arbitrary Number of Arguments

Python lets you define a function that takes an arbitrary number of arguments.

To set this up, put an asterisk in front of one of the function's parameters:

```python
def my_function(*args):
    # Function code
```

You can declare standard positional parameters before the arbitrary parameter, but not after it. Only
one parameter can be declared as arbitrary length.

The function receives the arbitrary arguments as a tuple.

---

### A Function that Accepts an Arbitrary Number of Arguments

Here, the function accepts any number of arguments as a tuple called `toppings`.

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

If you have a list of values to pass as arbitrary arguments, put an asterisk in front of the list.
That splits the list into its separate values:

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

Here, the function takes a required positional argument, followed by an arbitrary number of additional
arguments:

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

Consider a function that takes three positional arguments:

```python
def sum_up(x, y, z):
    """Sum the provided numbers."""
    print(f"{x} + {y} + {z} = {x + y + z}")
```

#### Wrong Number of Arguments: TypeError

If you have a collection of values, you can't pass the collection itself, even when it holds the right
number of values. Python would treat the whole list as a single argument:

```python
values = [2, 3, 4]
sum_up(values)
```

Output (sample output; the file name and line number depend on your program):

```
Traceback (most recent call last):
  File "...\09_arbitrary_arguments.py", line 38, in <module>
    sum_up(values)
TypeError: sum_up() missing 2 required positional arguments: 'y' and 'z'
```

---

#### Splitting the Values

When you put an asterisk in front of a list in a function call, Python splits the list into its separate
values and passes each one as its own argument.

The two uses of the asterisk are related. In a function definition, `*param` gathers separate arguments
into a single tuple. In a function call, `*arg` takes a single list (or other sequence) and splits it into
separate arguments.

So this pattern works:

```python
values = [2, 3, 4]
sum_up(*values)
```

Output:

```
2 + 3 + 4 = 9
```

> **About the `.py` file:** it includes a `pause()` helper that waits for you to press Enter between the
> examples, so you can read each result before the next one appears.

---

