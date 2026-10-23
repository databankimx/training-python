## The Walrus Operator `:=`

Python has a special operator that lets you assign a variable inside an expression.

This *assignment expression operator*, `:=`, is affectionately called the *walrus operator*.

---

### Walrus Operator in a `print()` Statement

For the sake of simplicity, let's say we want to square a number and then compare it with a maximum
value.

#### Without a Walrus Operator

We might write it like this:

```python
max_n = 100
n = 9
n_squared = n ** 2
print(f"{n}² = {n_squared}")
infix = "" if n_squared > max_n else "not "
print(f"{n_squared} is {infix}greater than {max_n}\n")
```

Output:

```
9² = 81
81 is not greater than 100
```

---

#### Using the Walrus Operator

We don't need `n_squared` until the f-string in the `print()` statement evaluates it, so we can assign
it right there with the walrus operator:

```python
max_n = 100
n = 9
print(f"{n}² = {(n_squared := n ** 2)}")
infix = "" if n_squared > max_n else "not "
print(f"{n_squared} is {infix}greater than {max_n}\n")
```

Output:

```
9² = 81
81 is not greater than 100
```

The result is the same. The value computed inside the expression is still available in `n_squared`
after the statement finishes.

---

### Reading Input Until a Sentinel

The walrus operator really earns its keep in a `while` loop that reads input. A *sentinel* is a value
that tells the loop to stop, such as `quit`.

Without the walrus operator, you need the `input()` call twice: once before the loop, so the condition
has something to test, and once inside the loop, to get the next value:

```python
message = input("> ")
while message.lower() != "quit":
    print(message)
    message = input("> ")
```

With the walrus operator, the assignment and the test happen together in the loop condition, so the
`input()` call appears only once:

```python
while (message := input("> ")).lower() != "quit":
    print(message)
```

Both versions do the same thing. The `.lower()` call makes the check case-insensitive, so `QUIT` also
ends the loop. If the user types `hi`, then `there`, then `quit`, each one prints:

```
hi
there
```

The `quit` ends the loop and is never printed. The walrus version is shorter, and it can't fall out of
step, because there's only one place where the input is read.

---

### Walrus Operator in a List Comprehension

You can use the walrus operator in any expression. Here's an example in a list comprehension:

```python
n = 9
odd_squares = [y for x in range(1, n + 1) if (y := x ** 2) % 2]
print(odd_squares)
```

Output:

```
[1, 9, 25, 49, 81]
```

The `if` clause computes `y` and assigns it, and the expression at the front of the comprehension uses
that same `y`. The walrus lets the condition and the output share one calculation.

---

#### Why is that useful?

Without the walrus operator, you could write a loop like this:

```python
n = 9
odd_squares = []
for x in range(1, n + 1):
    y = x ** 2
    if y % 2:
        odd_squares.append(y)
```

To use a list comprehension instead, you might write this:

```python
n = 9
odd_squares = [x ** 2 for x in range(1, n + 1) if x ** 2 % 2]
```

That works, but it computes `x ** 2` twice, once to test it and once to keep it. The walrus operator
lets you compute it once.

---
