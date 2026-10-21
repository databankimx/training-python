## Numeric Lists and the `range()` Function

The `range()` function gives you a sequence of numbers without making you type them
out. It's the standard tool for loops that count, and for building lists of numbers.

Here's the syntax:

```python
range([start,] stop[, step])
```

The rules are simple, with one catch:

* The `stop` value is the first number you *don't* want. In other words, it must be one
  higher than the last value you want to include. This is often called "off-by-one"
  behavior, and it trips up almost everyone at first.
* The `step` value is the increment between one number and the next.
* If you give `range()` only one value, it's the `stop`. The `start` defaults to `0`,
  and the `step` defaults to `1`.
* If you give it two values, they're `start` and `stop`, and the `step` defaults to `1`.

---

### Examples

#### A `range` with only `stop` specified

```python
for i in range(3):
    print(i)
```

Output:

```
0
1
2
```

Notice that `3` never shows up. That's the off-by-one rule at work.

---

#### A `range` with `start` and `stop` specified

```python
for i in range(1, 4):
    print(i)
```

Output:

```
1
2
3
```

---

#### A `range` with `start`, `stop`, and `step` specified

```python
for i in range(2, 7, 2):
    print(i)
```

Output:

```
2
4
6
```

A negative step counts down. The `stop` is still the first number you don't want, so
for a countdown, it sits below the last value:

```python
for i in range(10, 0, -2):
    print(i)
```

Output:

```
10
8
6
4
2
```

---

### What `range()` Actually Is

`range()` doesn't produce a list. It produces a *range object*, which knows how to make
the numbers as you ask for them. It doesn't store them all in memory first, so a range of a
billion numbers costs about the same as a range of ten.

Print one, and you can see that:

```python
print(range(3))
```

Output:

```
range(0, 3)
```

If you want an actual list, convert it with `list()`:

```python
numbers = list(range(1, 6))
print(numbers)
```

Output:

```
[1, 2, 3, 4, 5]
```

You can also unpack a range into separate variables, the same way you'd unpack a list
(see lesson 2.12):

```python
one, two, three = range(1, 4)
print(f"{one} - {two} - {three}")
```

Output:

```
1 - 2 - 3
```

---

### A Loop Using a `range` to Create a List

Put the pieces together, and you can build a list of numbers with a loop:

```python
squares = []
for value in range(1, 6):
    squares.append(value ** 2)
print(squares)
```

Output:

```
[1, 4, 9, 16, 25]
```

---

