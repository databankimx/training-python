## Bonus: Type Hints and Function Documentation

> Note: Even though I am introducing this topic here, the textbook does not
> cover this material.
>
> Because of this, examples in later chapters will (for the most part) not
> implement type hinting or detailed doc strings.

In VS Code, when you hover over a predefined function name, you are presented
with a pop-up dialog providing details about how to properly use the function.

For example, here is the function helper for `print()`

<img src="../../../../00 - Resources/Setup Documents/images/print-docstring.png" style="width:350px">

From this, we can tell a lot about the function and how we're expected to use 
it.

* The function's purpose is "*Prints the values to a stream or to sys.stdout
  by default.*"
* From `*values: object`, we can see that it accepts an arbitrary number of 
  arguments of any type that inherits from `object` and prints each one.
* From `sep: str | None = " "`, we can see that we're allowed to add a keyword 
  argument `sep`
    * This provides the "*string inserted between values, default a space*"
    * If added, this must be of the `str` type
    * If omitted (`None`), this defaults to `" "`
* The function returns `None`
* And so on...

This is enormously useful to any developer who is not the author of the 
function.

Let's take a look at how we can document our own functions so that others can
have the same advantage when working with modules we develop.

---

### Function Without Hints

Let's imagine that we have written this function

```python
def calculate(operation, x, y):
    op = operation[0].lower()
    if op == "a":
        # add
        return x + y
    elif op == "s":
        # subtract
        return x - y
    elif op == "m":
        # multiply
        return x * y
    elif op == "d":
        # divide
        return x / y
    else:
        print(f"Operation [{operation}] not supported!")
        return None
```

The function works as expected, but the pop-up helper is sparse and not very
informative:

<img src="../../../../00 - Resources/Setup Documents/images/type-hints-01.png" style="width:180px">

We're not provided any information about what the function does or what data it
expects as arguments and what type it returns.

---

### Adding a Doc String

As we've mentioned before, we should always include a doc string on the 
function.

```python
def calculate(operation, x, y):
    """Perform selected arithmetic calculation"""
    # -- SNIP --
```

After we add this, we now have more information in the helper. It tells us the
purpose of the function.

<img src="../../../../00 - Resources/Setup Documents/images/type-hints-02.png" style="width:220px">

---

### Adding Type Hints

Python allows the developer to specify the expected data type for function
parameters using this syntax:  
`def function(param1: type1, ...):`

Additionally, we can specify the return data type using this syntax:  
`def function() -> return_type:`

So, updating our function signature like this...

```python
def calculate(operation: str, x: int, y: int) -> int:
    """Perform selected arithmetic calculation"""
    # -- SNIP --
```

... further improves the helper documentation so that now we see this:

<img src="../../../../00 - Resources/Setup Documents/images/type-hints-03.png" style="width:220px">

Now the developer can see the expected data types for the function arguments
and the return data type.

---

### Type Hints with Multiple Possible Types

Starting in Python v3.10, we now have the ability to specify multiple possible
types for a parameter or return type, separated by a vertical pipe `|`
(bitwise OR)  
`type1 | type2`

This lets us further improve our function documentation in the signature like
this:

```python
def calculate(operation: str, x: int|float, y: int|float) -> int|float:
    """Perform selected arithmetic calculation"""
    # -- SNIP --
```

Which lets the developer know that either integers or floating-point numbers
are valid for this function.

<img src="../../../../00 - Resources/Setup Documents/images/type-hints-04.png" style="width:220px">

---

### Adding Parameters to the Doc String

Additionally, we can add explanations of the parameters to the doc string.

The doc string is displayed as markdown, so:

* To separate the parameters from the function explanation, leave two carriage
  returns.
* To force a new line after each parameter, end the line with two spaces.
* To make an item boldface, surround it with double-asterisks
* etc.

For our function, the doc string will now look like this:

```python
def calculate(operation: str, x: int|float, y: int|float) -> int|float:
    """
    Perform selected arithmetic calculation

    Parameters:  
    **operation**: Arithmetic operation to perform
    * [a]dd
    * [s]ubtract
    * [m]ultiply
    * [d]ivide)  
    **x**: Left numerical operand  
    **y**: Right numerical operand
    """
```

Which will result in a very informative function helper like this:

<img src="../../../../00 - Resources/Setup Documents/images/type-hints-05.png" style="width:420px">

---

### Adding the Return to the Doc String

Lastly, we can add a description of the return to the doc string:

The same markdown rules apply as we discussed above in parameter
documentation.

Here is the function with the return type added:

```python
def calculate(operation: str, x: int|float, y: int|float) -> int|float:
    """
    Perform selected arithmetic calculation

    Parameters:  
    **operation**: Arithmetic operation to perform
    * [a]dd
    * [s]ubtract
    * [m]ultiply
    * [d]ivide)  
    **x**: Left numerical operand  
    **y**: Right numerical operand

    **Returns**:  
    the result of the arithmetic operation
    """
```

Which will result in a complete function helper like this:

<img src="../../../../00 - Resources/Setup Documents/images/type-hints-06-top.png" style="width:420px">  
<img src="../../../../00 - Resources/Setup Documents/images/type-hints-06-bottom.png" style="width:420px">

---
