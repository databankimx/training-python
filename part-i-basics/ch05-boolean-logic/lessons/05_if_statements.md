## Using `if` Statements

So far, we've only looked at `if` statements where we check a single 
condition. We can extend that functionality to be able to handle situations
where there are several conditions to be checked, each with its own logical branch.

---

### One `if` Condition

With just a single `if` statement, we can perform some operation(s) when the
condition is `True`.

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

As we looked at before, we can also use the `else` statement to indicate some
operation(s) to perform when the condition is `False`

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

We can handle the situation where a condition is `False` but some other
condition is `True` using an `elif` (`else` + `if`) block:

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

When the code executed, it found that the condition `age < 4` was `False`,
so it did not perform the operations in the `if` block.

Since that was `False`, the `else` condition of the `elif` is met, so the
code evaluates the condition `age < 18` as though it was an `if`. This condition is `True`, so the entire `elif` is `True`, and we perform the
operations in its block.

Because that condition was already `True`, we don't meet the conditions
for the `else` block, so the process is complete. When there are `elif`
conditions being evaluated, `else` means "no prior condition was `True`."

---

### Separating the `print` Operation

As we'll learn later (when we get to functions), it's usually better to
stash a value that indicates the result of the condition blocks and then
use it later. A smart way to handle this would be to only print after all 
conditions are evaluated.

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

---

### Multiple `elif` Blocks

You can include as many `elif` blocks between the `if` and `else` as
desired, in order to handle many different conditions.

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

---

### `else` is Optional

Even with `elif` blocks, the `else` block is not required.

One standard coding pattern that doesn't use an `else` block looks like
this:

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

At the end, if no conditions are met, the variable still contains the original 
default value, so we can simplify the previous example like this:

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

When you need to check another condition regardless of other results, use another `if`, not `elif`

Mixing this up is one of the most common errors new programmers make.

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

### Bonus - Using `else` with a Loop

Although uncommonly used, you can append an `else` block to the end of a loop.

The `else` block will execute when the loop finishes, either when the loop
condition becomes `False` (in a `while` loop) or when the range is exhausted
(in a `for` loop).

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

---
