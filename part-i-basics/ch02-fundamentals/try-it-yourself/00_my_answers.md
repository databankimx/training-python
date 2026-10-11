## Chapter 2 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 2 try-it-yourself exercises.

---

### Assignment 2.1 - Simple Message

Assign a message to a variable, and then print that message.

<details>
<summary>Spoiler Code</summary>

```python
message = "I love programming!"
print(message)
```

</details>
<br>

<details>
<summary>Output</summary>

```
I love programming!
```

</details>

---

### Assignment 2.2 - Simple Messages

Assign a message to a variable, and print that message. Then change the value
of the variable to a new message, and print the new message.

<details>
<summary>Spoiler Code</summary>

```python
message = "Programming is hard..."
print(message)
message = "No way! Programming is fun!"
print(message)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Programming is hard...
No way! Programming is fun!
```

</details>

---

### Assignment 2.3 - Personal Message

Use a variable to represent a person's name, and print a message to that
person. Your message should be simple, such as, "Hello Eric, would you like to
learn some Python today?"

<details>
<summary>Spoiler Code</summary>

```python
name = "count maurice maeterlinck"
print(f"Hello there, {name.title()}.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Hello there, Count Maurice Maeterlinck.
```

</details>

---

### Assignment 2.4 - Name Cases

Use a variable to represent a person's name, and then print that person's name
in lowercase, uppercase, and title case.

<details>
<summary>Spoiler Code</summary>

```python
name = "count maurice maeterlinck"
print(name.lower())
print(name.upper())
print(name.title())
```

</details>
<br>

<details>
<summary>Output</summary>

```
count maurice maeterlinck
COUNT MAURICE MAETERLINCK
Count Maurice Maeterlinck
```

</details>

---

### Assignment 2.5 - Famous Quote

Find a quote from a famous person you admire. Print the quote and the name of
its author. Your output should look something like the following, including
the quotation marks:

```
Albert Einstein once said, "A person who never made a mistake never tried
anything new."
```

<details>
<summary>Spoiler Code</summary>

```python
name = "count maurice maeterlinck"
quote = """At every crossway on the road that leads to the future each \
progressive spirit is opposed by a thousand men appointed to guard the past."""
print(f"{name.title()} wrote:\n\"{quote}\"\n")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Count Maurice Maeterlinck wrote:
"At every crossway on the road that leads to the future each progressive
spirit is opposed by a thousand men appointed to guard the past."
```

</details>

---

### Assignment 2.6 - Famous Quote 2

Repeat Exercise 2-5, but this time represent the famous person's name using a
variable called `famous_person`. Then compose your message and represent it
with a new variable called `message`. Print your message.

<details>
<summary>Spoiler Code</summary>

```python
name = "count maurice maeterlinck"
famous_person = name.title()
quote = """At every crossway on the road that leads to the future each \
progressive spirit is opposed by a thousand men appointed to guard the past."""
message = f"{famous_person} wrote:\n\"{quote}\"\n"
print(message)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Count Maurice Maeterlinck wrote:
"At every crossway on the road that leads to the future each progressive
spirit is opposed by a thousand men appointed to guard the past."
```

</details>

---

### Assignment 2.7 - Stripping Names

Use a variable to represent a person's name, and include some whitespace
characters at the beginning and end of the name. Make sure you use each
character combination, `"\t"` and `"\n"`, at least once. Print the name once,
so the whitespace around the name is displayed. Then print the name using each
of the three stripping functions, `lstrip()`, `rstrip()`, and `strip()`.

<details>
<summary>Spoiler Code</summary>

```python
me = "\n\tScott McLean\t\n"
print(f"[{me}]\n")
print(f"[{me.lstrip()}]\n")
print(f"[{me.rstrip()}]\n")
print(f"[{me.strip()}]\n")
```

</details>
<br>

<details>
<summary>Output</summary>

```
[
        Scott McLean
]

[Scott McLean
]

[
        Scott McLean]

[Scott McLean]
```

</details>

---

### Assignment 2.8 - File Extensions

Python has a `removesuffix()` method that works exactly like `removeprefix()`.
Assign the value `'python_notes.txt'` to a variable called `filename`. Then
use `removesuffix()` to display the filename without the file extension, like
some file browsers do.

> Note: This exercise only appears in the 3rd edition.

<details>
<summary>Spoiler Code</summary>

```python
filename = "python_notes.txt"
print(f"Filename without extension: {filename.removesuffix('.txt')}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Filename without extension: python_notes
```

</details>

---

### Assignment 2.9 - Number Eight

Write addition, subtraction, multiplication, and division operations that each
result in the number 8. Enclose each operation in a `print()` call.

> Note: In the 2nd edition, this is assignment 2.8.

<details>
<summary>Spoiler Code</summary>

```python
print(4 + 4)
print(2 * 4)
print(10 - 2)
print(16 // 2)
```

</details>
<br>

<details>
<summary>Output</summary>

```
8
8
8
8
```

</details>

---

### Assignment 2.10 - Favorite Number

Use a variable to represent your favorite number. Then create a message that
reveals it, and print it.

> Note: In the 2nd edition, this is assignment 2.9.

<details>
<summary>Spoiler Code</summary>

```python
favorite_number = int(6.48074069841 ** 2)
print(f"My favorite number is {favorite_number}!")
```

</details>
<br>

<details>
<summary>Output</summary>

```
My favorite number is 42!
```

</details>

---

### Assignment 2.11 - Adding Comments

Choose two of the programs you've written, and add at least one comment to
each. If you don't have anything specific to write because your programs are
too simple at this point, add your name and the current date at the top of
each file and write one sentence describing what it does.

> Note: In the 2nd edition, this is assignment 2.10.

<details>
<summary>Spoiler Code</summary>

```python
# Here's a comment...
print("You will find comments throughout all my chapter example files.")
```

</details>

---

### Assignment 2.12 - Zen of Python

Enter `import this` into a Python terminal session and skim through the
additional principles.

> Note: In the 2nd edition, this is assignment 2.11.

<details>
<summary>Spoiler Code</summary>

```python
import this
```

</details>

---
