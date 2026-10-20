## The Walrus Operator `:=`

Python implements a special operator to permit assigning a variable
within an expression.

This *assignment expression operator* `:=` is affectionately called the 
*walrus operator*.

---

### Walrus Operator in a `print()` Statement

For the sake of simplicity, let's imagine we want to square a number and 
then compare it with a max value.

#### Without a Walrus Operator

We might implement it like this:

```python
max = 100
n = 9
n_squared = n ** 2
print(f"{n}² = {n_squared}")
infix = "" if n_squared > max else "not "
print(f"{n_squared} is {infix}greater than {max}\n")
```

Output:

```
9² = 81
81 is not greater than 100
```

---

#### Using the Walrus Operator

However, since we don't need the variable until it is evaluated in the
f-string in the `print()` statement, we can assign it inline there using 
the walrus operator:

```python
max = 100
n = 9
print(f"{n}² = {(n_squared := n ** 2)}")
infix = "" if n_squared > max else "not "
print(f"{n_squared} is {infix}greater than {max}\n")
```

Output:

```
9² = 81
81 is not greater than 100
```

The result is the same, and the value computed in the expression is
available in the variable after the statement completes.

---

### Walrus Operator in a List Comprehension

We can use a walrus operator in any expression. Here's an example of its
use in a list comprehension:

```python
n = 9
odd_squares = [y for x in range(1, n + 1) if (y := x ** 2) % 2]
print(odd_squares)
```

Output:

```
[1, 9, 25, 49, 81]
```

Note how we can use the variable `y` earlier in the comprehension than we
assign it. This results in an efficient algorithm.

---

#### Why is that useful?

Without using a walrus operator, we could implement a loop like this:

```python
n = 9
odd_squares = []
for x in range(1, n + 1):
    y = x ** 2
    if y % 2:
        odd_squares.append(y)
```

But if we wanted to use a list comprehension instead of a loop, we might 
end up with this:

```python
n = 9
odd_squares = [x ** 2 for x in range(1, n + 1) if x ** 2 % 2]
```

That would work, but in order to both compare and obtain the square, we're
computing `x ** 2` twice, which is wasteful of clock cycles.

---
