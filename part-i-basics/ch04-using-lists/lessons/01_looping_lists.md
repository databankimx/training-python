## Looping over Lists

Back in exercise 3.6, the guest list, we printed each guest on their own line,
one `print()` after another. It worked, but it was tedious, and it broke a basic rule
of good code: don't repeat yourself.

Wouldn't it be nice to look at every item in a list and run the same instructions
on each one? Good news. You can.

### Looping with `for`

In Python, a `for` loop works a lot like a "foreach" loop in C#. The loop goes through
the list one item at a time, and for each item it runs the code inside the loop:

```python
for item in collection:
    # Code to run on each item
```

That line ends with a colon. In Python, a colon means "a block of code starts here,"
and the lines that belong to the block are indented below it.

> **About indenting:** Indentation is how Python knows which lines belong together, so
> it matters more than it looks.
>
> * Keep the indentation consistent within a block. Four spaces, every time.
> * Mixing tabs and spaces causes an error in Python 3 when the indentation doesn't
>   line up, even if it looks right on screen.
> * Indent only inside a block.
> * When a block sits inside another block, each level gets one more indent. Indent
>   once for the outer block, and once more for the inner one.

---

### Examples

#### A simple loop with one statement in the block

```python
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    # The indented line runs on each loop iteration
    print(magician)
```

Output:

```
alice
david
carolina
```

---

#### A more thorough example

A loop's block can hold as many statements as you need.

A line that isn't indented runs once, after the loop finishes:

```python
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    # The indented lines run on each loop iteration
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next one.\n")
# This line isn't indented, so it runs after the loop is complete
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

### Be Careful with Indenting

Incorrect indentation is one of the most common mistakes in a loop, and Python
won't always tell you about it. It just does what you wrote.

#### Indenting a line that shouldn't be indented

If you indent a line in a loop's block, that line runs on every iteration, whether
you wanted it to or not. The example below uses `range()`, which produces a sequence
of numbers. We'll cover it properly in the next lesson, so for now, just know that
`range(3, 0, -1)` counts down from 3 to 1:

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

We indented the second `print()`, so it ran on every iteration. What we meant was
this:

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

The opposite mistake is just as easy. If a line should run on every iteration but
isn't indented, it runs once, after the loop ends:

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

The `message` line wasn't indented, so it ran after the loop, and only the last value
survived. What we meant was this:

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

