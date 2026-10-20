## Bonus Lesson: The Ternary Logic Expression

Many languages include a ternary logic operator. For example, in C# or 
JavaScript, we have the `condition ? value_if_true : value_if_false` operator.

This can be useful if you want to set a single value depending on whether or
not some condition is true.

---

### Without a Ternary Expression

Consider the scenario where we want to evaluate the data entered by a user.

If the user enters an empty string or a string containing only whitespace, we
want to swap that with `"nothing"`. Otherwise we want to work with the user's 
input.

Using our existing knowledge, we can construct the logic like this:

```python
user_entry = input("Enter whatever you want:\n> ")
if not user_entry.strip(): # Same as `if user_entry.strip() == ""`
    data = "nothing"
else:
    data = user_entry.strip()
print(f"You entered: [{data}]")
```

Output:

If the user entered `" "`:
```
You entered [nothing]
```

If the user entered `"abc"`:
```
You entered [abc]
```

---

### Using a Ternary Expression

For this kind of scenario, where we are simply setting a value based on a
condition, Python provides a ternary expression structured like this:

```python
variable = value_if_true if condition else value_if_false
```

So, for our example, we can do something like this and obtain the same
result:

```python
data = user_entry.strip() if user_entry.strip() else "nothing"
print(f"You entered: [{data}]")
```

Output:

If the user entered `" "`:
```
You entered [nothing]
```

If the user entered `"abc"`:
```
You entered [abc]
```

---
