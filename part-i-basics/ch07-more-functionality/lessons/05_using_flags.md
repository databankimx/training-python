## Using a Boolean Flag

One of the common patterns to terminate a `while` loop is to use a Boolean
variable as a flag and assign it as the condition for the loop.

With this pattern, you change the state of the flag when certain conditions are
met, and the loop terminates only at that point.

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

The loop terminated because the 'active' flag is now 'False'
```

---
