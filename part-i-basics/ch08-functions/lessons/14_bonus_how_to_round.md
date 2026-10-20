## Bonus Lesson - Understanding Rounding

An initial note...

For this lesson, I have prepared a separate module
[rounding_functions.py](./rounding_functions.py) containing the following code:

<details>
<summary>Rounding Functions Source Code</summary>

```python
import math

def truncate(n: float, dec: int=0) -> float:
    """Truncate a number to a specified number of decimal places"""
    mult = 10 ** dec
    return int(n * mult) / mult


def round_up(n: float, dec: int=0) -> float:
    """Round a number up to a specified number of decimal places"""
    mult = 10 ** dec
    return math.ceil(n * mult) / mult


def round_down(n: float, dec: int=0) -> float:
    """Round a number down to a specified number of decimal places"""
    mult = 10 ** dec
    return math.floor(n * mult) / mult


def round_half_up(n: float, dec: int=0) -> float:
    """Round a number to a specified number of decimal places (where 5 rounds up)"""
    mult = 10 ** dec
    return math.floor(n * mult + 0.5) / mult


def round_half_down(n: float, dec: int=0) -> float:
    """Round a number to a specified number of decimal places (where 5 rounds down)"""
    mult = 10 ** dec
    return math.ceil(n * mult - 0.5) / mult


def round_half_away_from_zero(n: float, dec: int=0) -> float:
    """Round a number to a specified number of decimal places (where 5 rounds up and negative 5 rounds down)"""
    rounded_abs = round_half_up(abs(n), dec)
    return math.copysign(rounded_abs, n)


def round_half_toward_zero(n: float, dec: int=0) -> float:
    """Round a number to a specified number of decimal places (where 5 rounds down and negative 5 rounds down)"""
    rounded_abs = round_half_down(abs(n), dec)
    return math.copysign(rounded_abs, n)


def round_half_to_even(n: float, dec: int=0) -> float:
    """Round a number to a specified number of decimal places (where 5 rounds up or down to an even number)"""
    return round(n, dec)


def average(numbers: list[float]) -> float:
    """Calculate the average from a list of numbers"""
    return sum(numbers) / len(numbers)
```

</details>
<br>

In order to use the code samples below, you'll need to import a few modules 
into your Python file:

```python
from rounding_functions import *
from statistics import mean
import random
```

And although it's not strictly required, it's probably advisable to seed the
random number generator:

```python
random.seed(100)
```

As we proceed, I will not be repeating sections we've already added to the 
code, so assume that you'll need everything prior for any test.

---

Now that we're looking at libraries and common functions, it's worth taking a 
side-trip to discuss rounding.

Although Python exposes a `round()` function for rounding floating-point 
numbers, it may not necessarily behave the way you expect.

We'll look at a number of strategies for rounding.

Let's include some floating-point numbers to use for rounding in our tests.

```python
pi = 3.14159265359
x = 1.5
y = 2.5
```

---

### Python's `round()` Function

The `round()` function in Python accepts two arguments:

* `number`: The value to be rounded
* `ndigits`: The number of decimal places to round to
    * If omitted, the function will round to an integer

---

#### Sometimes, the `round()` result is what we expect

```python
print("round(pi)", round(pi))
print("round(pi)", round(pi, 2))
```

Output:

```
round(pi) 3
round(pi) 3.14
```

That output is exactly what we expected. So far so good.

---

#### Other times, unexpected results occur

```python
print(f"round({x}) =", round(x))
print(f"round({y}) =", round(y))
```

Output:

```
round(1.5) = 2
round(2.5) = 2
```

When we rounded `1.5`, the result was `2`, which is exactly what we expect

But when we rounded `2.5`, the answer was also `2`, which is decidedly **not**
what we expect.

What gives?

---

#### Introducing Banker's Rounding

Python implements the "*Banker's Rounding*" or round-to-even strategy. This
differs from the standard 5/4 rounding that people typically use in one crucial
way.

> When the decimal part of the number to be rounded is exactly `.5`, this
> algorithm does not always round up. Instead, it rounds to the nearest even
> number.

There's a very good reason why this strategy is chosen. Python expects to be
used on large amounts of statistical data. If we always rounded up on `.5`,
it would introduce a significant amount of rounding error into statistical
computations. So the round-to-even algorithm is used to minimize the amount of
rounding error.

---

### Other Rounding Strategies

Unfortunately, if we're working with small amounts of information (like a
single user's entries on a form), this would not be the best choice.

