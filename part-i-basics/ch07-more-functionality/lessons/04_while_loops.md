## `while` Loops

Unlike the `for` loop, a `while` loop does not require an incrementing value
or range. Instead, the loop continues iterating as long as the condition associated with it remains true.

Syntax:

```python
while some_condition:
    # Perform tasks
```

---

### Make Sure To Avoid Infinite Loops

Because the `while` loop executes as long as its condition is `True`, it is
important to ensure that your code provides a mechanism to eventually make the
condition `False`.

> As your code gets more complex, it becomes increasingly more difficult to
> identify possible infinite loops. You should assume that sooner or later
> you **will** create one.
>
> To escape from an infinite loop, place the cursor in the terminal pane and
> type `CTRL`+`C` to terminate the program.

In this example, a counter is incremented in each iteration. This ensures that
the condition `count < 5` will eventually become `False`

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

---

### Integers Behave Like Booleans

Since the integer value `0` behaves like `False` when evaluated as a condition,
we can omit the `== 0` comparison operator when a zero value ends the loop.

```python
count = 5
while count:
    count -= 1
    print(count)
```

Output:

```
4
3
2
1
0
```

---

### Non-Numeric Conditions

Since the condition governing the `while` loop is any expression that resolves 
to a Boolean (or Boolean-like) value, there is no requirement for the condition
to be numeric.

Here, we'll iterate a loop until the user enters the value `quit`.

```python
prompt = "\nTell me something and I will repeat it back to you:\n> "
message = ""
while message.lower() != "quit":
    message = input(prompt)
    print(message)
```

Output:

```
Tell me something and I will repeat it back to you:
> message 1
message 1

Tell me something and I will repeat it back to you:
> message 2
message 2

...

Tell me something and I will repeat it back to you:
> quit
quit
```

---

### Modifying a List While in a Loop

You may recall, way back in Lesson 4.1, we discussed the problem with 
modifying an object we're looping across using `for`.

With a while loop, since we are no longer iterating across the list, but 
instead checking a condition, we can accomplish what we were trying to do in 
that loop.

We're going to take advantage of the fact that, like `0` above, and empty list
is a *falsy* value (evaluates as `False` in a conditional). 

```python
numbers = [1, 2, 3, 4, 5]
print(numbers)
while numbers:
    n = numbers.pop(0)
    print(n)
print(numbers)
```

Output:

```
[1, 2, 3, 4, 5]
1
2
3
4
5
[]
```

---
