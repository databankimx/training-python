## Default Parameter Values

So far, we've treated every parameter as required.

It's true that every parameter has to receive a value. But you can make an argument optional by giving
its parameter a default value in the function signature.

Syntax:

```python
def my_function(required_param, optional_param=default_value):
```

There's one restriction. Once a parameter has a default value, every parameter after it must also have
a default value.

---

### Skipping Optional Arguments

Consider this function, which gives the `animal_type` parameter a default value.

```python
def describe_pet_def(pet_name, animal_type="dog"):
    """Print a description of a pet by type and name"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
```

You can call this function without the argument whose parameter has a default value:

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

You can also pass a value for `animal_type`, which overrides the default.

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

It's important to understand how Python handles default values. If you give a parameter a default value
of a mutable type, such as a list or a dictionary, you can run into unexpected behavior.

See bonus lesson 16, [Mutable Defaults](./16_bonus_mutable_defaults.md), for an explanation of this
behavior.

---

