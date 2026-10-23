## Using `if` Statements

So far, we've only looked at `if` statements that check a single condition. Now we'll
handle situations where several conditions need checking, and each one leads to its own
branch of code.

---

### One `if` Condition

With a single `if` statement, we can run one or more operations when the condition is `True`.

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

Output:

```
You are old enough to vote!
Have you registered to vote yet?
```

---

### Handling the `False` Case with `else`

As we saw before, the `else` statement runs its operations when the condition is `False`:

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

Output:

```
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```

---

### Handling More Conditions with `elif`

When the first condition is `False`, but another condition might be `True`, use an `elif`
(short for `else` + `if`) block:

```python
age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")
```

Output:

```
Your admission cost is $25
```

Python checks the conditions from the top, one at a time:

1. `age < 4` is `False` for 12, so Python skips the `if` block.
2. `age < 18` is `True`, so Python runs the `elif` block and prints `$25`.
3. Because a condition was already `True`, Python skips the `else` block.

The rule to remember is that `else` means "none of the conditions before it were `True`."
Once one branch runs, Python skips the rest of the chain.

---

### Separating the `print` Operation

It's usually cleaner to decide on a value first, and print it once, after the decision is
made:

```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}")
```

Output:

```
Your admission cost is $25
```

Now the decision lives in one place, and the printing happens in one place. If the price rules
change, you only have to change the decision.

---

### Multiple `elif` Blocks

You can have as many `elif` blocks as you need between the `if` and the `else`:

```python
age = 20
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}")
```

Output:

```
Your admission cost is $40
```

Order matters here. Python runs the first branch whose condition is `True`, and it ignores
the rest. If you put `age < 65` above `age < 18`, a child would get the adult price.

---

### `else` Is Optional

The `else` block is optional, even when you use `elif`.

A common pattern is to set a default value first, and then let the conditions change it
only when they need to. The placeholders below stand in for real values:

```python
some_variable = default_value
if condition_1:
    some_variable = value_1
elif condition_2:
    some_variable = value_2
...
elif condition_n:
    some_variable = value_n
```

If no condition matches, the variable keeps its default value. That lets you simplify the
admission example, because the default does the job of the `else`:

```python
age = 70
price = 20 # Default value instead of using `else`
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
print(f"Your admission cost is ${price}\n")
```

Output:

```
Your admission cost is $20
```

---

### Checking Independent Conditions

If you need to check a condition no matter what the earlier conditions found, use another
`if`, not an `elif`.

Using `elif` where you meant `if` is a common mistake. With `elif`, only the first match
runs. With separate `if` statements, each one gets its own check:

```python
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms...")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni...")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese...")
print("Finished making your pizza!")
```

Output:

```
Adding mushrooms...
Adding extra cheese...
Finished making your pizza!
```

---

### Bonus: Using `else` with a Loop

It's uncommon, but a loop can have an `else` block too. The `else` runs when the loop finishes
normally. For a `while` loop, that means the condition became `False`. For a `for` loop, it
means the range ran out.

```python
i = 0
while i < 5:
    i += 1
    print(i)
else:
    print("If this ran, i must be 5 or more.\n")

for i in range(1, 6):
    print(i)
else:
    print("This ran when I exhausted the range.")
```

Output:

```
1
2
3
4
5
If this ran, i must be 5 or more.

1
2
3
4
5
This ran when I exhausted the range.
```

The `else` doesn't run if the loop stops early because of a `break`:

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("This won't print, because the loop stopped at 3.")
```

Output:

```
1
2
```

---
