## Using a Loop to Populate a Dictionary

We've looked at using a loop to populate a list. It stands to reason that we
can use a similar technique to populate a dictionary.

```python
responses = {}

while True:
    name = input("\nWhat is your name?\n> ")
    mountain = input("Which mountain would you like to climb someday?\n> ")
    
    responses[name] = mountain
    
    repeat = input("Would you like to let another person respond? (yes/no)\n> ").lower()[0]
    if repeat == "n":
        break
        
print("\n--- Poll Results ---")
for name, mountain in responses.items():
    print(f"{name.title()} would like to climb {mountain.title()}.")
```

Output:

```
What is your name?
> linda
Which mountain would you like to climb someday?
> mount everest
Would you like to let another person respond? (yes/no)
> y

What is your name?
> phil
Which mountain would you like to climb someday?
> mount kilimanjaro
Would you like to let another person respond? (yes/no)
> n

--- Poll Results ---
Linda would like to climb Mount Everest.
Phil would like to climb Mount Kilimanjaro.
```

---
