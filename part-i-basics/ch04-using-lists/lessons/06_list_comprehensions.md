## List Comprehensions

A list comprehension builds a list in a single line. It's a compact way to write a loop
whose only job is to create a list.

Comprehensions are a common idiom in Python, so you'll see them in plenty of code. Being
able to read them comfortably is part of reading Python well.

---

Up to now, we've used loops to populate lists. For example, this creates a list of the
first 10 squares:

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

An easy way to think of a list comprehension is a loop that computes an expression on
each iteration and appends the result to a list, all in one step. You describe the
contents of the list with an expression, and the comprehension does the looping for you.

The syntax is:

```python
[expression_on_var for var in collection]
```

---

### A List Comprehension for Squares

Here's the same result as the loop above, in one line:

```python
squares = [value ** 2 for value in range(1, 11)]
print(squares)
```

Output:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

### Adding a Condition

You can also add an `if` condition to filter the results. The syntax is:

```python
[expression_on_var for var in collection if condition]
```

Here's a list of even squares:

```python
even_squares = [value ** 2 for value in range(1, 11) if value % 2 == 0]
print(even_squares)
```

Output:

```
[4, 16, 36, 64, 100]
```

Notice the difference. The `if` at the end filters which values make it into the list. The
expression at the front decides what each kept value becomes.

---

### Always Balance Concision with Readability

Comprehensions can get very complex. Consider this example:

```python
[["" if item == " " else item if item != "ChangeMe" else some_value for item in row][:-1] for row in response]
```

Before you read on, know that `some_value` is a placeholder, and `response` is some
collection of rows. The interesting part is the conditional expression. It has the form
`value_if_true if condition else value_if_false`, and it can be chained, as it is here.
Read from left to right:

* An empty string if the item is a single space
* Otherwise, `some_value` if the item is the string `"ChangeMe"`
* Otherwise, the item itself

This comprehension iterates over the rows and the items in each row, dropping the last
element of each row. It's concise, since it replaces two nested loops. It's also hard to
read, and the next developer to look at it might spend a long time figuring out what it
does.

We've traded readability for brevity, and it's not a good trade here. Comprehensions are
a good tool, but they shouldn't be the only tool. In this case, keeping at least one of the
loops would make the code clearer, and nobody would mind the extra two lines.

---

