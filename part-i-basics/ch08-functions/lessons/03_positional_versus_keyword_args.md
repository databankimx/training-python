## Positional Versus Keyword Arguments

So far, we've only looked at positional arguments. These are unnamed arguments that must be passed to
the function in the order they appear in the function signature.

Python also lets you pass keyword arguments. These include the name of the parameter, so they can be
passed in any order.

---

### Positional Arguments

Positional arguments must be passed to the function in the order they appear in the function signature.

So, if we have this function:

```python
def describe_pet(animal_type, pet_name):
    """Print a description of a pet by type and name"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
```

We must pass the arguments in order: `animal_type` first, then `pet_name`.

```python
describe_pet("dog", "fido")
```

Output:

```
I have a dog.
My dog's name is Fido.
```

---

If we pass the arguments in the wrong order, we get undesirable results.

```python
describe_pet("fido", "dog")
```

Output:

```
I have a fido.
My fido's name is Dog.
```

---

### Keyword Arguments

When you pass arguments as keywords, the order doesn't matter. Include the parameter names in your call.
The names are case-sensitive and must match exactly.

Using the same function, we can pass the arguments out of order:

```python
describe_pet(pet_name="fido", animal_type="dog")
```

Output:

```
I have a dog.
My dog's name is Fido.
```

The results are the same as before.

---

### All Arguments Are Required

By default, every argument is required. If you leave one out when calling a function, Python raises
a `TypeError`.

```python
describe_pet("fido")
```

Output (the file name and line number depend on your program):

```
Traceback (most recent call last):
  File "...\03_positional_versus_keyword_args.py", line 18, in <module>
    describe_pet("fido")
TypeError: describe_pet() missing 1 required positional argument: 'pet_name'
```

---

### Functions Don't Always Return a Value

Don't assume that a function gives you something back just because you called it. A function that
doesn't use `return` gives back `None`.

We'll cover how to return a value in a couple of lessons. For now, just notice that this prints `None`:

```python
message = describe_pet("fish", "bubbles")
print(message)
```

Output:

```
None
```

> **About the Pylint comment:** the `.py` file turns off a Pylint warning on that assignment. Pylint
> notices that `describe_pet()` never returns a value, so it flags the assignment. That warning is the
> point of this example, so the comment is there to keep the file clean while the lesson shows the
> `None`.

---
