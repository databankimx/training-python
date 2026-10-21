## Bonus Lesson: Understanding Rounding

Rounding looks simple, but Python's `round()` doesn't always behave the way people expect. This lesson
looks at why, and at the other rounding strategies you can choose from.

For this lesson, I've prepared a separate module, [rounding_functions.py](./rounding_functions.py). It
contains the following code:

<details>
<summary>Rounding Functions Source Code</summary>

```python
import math


def truncate(n: float, dec: int = 0) -> float:
    """Truncate a number to a specified number of decimal places"""
    mult = 10 ** dec
    return int(n * mult) / mult


def round_up(n: float, dec: int = 0) -> float:
    """Round a number up to a specified number of decimal places"""
    mult = 10 ** dec
    return math.ceil(n * mult) / mult


def round_down(n: float, dec: int = 0) -> float:
    """Round a number down to a specified number of decimal places"""
    mult = 10 ** dec
    return math.floor(n * mult) / mult


def round_half_up(n: float, dec: int = 0) -> float:
    """Round a number to a specified number of decimal places (where 5 rounds up)"""
    mult = 10 ** dec
    return math.floor(n * mult + 0.5) / mult


def round_half_down(n: float, dec: int = 0) -> float:
    """Round a number to a specified number of decimal places (where 5 rounds down)"""
    mult = 10 ** dec
    return math.ceil(n * mult - 0.5) / mult


def round_half_away_from_zero(n: float, dec: int = 0) -> float:
    """Round a number to a specified number of decimal places
       (where 5 rounds up and negative 5 rounds down)"""
    rounded_abs = round_half_up(abs(n), dec)
    return math.copysign(rounded_abs, n)


def round_half_toward_zero(n: float, dec: int = 0) -> float:
    """Round a number to a specified number of decimal places
       (where 5 rounds down and negative 5 rounds down)"""
    rounded_abs = round_half_down(abs(n), dec)
    return math.copysign(rounded_abs, n)


def round_half_to_even(n: float, dec: int = 0) -> float:
    """Round a number to a specified number of decimal places
       (where 5 rounds up or down to an even number)"""
    return round(n, dec)


def average(numbers: list[float]) -> float:
    """Calculate the average from a list of numbers"""
    return sum(numbers) / len(numbers)
```

</details>
<br>

To run the examples below, import the functions into your Python file:

```python
from rounding_functions import (
    truncate,
    round_up,
    round_down,
    round_half_up,
    round_half_down,
    round_half_away_from_zero,
    round_half_toward_zero,
    round_half_to_even,
    average,
)
from statistics import mean
import random
```

It's not strictly required, but it's a good idea to seed the random number generator, so the results
repeat from run to run:

```python
random.seed(100)
```

As we go, I won't repeat code we've already written. Assume you need everything from earlier sections
for each new example.

The `.py` file for this lesson also uses `pause()` and `clear_terminal()` from the `sm_utils` package, so
it waits for you between sections.

---

Now that we're working with libraries and common functions, it's worth a side trip to discuss rounding.

Python provides a `round()` function for floating-point numbers, but it may not always behave the way you
expect. We'll look at several strategies for rounding.

Let's define some floating-point numbers to use in our tests.

```python
pi = 3.14159265359
x = 1.5
y = 2.5
```

---

### Python's `round()` Function

The `round()` function accepts two arguments:

* `number`: The value to round
* `ndigits`: The number of decimal places to round to
    * If you leave it out, the function rounds to an integer

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

That's what we expected, so far so good.

---

#### Other times, the results are unexpected

```python
print(f"round({x}) =", round(x))
print(f"round({y}) =", round(y))
```

Output:

```
round(1.5) = 2
round(2.5) = 2
```

Rounding `1.5` to `2` is what we expect. But rounding `2.5` also gives `2`, which is not what most
people expect.

What gives?

---

#### Introducing Banker's Rounding

Python uses a strategy called *Banker's rounding*, or round-to-even. It differs from the standard
round-half-up method people usually learn in one important way.

> When the part of the number after the decimal point is exactly `.5`, this algorithm doesn't always
> round up. Instead, it rounds to the nearest even number.

