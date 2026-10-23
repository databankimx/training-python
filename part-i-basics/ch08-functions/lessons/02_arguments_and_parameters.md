## Function Arguments and Parameters

Functions are great for avoiding repeated code, but they're not very useful unless they can work with
different data each time they run, instead of always doing the same thing.

That's where parameters and arguments come in.

When you define a function, you can specify **parameters**, the values the function expects to
receive when it's called:
`def my_function(my_parameter, ...)`

When you call a function, you supply **arguments** that fill in those parameters:
`my_function(my_argument, ...)`

People often use the two terms interchangeably, but in technical terms:

* **Parameters** are defined in the function signature
* **Arguments** are the actual values passed when the function is called

---

### A Function with a Parameter

Using this idea, we can rewrite our earlier example so the function accepts a `name` parameter. Now
we can call the function with different `name` arguments and get different results.

```python
def greet_named_user(name):
    """Print a greeting to the user passed to the function"""
    print(f"Hello, {name.title()}")

greet_named_user("abe")
greet_named_user("betty")
greet_named_user("carlos")
```

Output:

```
Hello, Abe
Hello, Betty
Hello, Carlos
```

---

### List as a Parameter

A parameter can be a list, not just a single value.

```python
def greet_users(names):
    """Print a greeting to each of the users passed to the function"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ["hannah", "ty", "margot"]
greet_users(usernames)
```

Output:

```
Hello, Hannah!
Hello, Ty!
Hello, Margot!
```

---

### Multiple Parameters

A function can take more than one parameter. In the function definition, and in the function call,
the parameters and arguments are separated by commas `,`.

```python
def greet_full_name(first_name, last_name):
    """Print a greeting to the user passed to the function"""
    print(f"\nHello, {first_name.title()} {last_name.title()}")

greet_full_name("charles", "babbage")
```

Output:

```
Hello, Charles Babbage
```

---
