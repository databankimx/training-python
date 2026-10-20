## Default Parameter Values

So far, we've described all parameters as being required.

While it is strictly true that every parameter must receive a value, it is
possible to make arguments optional by providing default values for them in the
function signature.

Syntax:

```python
def my_function(required_param, optional_param=default_value)
```

There is one restriction: Once a default value is provided for any parameter, 
all parameters coming after it in the function must also receive have default
values.

---

### Skipping Optional Arguments

Consider the following function that includes a default value for the
`animal_type` parameter.

```python
def describe_pet_def(pet_name, animal_type="dog"):
    """Print a description of a pet by type and name"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
```

We can call this function without specifying the argument whose parameter has
a default value:

```python
describe_pet_def("rover")
```

Output:

```
I have a dog.
My dog's name is Rover.
```

---

### Overriding Default Values

Or, we can pass a value in the `animal_type` argument and override the default.

```python
describe_pet_def("pickles", "cat")
```

Output:

```
I have a cat.
My cat's name is Pickles.
```

---

### Risks with Mutable Types

It's important to understand how default values are handled in Python. If
you provide a default value of a mutable type (like a list or dictionary),
you may run into unexpected behavior.

Take a look at bonus lesson 16 
[Mutable Defaults](./16_bonus_mutable_defaults.md) for an explanation of
this behavior.

---
