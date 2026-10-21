## Bonus Lesson: The Ternary Conditional Expression

Many languages have a *ternary conditional* operator. In C# or JavaScript, for example, it
looks like `condition ? value_if_true : value_if_false`.

It's handy when you want to set a single value based on whether a condition is true.

---

### Without a Ternary Expression

Suppose a user types something, and you want to replace an empty entry, or one that holds only
whitespace, with `"nothing"`. Otherwise, you want to keep what they typed.

Using what we already know, you can write the logic like this:

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
You entered: [nothing]
```

If the user entered `"abc"`:
```
You entered: [abc]
```

---

### Using a Ternary Expression

When you're simply setting a value based on a condition, Python offers a ternary expression.
It has this form:

```python
variable = value_if_true if condition else value_if_false
```

For our example, you can get the same result like this:

```python
data = user_entry.strip() if user_entry.strip() else "nothing"
print(f"You entered: [{data}]")
```

Output:

If the user entered `" "`:
```
You entered: [nothing]
```

If the user entered `"abc"`:
```
You entered: [abc]
```

The ternary reads like a sentence: `data` is the stripped entry if there is one, and `"nothing"`
otherwise. It also takes up fewer lines.

---

### One Line Inside an f-String

You can even put the whole ternary inside the f-string. It's compact, but it's also harder to
read at a glance, so use it sparingly:

```python
print(f"You entered: [{'nothing' if user_entry.strip() == '' else user_entry.strip()}]")
```

---

### A Word of Caution

A ternary is a good fit for a simple, one-time choice. Nesting several of them, or squeezing a
long condition onto one line, quickly turns code into a puzzle. When that happens, go back to an
`if` and `else` block. The next developer will thank you.

---

