## Bonus Lesson: The Ternary Logic Expression

Many languages include a ternary operator (e.g. `condition ? value_if_true :
value_if_false` in C# and JavaScript). Python has an equivalent expression
useful for setting a single value based on a condition.

---

### Without a Ternary Expression

```python
user_entry = input("Enter whatever you want:\n> ")
if not user_entry.strip():
    data = "nothing"
else:
    data = user_entry.strip()
print(f"You entered: [{data}]")
```

---

### Using a Ternary Expression

Syntax:

```python
variable = value_if_true if condition else value_if_false
```

The same logic in one line:

```python
data = user_entry.strip() if user_entry.strip() else "nothing"
print(f"You entered: [{data}]")
```

Both approaches produce identical output. The ternary form is concise and
readable when the condition and values are simple. Prefer the full `if`-`else`
block when the logic becomes complex.

---
