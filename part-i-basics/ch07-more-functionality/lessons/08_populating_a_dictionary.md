## Using a Loop to Populate a Dictionary

We've used a loop to populate a list. It makes sense that we can use the same idea to populate a
dictionary.

```python
responses = {}

while True:
    name = input("\nWhat is your name?\n> ")
    mountain = input("Which mountain would you like to climb someday?\n> ")

    responses[name] = mountain

    repeat = input("Would you like to let another person respond? (yes/no)\n> ").strip().lower()
    if repeat == "n" or repeat == "no":
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

The loop stops only when the answer is `n` or `no`. Any other answer, including an empty one, keeps the
poll going. Stripping spaces and lowercasing first means `  N  ` and `No` also count.

> **A note on names:** each name is a dictionary key, and keys are unique. If two people enter the same
> name, the second answer replaces the first. We saw that in lesson 6.1.

---

