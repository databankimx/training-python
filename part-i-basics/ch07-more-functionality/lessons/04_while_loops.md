## `while` Loops

Unlike a `for` loop, a `while` loop doesn't need an incrementing value or a range. Instead, it keeps
going for as long as its condition remains `True`.

Syntax:

```python
while some_condition:
    # Perform tasks
```

---

### Make Sure to Avoid Infinite Loops

Because a `while` loop runs as long as its condition is `True`, your code has to provide a way to
make that condition `False`, or the loop never ends.

> As your code gets more complex, it becomes harder to spot possible infinite loops. Assume that
> sooner or later, you **will** create one.
>
> To escape from an infinite loop, click in the terminal pane and press `CTRL`+`C` to stop the
> program.

In this example, a counter goes up in each iteration. That makes the condition `count <= 5` eventually
`False`:

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

Since the integer `0` behaves like `False` when it's evaluated as a condition, you can leave out the
`== 0` comparison when a zero value should end the loop.

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

A `while` condition can be any expression that resolves to a Boolean (or Boolean-like) value. It
doesn't have to be numeric.

Here, we'll keep the loop going until the user enters the word `quit`.

```python
prompt = "\nTell me something and I will repeat it back to you:\n> "
message = ""
while message.lower() != "quit":
    message = input(prompt)
    print(message)
```

Output (the loop continues for each message, and the output below shows the first and last exchanges):

```
Tell me something and I will repeat it back to you:
> message 1
message 1

Tell me something and I will repeat it back to you:
> message 2
message 2

(the loop continues with more messages)

Tell me something and I will repeat it back to you:
> quit
quit
```

---

### Modifying a List While in a Loop

Back in lesson 4.3, we saw the problem with changing a list while looping over it with `for`.

A `while` loop doesn't iterate over the list. It checks a condition instead, so we can do the job we
were attempting in that earlier loop.

This works because an empty list is a *falsy* value, just like the `0` above. It evaluates as `False`
in a condition.

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

