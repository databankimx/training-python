## Nested Formatters

Sometimes you may not know what value you want in a format specifier when
you're writing your code. You might, for example, need to determine the width
at runtime.

Let's imagine a scenario where we know we will receive a set of integers, and
we need to add them up and display them similarly to this:

```
     1
    10
   100
+ 1000
------
  1111
```

We could guess at the necessary width for our format specifier, but sooner or
later, we would encounter a scenario where a number is too long or all the
numbers are too short.

In a scenario like this, it is useful to be able to specify a variable width.

But how?

---

### Making Sure We Can't Predict the Length

For this example, I've implemented this function to generate a short, random
list of integer values.

```python
from random import randint

def get_random_numbers(min: int=1, max: int=1000, length: int=5) -> list[int]:
    """Get a list of random integers"""
    return [randint(min, max) for _ in range(length)]
```

After generating a list using the default values for this function, we could
have all one-digit numbers, some four-digit numbers, or anything in between.

---

### Just Embedding the Name Isn't Allowed

Let's create a function to print out all the numbers and the sum in the 
pattern specified above.

We might imagine that we could just embed the variable name `width` where the
width specifier belongs in order to set a width at runtime...

```python
def align_numbers(numbers: list[int]) -> None:
    """Right-justify numbers for proper alignment"""
    total = sum(numbers)
    width = max(len(str(n)) for n in numbers + [total]) + 1
    for i in range(len(numbers)):
        lead = "+" if i == len(numbers) - 1 else " "
        print(f"{lead}{numbers[i]:>width}") # `width` used here
    print("-" * (width + 1))
    print(f" {sum(numbers):>width}")        # and here

numbers = get_random_numbers()
align_numbers(numbers)
```

... but this doesn't work.

Output:

```
Traceback (most recent call last):
  File "...\16_nested_formatters.py", line 21, in <module>
    main()
  File "...\16_nested_formatters.py", line 18, in main
    align_numbers(numbers)
  File "...", line 12, in align_numbers     
    print(f"{lead}{numbers[i]:>width}")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: Invalid format specifier '>width' for object of type 'int'
```

We got a `ValueError`, because the format specifier is expecting an integer.

---

### Nesting Replacement Fields

A little-known Python feature is that any format specifier can contain nested
replacement fields, like this: `f"{my_var:{fill}{align}10}"`

With that tidbit, we can easily fix our function like this:

```python
def align_numbers(numbers: list[int]) -> None:
    """Right-justify numbers for proper alignment"""
    total = sum(numbers)
    width = max(len(str(n)) for n in numbers + [total]) + 1
    for i in range(len(numbers)):
        lead = "+" if i == len(numbers) - 1 else " "
        print(f"{lead}{numbers[i]:>{width}}")
    print("-" * (width + 1))
    print(f" {total:>{width}}")

numbers = get_random_numbers()
align_numbers(numbers)
```

Output:

> Note: Your numbers will vary (they're random after all)

```
      2
    356
     27
    251
+  1000
-------
   1636
```

Et voila! We've solved the variable width problem.

You can use this technique to nest variable values for any of your specifier
characters,

---
