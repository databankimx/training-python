## Getting User Input

One of the most common requirements in programs is to obtain information from a
user. Whether it's login credentials, payment information, or anything, 
providing a means to allow the user to provide data to the program is a must.

Python exposes the `input()` function to accomplish this in terminal 
applications.

Syntax:

```python
variable = input(prompt)
```

When you use the `input()` function, it performs these tasks:

1. Displays the prompt you provided to the user
2. Suspends the program until the user presses \<ENTER>
3. Returns a string containing everything the user typed before \<ENTER>
4. Resumes the program process

---

### The `input()` Function

Let's look at a simple example, where we simply print whatever the user types
at the prompt:

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

### Using User Input

More commonly, we will use the input data rather than immediately outputting it

Here, we'll combine the user input with a greeting.

```python
name = input("\nPlease enter your name:\n> ")
print(f"\nHello, {name.title()}!")
```

User Prompt:

```
Tell me something, and I will repeat it back to you:
> _ 
```

We'll imagine that the user typed `john` + `<ENTER>`

Output After User Interaction:

```
Hello, John!
```

---

### Multiple Inputs

Obviously, since we can store the user input in a variable, we can perform more
than a single input before responding to the user.

```python
prompt = "If you tell us who you are, we can personalize a message."
prompt += "What is your first name?\n> "
first_name = input(prompt)
prompt = "What is your last name?\n> "
last_name = input(prompt)
print(f"Hello, {first_name.title()} {last_name.title()}!")
```

First User Prompt:

```
If you tell us who you are, we can personalize a message.
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
