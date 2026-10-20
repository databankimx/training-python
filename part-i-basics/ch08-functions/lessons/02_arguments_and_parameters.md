## Function Arguments and Parameters

It's great to have functions that avoid code redundancy, but they're not 
really useful unless we can make them handle situational data as opposed to
just executing.

That's where function parameters and arguments come in.

When you define a function, you can specify **parameters** that the function
expects to receive when it is called:  
`def my_function(my_parameter, ...)`

When you call a function, you add **arguments** to the call to fulfill the
function's parameter expectations:  
`my_function(my_argument, ...)`

You will often hear these two terms used interchangeably, but in technical
terms:

* **Parameters** are defined in the function signature
* **Arguments** are the actual values passed when calling the function

---

### A Function with a Parameter

Using this principle, we can redefine our previous example so that it
accepts a `name` parameter. This allows us to call the function and
pass different `name` arguments to get different results.

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

A parameter can be a list, not just a single variable.

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

You can pass multiple parameters to the function. The parameters in the
function definition (and the arguments in the function call) are separated by
commas `,`.

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
