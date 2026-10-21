## List Statistics

Python has a handful of built-in functions that tell you something about a list.

|Function|Effect|
|-|-|
|`len(list)`|Returns the number of elements in the list|
|`min(list)`|Returns the lowest value in the list|
|`max(list)`|Returns the highest value in the list|
|`sum(list)`|Returns the sum of the values in the list|

```python
digits = list(range(10))
print(digits)
print(f"List Length:  {len(digits)}")
print(f"Minimum:      {min(digits)}")
print(f"Maximum:      {max(digits)}")
print(f"Sum:          {sum(digits)}")
```

Output:

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
List Length:  10
Minimum:      0
Maximum:      9
Sum:          45
```

---

With those values, you can work out other statistics. The mean average is the sum
divided by the length:

```python
digits = list(range(10))
print(digits)
print(f"Average:      {sum(digits) / len(digits)}")
```

Output:

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Average:      4.5
```

---

Division always gives you a float, though, even when the answer is a whole number. Try
the average of the numbers 10 through 100:

```python
tens = list(range(10, 101, 10))
print(tens)
print(f"Average:      {sum(tens) / len(tens)}")
```

Output:

```
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Average:      55.0
```

The answer is `55`, but Python reports it as `55.0`. Nothing is wrong with the math. It
just comes back as a float.

---

### The `statistics` Module

If you'd rather get `55` back, the `statistics` module has a `mean()` function that
handles this for you. Bringing a module into your program takes an `import` statement.
A module is a file full of ready-made functions, and `import` makes them available to
you. We'll cover modules properly later in the book.

```python
import statistics

tens = list(range(10, 101, 10))
print(tens)
print(f"Average:      {statistics.mean(tens)}")
```

Output:

```
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Average:      55
```

Until you've learned conditionals, `statistics.mean()` is the approach to use.

---

### A Preview: Tidying Up the Float

There's also a way to get `55` without a module, using modulo arithmetic and a
conditional. It's a preview, so don't worry about the details yet. Conditionals come
in Chapter 5, and it will make more sense then:

```python
tens = list(range(10, 101, 10))
print(tens)
avg = sum(tens) / len(tens)
mean = int(avg) if (avg * 10) % 10 == 0 else avg
print(f"Average:      {mean}")
```

Output:

```
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Average:      55
```

The line with `if` is the conditional. It says: if the average has no fractional part,
turn it into an integer. Otherwise, keep it as it is.

---

