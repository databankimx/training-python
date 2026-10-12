## List Comprehensions

List comprehensions provide a way to create a list with some set of constraints
in a single line of code.

Using comprehensions where they can logically replace more verbose code is
often seen as a mark of competency for newer Python developers.

---

Up to now, we have used loops to populate lists.
For example, this will generate a list of the first 10 squares

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

An easy way to think of a list comprehension is a loop that computes an 
expression on each iteration and automatically appends the result to a list.

A comprehension allows you to define the content of a list based on an 
expression, simplifying the loop.

Syntax:

```python
[expression_on_var for var in collection]
```

---

### List Comprehension for List of Squares

We can accomplish the same result as the loop above with the following list
comprehension:

```python
squares = [value ** 2 for value in range(1, 11)]
print(squares)
```

Output:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

---

You can also add a condition to a list comprehension to filter the results

Syntax:

```python
[expression_on_var for var in collection if condition]
```

---

### List Comprehension for List of Even Squares

```python
even_squares = [value ** 2 for value in range(1, 11) if value % 2 == 0]
print(even_squares)
```

Output:

```
[4, 16, 36, 64, 100]
```

---

### Always Balance Concision with Readability

You can create very complex list comprehensions

Consider this example:

```python
[["" if item == " " else item if item != "ChangeMe" else some_value for item in row][:-1] for row in response]
```

This comprehension is iterating across rows of data and the elements in the 
rows (omitting the last element in each) and replacing them with:

* An empty string if they contain a single space character
* A default value if they contain the string "ChangeMe"
* Or not at all (keep original value) under any other conditions.

It's quite concise, since it replaces two nested loops. However, it can be 
pretty difficult for the next developer to read and understand.

We've sacrificed readability in order to force-fit a list comprehension.

Even though comprehensions are considered Pythonic, the tendency to use them
should be balanced with keeping your code readable.

In this instance, we might be better off keeping at least one of the loops.

---
