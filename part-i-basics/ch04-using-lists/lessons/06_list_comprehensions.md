## List Comprehensions

List comprehensions provide a concise way to generate a list in a single line.
Using them where they naturally replace a verbose loop is often considered a
mark of Python fluency.

---

### The Loop Approach

This generates a list of the first 10 squares:

```python
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
```

Output:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

### The List Comprehension

The same result in one line:

```python
squares = [value ** 2 for value in range(1, 11)]
print(squares)
```

Output:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Syntax:

```python
[expression for var in collection]
```

---

### Adding a Filter Condition

You can add an `if` clause to filter which items are included:

```python
even_squares = [value ** 2 for value in range(1, 11) if value % 2 == 0]
print(even_squares)
```

Output:

```
[4, 16, 36, 64, 100]
```

Syntax:

```python
[expression for var in collection if condition]
```

---

### Balance Concision with Readability

You can write very complex list comprehensions, but that doesn't mean you
should. Consider this example:

```python
[["" if item == " " else item if item != "ChangeMe" else some_value
  for item in row][:-1] for row in response]
```

This replaces two nested loops and is quite concise. It is also difficult
for the next developer to read. Using comprehensions is Pythonic; using them
past the point where the code remains readable is not.

When in doubt, keep the loop.

---
