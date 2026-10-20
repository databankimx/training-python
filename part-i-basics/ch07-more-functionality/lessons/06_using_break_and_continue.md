## Using `break` and `continue`

Sometimes it's necessary to end either one iteration of the loop or the entire
loop itself when some condition occurs.

Python provides the `break` and `continue` statements to give the programmer
control over precisely what happens in the loop.

* The `break` command immediately ends the loop
    * The remainder of the current iteration does not execute
    * No more iterations execute
* The `continue` command immediately ends the current iteration of the loop
    * The remainder of the current iteration does not execute
    * But the loop itself continues with the next iteration

---

### Terminating a Loop with `break`

One very common programming pattern is to establish a loop with a constant
condition: `True`.

This sort of loop is inherently infinite. The condition will never become
`False`, because it's constant.

In order to ensure that the loop eventually terminates, the programmer must
identify one or more conditions where this should occur and implement the
`break` statement to end the loop.

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

Output:

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

One common programming scenario is where you need to iterate across some
collection of values, but you only want certain steps to be performed when a
given condition is met.

The `continue` statement allows the programmer to skip the remainder of the
iteration following the `continue` command but pick back up with the next
iteration of the loop.

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

---