Round-to-even has a good reason behind it. If you always rounded `.5` up, then over many values the
rounding would push the average upward. Round-to-even cancels out that bias, because half of the `.5`
cases go up and half go down. That's why it's the default for `round()`.

---

### Other Rounding Strategies

If you're rounding a small number of values, like a single user's entries on a form, round-to-even
might not be the best choice. Its benefit only shows up across many values.

So the question is which strategy fits a given problem. Let's compare them.

---

#### Truncation

Truncation ignores every digit to the right of the position you're rounding to.

```python
print("Truncating:")
print("truncate(pi, 2) = ", truncate(pi, 2))
print("truncate(pi) = ", truncate(pi))
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

This is further from our intent than `round()`, because both `1.5` and `2.5` round down.

---

#### Always Round Up

This strategy rounds any decimal value up to the next higher number.

```python
print("Rounding Up:")
print("round_up(pi, 2) = ", round_up(pi, 2))
print("round_up(pi) = ", round_up(pi))
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

Many of these results aren't what we want. Rounding pi to `4.0` is a clear example.

---

#### Rounding Down

This strategy rounds any decimal value down to the next lower number.

It behaves the same as truncation for positive numbers, but it can be written differently in code.

```python
print("Rounding Down:")
print("round_down(pi, 2) = ", round_down(pi, 2))
print("round_down(pi) = ", round_down(pi))
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

These results have the same problems as truncation.

---

#### Rounding Half Up

This strategy matches what most people do by hand: anything below `.5` rounds down, and `.5` rounds up.

```python
print("Rounding Half Up:")
print("round_half_up(pi, 2) = ", round_half_up(pi, 2))
print("round_half_up(pi) = ", round_half_up(pi))
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

It might not be the best choice for statistics, but it matches what we learned in school. If you're
showing a single rounded number to a user, it's often the right one.

---

#### Rounding Half Down

This strategy rounds `.5` down, while anything above `.5` still rounds up.

```python
print("Rounding Half Down:")
print("round_half_down(pi, 2) = ", round_half_down(pi, 2))
print("round_half_down(pi) = ", round_half_down(pi))
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

This strategy also produces some surprising results.

---

#### Rounding Half Away from Zero

So far, we've only considered positive numbers. Negative numbers need thinking about too.

With round-half-up, positive numbers behave well:

* `round_half_up(2.5)` gives `3.0`

But negative numbers don't:

* `round_half_up(-2.5)` gives `-2.0`

Round-half-away-from-zero always moves a `.5` value away from zero, so:

* `round_half_away_from_zero(2.5)` gives `3.0`, and
* `round_half_away_from_zero(-2.5)` gives `-3.0`

```python
print("Rounding Half away from Zero:")
print("round_half_away_from_zero(pi, 2) = ", round_half_away_from_zero(pi, 2))
print("round_half_away_from_zero(pi) = ", round_half_away_from_zero(pi))
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

This is the strategy that comes closest to the human-style rounding we learned in school, including for
negative numbers.

---

#### Rounding Half Toward Zero

Round-half-away-from-zero works with negative numbers, like round-half-up, but it rounds `.5` away from
zero. Round-half-toward-zero also handles negative numbers, but it rounds `.5` toward zero, like
round-half-down.

```python
print("Rounding Half toward Zero:")
print("round_half_toward_zero(pi, 2) = ", round_half_toward_zero(pi, 2))
print("round_half_toward_zero(pi) = ", round_half_toward_zero(pi))
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

This is the algorithm Python's `round()` uses. Here it's written out explicitly.

```python
print("Rounding Half to Even:")
print("round_half_to_even(pi, 2) = ", round_half_to_even(pi, 2))
print("round_half_to_even(pi) = ", round_half_to_even(pi))
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

#### Comparing the Strategies Across Many Values

We can see how much error each strategy adds over a larger set of values. Here, we round every value to
a whole number and compare the averages.

```python
data = [i + j / 10 for i in range(10) for j in range(10)]
d = 0

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

Round-half-to-even gives the same average as the exact mean. The other strategies drift in one
direction, which is the bias we saw earlier. So for large amounts of data, `round()` is the least biased
choice. For a single value shown to a person, a different strategy may be the better fit.

---

