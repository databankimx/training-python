## Getting User Input

One of the most common needs in a program is to get information from the user. Whether it's
login credentials, payment details, or a simple answer to a question, your program needs a way to
accept data from the person running it.

Python gives you the `input()` function for this in terminal applications.

Syntax:

```python
variable = input(prompt)
```

When you call `input()`, it does four things:

1. Displays the prompt you provided to the user
2. Pauses the program until the user presses \<ENTER>
3. Returns a string containing everything the user typed before \<ENTER>
4. Resumes the program

---

### The `input()` Function

Let's start with a simple example, where we print whatever the user types at the prompt:

```python
message = input("Tell me something, and I will repeat it back to you:\n> ")
print(message)
```

User Prompt:

```
Tell me something, and I will repeat it back to you:
> _
```

We'll imagine that the user typed `Hello` + `<ENTER>`

Output After User Interaction:

```
Hello
```

---

### Using User Input

More often, you'll use the input rather than printing it right away.

Here, we'll combine the user's input with a greeting:

```python
name = input("\nPlease enter your name:\n> ")
print(f"\nHello, {name.title()}!")
```

User Prompt:

```
Please enter your name:
> _
```

We'll imagine that the user typed `john` + `<ENTER>`

Output After User Interaction:

```
Hello, John!
```

---

### Multiple Inputs

Since you can store each input in a variable, you can ask for more than one piece of information
before you respond:

```python
prompt = "\nIf you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?\n> "
first_name = input(prompt)
prompt = "\nWhat is your last name?\n> "
last_name = input(prompt)
print(f"Hello, {first_name.title()} {last_name.title()}!")
```

First User Prompt:

```
If you tell us who you are, we can personalize the messages you see.
What is your first name?
> _
```

Let's imagine that the user typed `jane` + `<ENTER>`

Second User Prompt:

```
What is your last name?
> _
```

Let's imagine that the user typed `smith` + `<ENTER>`

Output After User Interaction:

```
Hello, Jane Smith!
```

---

