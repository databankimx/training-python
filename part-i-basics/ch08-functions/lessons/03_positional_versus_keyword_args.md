## Positional Versus Keyword Arguments

So far, we've only looked at positional arguments. These are unnamed arguments
that must be passed to the function in the order they appear in the function 
signature.

Python also permits passing keyword arguments. These calls include the name of 
the argument and can be passed in any order.

---

### Positional Arguments

Positional arguments must be passed to the function in the order they appear
in the function signature.

So, if we have this function:

```python
def describe_pet(animal_type, pet_name):
    """Print a description of a pet by type and name"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
```

We must pass the arguments to the function in order: `animal_type` and then
`pet_name`.

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

When we pass the arguments as keywords, the order doesn't matter.

Using the same function we defined earlier, we simply include the parameter
names (which must match exactly) in our arguments, and even when we pass them 
out of order...

```python
describe_pet(pet_name="fido", animal_type="dog")
```

Output:

```
I have a dog.
My dog's name is Fido.
```

... the results are as we expected.

---

### All Argument Are Required

By default, every argument is required. If we omit an argument when calling
a function, we will receive a `TypeError`.

```python
describe_pet("fido")
```

Output:

```
Traceback (most recent call last):
  File "...\03_positional_versus_keyword_args.py", line 18, in <module>      
    describe_pet("fido")
TypeError: describe_pet() missing 1 required positional argument: 'pet_name'
```

---

### Functions Don't Always Return Values

You should not make the mistake of assuming that you can capture the results
of a function.

We will discuss how to make a function pass back a value in a couple of
lessons. For now, just note that this will print `None`

```python
message = describe_pet("fish", "bubbles")
print(message)
```

Output:

```
None
```

---
