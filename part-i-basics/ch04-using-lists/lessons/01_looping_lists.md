## Looping over Lists

If we look back at assignment 3.6, we spent a lot of time repeatedly printing
the members of a list, one at a time. That's really awful, and it violates the
principle of not writing redundant code.

Wouldn't it be neat if we had a way to look at all the items in a list and
repeat an instruction on each one?

Well, I have some good news for you!

---

### Iterating Lists with `for`

In Python a `for` loop is like a "foreach" loop in C#. The loop iterates over
the list, capturing each element and performing some task(s) with it.

```python
for item in collection:
    # Code to perform on each item
```

A line ending in a colon indicates the start of a block of indented lines.

> **Indentation rules:**
> - The indentation must be consistent throughout the file (four spaces, not tabs)
> - Only indent inside a block
> - If a block contains another block, indent again inside the inner block

---

### Examples

#### A simple loop with one statement in the block

```python
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)
```

Output:

```
alice
david
carolina
```

---

#### Multiple statements in the block

The code block can contain multiple instructions. A non-indented line
following the loop executes after the loop completes.

```python
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next one.\n")
print("That was a great magic show!\n")
```

Output:

```
Alice, that was a great trick!
I can't wait to see your next one.

David, that was a great trick!
I can't wait to see your next one.

Carolina, that was a great trick!
I can't wait to see your next one.

That was a great magic show!
```

---

### Be Careful Indenting

One logic error you ***will*** make at some point is incorrectly indenting inside a loop.

#### Indenting a line that should not be indented

```python
for i in range(3, 0, -1):
    print(i)
    print("Blast off!")
```

Output:

```
3
Blast off!
2
Blast off!
1
Blast off!
```

The `print("Blast off!")` ran on every iteration. What was intended:

```python
for i in range(3, 0, -1):
    print(i)
print("Blast off!")
```

Output:

```
3
2
1
Blast off!
```

---

#### Not indenting a line that should be indented

```python
for i in range(3, 0, -1):
    message = f"{i}..."
print(message)
print("Blast off!")
```

Output:

```
1...
Blast off!
```

The message only printed once, after the loop ended. What was intended:

```python
for i in range(3, 0, -1):
    message = f"{i}..."
    print(message)
print("Blast off!")
```

Output:

```
3...
2...
1...
Blast off!
```

---