The question then is what rounding strategies exist, and which is the best
suited to a given problem.

---

#### Truncation Rounding

In truncation rounding, we simply ignore whatever decimal value exists to the 
right of the position to which we are rounding.

```python
print("Truncating:")
print(f"truncate(pi, 2) = ", truncate(pi, 2))
print(f"truncate(pi) = ", truncate(pi))
print(f"truncate({x}) = ", truncate(x))
print(f"truncate({y}) = ", truncate(y))
```

Output:

```
Truncating:
truncate(pi, 2) =  3.14
truncate(pi) =  3.0
truncate(1.5) =  1.0
truncate(2.5) =  2.0
```

Arguably, this is further from out intent than the `round()` function, since
now, both `1.5` and `2.5` are rounded down.

---

#### Always Round Up

In this strategy, we will round up any decimal value to the next higher number

```python
print("Rounding Up:")
print(f"round_up(pi, 2) = ", round_up(pi, 2))
print(f"round_up(pi) = ", round_up(pi))
print(f"round_up({x}) = ", round_up(x))
print(f"round_up({y}) = ", round_up(y))
```

Output:

```
Rounding Up:
round_up(pi, 2) =  3.15
round_up(pi) =  4.0
round_up(1.5) =  2.0
round_up(2.5) =  3.0
```

A whole lot of these results are not what we want, especially rounding pi to
`4.0`

---

#### Rounding Down

In this strategy, we will round down any decimal value to the next lower number

This is functionally identical to the truncation rounding strategy but may be
implemented differently in code.

```python
print("Rounding Down:")
print(f"round_down(pi, 2) = ", round_down(pi, 2))
print(f"round_down(pi) = ", round_down(pi))
print(f"round_down({x}) = ", round_down(x))
print(f"round_down({y}) = ", round_down(y))
```

Output:

```
Rounding Down:
round_down(pi, 2) =  3.14
round_down(pi) =  3.0
round_down(1.5) =  1.0
round_down(2.5) =  2.0
```

Of course, these results have the same issues as truncation

---

#### Rounding Half Up

In this strategy, we calculate what most people would select if manually
rounding, where `.499999...` rounds down but `.5` rounds up.

```python
print("Rounding Half Up:")
print(f"round_half_up(pi, 2) = ", round_half_up(pi, 2))
print(f"round_half_up(pi) = ", round_half_up(pi))
print(f"round_half_up({x}) = ", round_half_up(x))
print(f"round_half_up({y}) = ", round_half_up(y))
```

Output:

```
Rounding Half Up:
round_half_up(pi, 2) =  3.14
round_half_up(pi) =  3.0
round_half_up(1.5) =  2.0
round_half_up(2.5) =  3.0
```

This might not always be the best strategy, but it matches what we learned in
grade-school arithmetic, so it may be the best choice if presenting individual 
rounded numbers to a user.

---

#### Rounding Half Down

In this strategy, we perform a slightly different calculation, where
`.5` rounds down but `.500...01` rounds up.

```python
print("Rounding Half Down:")
print(f"round_half_down(pi, 2) = ", round_half_down(pi, 2))
print(f"round_half_down(pi) = ", round_half_down(pi))
print(f"round_half_down({x}) = ", round_half_down(x))
print(f"round_half_down({y}) = ", round_half_down(y))
```

Output:

```
Rounding Half Down:
round_half_down(pi, 2) =  3.14
round_half_down(pi) =  3.0
round_half_down(1.5) =  1.0
round_half_down(2.5) =  2.0
```

Again, we have more unexpected results from this strategy than `round()` did

---

#### Rounding Half Away From Zero

So far, we've made an error in thinking too narrowly, ignoring the possibility
that we might need to round negative numbers.

In the round half up strategy, we would have properly rounded positive numbers

* `round_half_up(2.5)` yields `3.0`

... but for negative numbers, we have an issue:

* `round_half_up(-2.5)` yields `-2.0`

In the round half away from zero strategy, we always round a decimal of `.5` 
away from zero, so:

* `round_half_away_from_zero(2.5)` yields `3.0`  
  and
* `round_half_away_from_zero(-2.5)` yields `-3.0`

