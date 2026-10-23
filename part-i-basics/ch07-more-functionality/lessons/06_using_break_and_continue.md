## Using `break` and `continue`

Sometimes you need to end one iteration of a loop, or the entire loop, when a certain condition
occurs.

Python provides the `break` and `continue` statements, which give you precise control over what
happens inside a loop.

* The `break` statement ends the loop immediately
    * The rest of the current iteration doesn't run
    * No more iterations run
* The `continue` statement ends the current iteration immediately
    * The rest of the current iteration doesn't run
    * The loop itself carries on with the next iteration

Both statements also work in `for` loops.

---

### Terminating a Loop with `break`

A common pattern is to start a loop with a constant condition: `True`.

A loop like this is infinite by design, because its condition never becomes `False`.

To make sure the loop eventually ends, identify the condition that should stop it, and use a
`break` statement when that condition is met:

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)\n> "

while True:
    city = input(prompt)
    if city.lower() == "quit":
        break # End when the user enters `quit`
    else:
        print(f"I'd love to go to {city.title()}!")
```

Output (the `...` stands for the rest of the conversation, which is left out):

```
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.)
> city a
I'd love to go to City A!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.)
> city b
I'd love to go to City B!

...

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.)
> quit
```

---

### Terminating an Iteration with `continue`

Sometimes you need to step through a collection, but you only want certain steps to run when a
condition is met.

The `continue` statement skips the rest of the current iteration and moves on to the next one:

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # Skip even numbers
    print(current_number)
```

Output:

```
1
3
5
7
9
```

> **Watch out for `continue` in a `while` loop:** the `continue` skips everything after it in the
> same iteration. If the line that changes the loop's condition comes after the `continue`, the
> loop never reaches it, and the loop never ends. The example above increments `current_number`
> before the `continue`, which is why it stops at 10.
>
> ```python
> current_number = 0
> while current_number < 10:
>     if current_number % 2 == 0:
>         continue  # Infinite loop: the increment below is never reached for even numbers
>     current_number += 1
>     print(current_number)
> ```
>
> Put the update before any `continue`, or make sure it runs on every path through the loop.

---
