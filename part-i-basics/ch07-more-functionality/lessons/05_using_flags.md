## Using a Boolean Flag

A *flag* is a Boolean variable that records a state, such as "the program is still running." One
common way to end a `while` loop is to use a flag as its condition.

With this pattern, you change the flag when a certain condition is met, and the loop ends at that
point.

```python
prompt = "\nTell me something and I will repeat it back to you:\n> "
message = ""
active = True

while active:
    message = input(prompt)
    if message.lower() == "quit":
        active = False
    else:
        print(message)
else:
    print(f"\nThe loop terminated because the 'active' flag is now '{active}'")
```

Output (the `...` marks the middle of the conversation, which is left out):

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

The loop terminated because the 'active' flag is now 'False'
```

> **About the `else`:** this loop has an `else` block, which we first saw in lesson 5.5. The `else`
> runs only when the loop ends normally, meaning its condition became `False` without a `break`. Here,
> it's there to show the flag at work. Most of the time, you won't need an `else` on a loop.
>
> The `.py` file disables a Pylint warning about this `else`. Pylint is flagging a style issue, not an
> error, and the example is clearer with the `else` left in.

---