```python
print("Rounding Half away from Zero:")
print(f"round_half_away_from_zero(pi, 2) = ", round_half_away_from_zero(pi, 2))
print(f"round_half_away_from_zero(pi) = ", round_half_away_from_zero(pi))
print(f"round_half_away_from_zero({x}) = ", round_half_away_from_zero(x))
print(f"round_half_away_from_zero({y}) = ", round_half_away_from_zero(y))
print(f"round_half_away_from_zero(-{x}) = ", round_half_away_from_zero(-x))
print(f"round_half_away_from_zero(-{y}) = ", round_half_away_from_zero(-y))
```

Output:

```
Rounding Half away from Zero:
round_half_away_from_zero(pi, 2) =  3.14
round_half_away_from_zero(pi) =  3.0
round_half_away_from_zero(1.5) =  2.0
round_half_away_from_zero(2.5) =  3.0
round_half_away_from_zero(-1.5) =  -2.0
round_half_away_from_zero(-2.5) =  -3.0
```

Finally, we have an algorithm that approximates the human-style rounding
process.

---

#### Rounding Half Toward Zero

Just like the round-half-away-from-zero was essentially the same as
round-half-up but with the added capability to round negative numbers,
this strategy supports negative numbers but behaves like round-half-down.

```python
print("Rounding Half toward Zero:")
print(f"round_half_toward_zero(pi, 2) = ", round_half_toward_zero(pi, 2))
print(f"round_half_toward_zero(pi) = ", round_half_toward_zero(pi))
print(f"round_half_toward_zero({x}) = ", round_half_toward_zero(x))
print(f"round_half_toward_zero({y}) = ", round_half_toward_zero(y))
print(f"round_half_toward_zero(-{x}) = ", round_half_toward_zero(-x))
print(f"round_half_toward_zero(-{y}) = ", round_half_toward_zero(-y))
```

Output:

```
Rounding Half toward Zero:
round_half_toward_zero(pi, 2) =  3.14
round_half_toward_zero(pi) =  3.0
round_half_toward_zero(1.5) =  1.0
round_half_toward_zero(2.5) =  2.0
round_half_toward_zero(-1.5) =  -1.0
round_half_toward_zero(-2.5) =  -2.0
```

---

#### Rounding Half to Even

Here, we've explicitly implemented the same algorithm that the Python
`round()` function uses.

```python
print("Rounding Half to Even:")
print(f"round_half_to_even(pi, 2) = ", round_half_to_even(pi, 2))
print(f"round_half_to_even(pi) = ", round_half_to_even(pi))
print(f"round_half_to_even({x}) = ", round_half_to_even(x))
print(f"round_half_to_even({y}) = ", round_half_to_even(y))
```

Output:

```
Rounding Half to Even:
round_half_to_even(pi, 2) =  3.14
round_half_to_even(pi) =  3.0
round_half_to_even(1.5) =  2.0
round_half_to_even(2.5) =  2.0
```

---

#### Some Statistics on Rounding Strategy Behavior

We can look at the extent of rounding error introduced by each rounding
strategy.

We'll create a list of values to test on and then calculate the averages
of the rounded data from each strategy.

```python
print("** Rounding Bias Examples **")
print("----------------------------")
print("Computed Average:          ", average(data))
print("Statistical Mean:          ", mean(data))
print("Rounded Mean:              ", average([round(x, d) for x in data]))
print("Truncated Mean:            ", average([truncate(x, d) for x in data]))
print("Round Up Mean:             ", average([round_up(x, d) for x in data]))
print("Round Down Mean:           ", average([round_down(x, d) for x in data]))
print("Round Half Up Mean:        ", average([round_half_up(x, d) for x in data]))
print("Round Half Down Mean:      ", average([round_half_down(x, d) for x in data]))
print("Round Away from Zero Mean: ", average([round_half_away_from_zero(x, d) for x in data]))
print("Round Toward Zero Mean:    ", average([round_half_toward_zero(x, d) for x in data]))
print("Round Half to Even Mean:   ", average([round_half_to_even(x, d) for x in data]))
```

Output:

```
Computed Average:           4.95
Statistical Mean:           4.95
Rounded Mean:               4.95
Truncated Mean:             4.5
Round Up Mean:              5.4
Round Down Mean:            4.5
Round Half Up Mean:         5.0
Round Half Down Mean:       4.9
Round Away from Zero Mean:  5.0
Round Toward Zero Mean:     4.9
Round Half to Even Mean:    4.95
```

As you can see, although other strategies might more closely approximate what
we (as humans) think rounding means, statistically speaking, the Python default
algorithm implemented in `round()` is the best when working with large amounts
of data.

---
