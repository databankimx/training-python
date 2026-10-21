## Chapter 4 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 4 try-it-yourself exercises.

---

### Assignment 4.1 - Pizzas

Think of at least three kinds of your favorite pizza. Store these pizza names
in a list, and then use a for loop to print the name of each pizza.

- Modify your for loop to print a sentence using the name of the pizza instead
  of just the name. Each pizza should produce one line like "I like pepperoni pizza."
- Add a line at the end, outside the for loop, that states how much you like pizza.

<details>
<summary>Spoiler Code</summary>

```python
from random import choice

pizzas = ["margherita", "spinach and garlic", "feta and black olive"]
adjectives = ["delicious", "tasty", "scrumptious"]
for pizza in pizzas:
    print(f"I think {pizza} pizza is {choice(adjectives)}!")
print("Pizza is magnificent!")
```

</details>
<br>

> Note: `choice()` picks an adjective at random, so your output will differ from this example.

<details>
<summary>Output</summary>

```
I think margherita pizza is tasty!
I think spinach and garlic pizza is scrumptious!
I think feta and black olive pizza is delicious!
Pizza is magnificent!
```

</details>

---

### Assignment 4.2 - Animals

Think of at least three different animals that have a common characteristic.
Store the names in a list, print each animal, and add a statement about what
they have in common.

<details>
<summary>Spoiler Code</summary>

```python
from random import choice

animals = ["octopus", "squid", "cuttlefish"]
verbs = ["eat", "devour", "dine on"]
for animal in animals:
    print(f"I like to {choice(verbs)} {animal}.")
print("You have to be very careful cooking any of these animals.")
```

</details>
<br>

> Note: `choice()` picks a verb at random, so your output will differ from this example.

<details>
<summary>Output</summary>

```
I like to devour octopus.
I like to dine on squid.
I like to eat cuttlefish.
You have to be very careful cooking any of these animals.
```

</details>

---

### Assignment 4.3 - Counting to Twenty

Use a for loop to print the numbers from 1 to 20, inclusive.

<details>
<summary>Spoiler Code</summary>

```python
for num in range(1, 21):
    print(num)
```

</details>

---

### Assignment 4.4 - One Million

Make a list of the numbers from one to one million, and then use a for loop to
print the numbers. (If the output is taking too long, stop it by pressing
`CTRL`+`C`.)

> Note: the `.py` file prints only the first and last five numbers, so the terminal stays readable. The full loop is in the file as a commented-out block.

<details>
<summary>Spoiler Code</summary>

```python
million = list(range(1, 1_000_001))
for num in million:
    print(num)
```

</details>

---

### Assignment 4.5 - Summing a Million

Make a list of the numbers from one to one million, and then use `min()`,
`max()`, and `sum()` to verify the list and see how quickly Python can add a
million numbers.

<details>
<summary>Spoiler Code</summary>

```python
million = list(range(1, 1_000_001))
print(min(million))
print(max(million))
print(sum(million))
```

</details>
<br>

<details>
<summary>Output</summary>

```
1
1000000
500000500000
```

</details>

---

### Assignment 4.6 - Odd Numbers

Use the third argument of `range()` to make a list of the odd numbers from 1
to 20. Use a for loop to print each number.

<details>
<summary>Spoiler Code</summary>

```python
nums = list(range(1, 21, 2))
for num in nums:
    print(num)
```

</details>
<br>

<details>
<summary>Output</summary>

```
1
3
5
7
9
11
13
15
17
19
```

</details>

---

### Assignment 4.7 - Threes

Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the
numbers in your list.

<details>
<summary>Spoiler Code</summary>

```python
nums = list(range(3, 31, 3))
for num in nums:
    print(num)
```

</details>
<br>

<details>
<summary>Output</summary>

```
3
6
9
12
15
18
21
24
27
30
```

</details>

---

### Assignment 4.8 - Cubes

Make a list of the first 10 cubes using a for loop, then print each cube.

<details>
<summary>Spoiler Code</summary>

```python
cubes = []
for num in range(1, 11):
    cubes.append(num ** 3)
for num in cubes:
    print(num)
```

</details>
<br>

<details>
<summary>Output</summary>

```
1
8
27
64
125
216
343
512
729
1000
```

</details>

---

### Assignment 4.9 - Cube Comprehension

Use a list comprehension to generate a list of the first 10 cubes.

<details>
<summary>Spoiler Code</summary>

```python
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
```

</details>
<br>

<details>
<summary>Output</summary>

```
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

</details>

---

### Assignment 4.10 - Slices

Using one of the programs you wrote in this chapter, add lines that print the
first three items, three items from the middle, and the last three items.

<details>
<summary>Spoiler Code</summary>

```python
odd_numbers = list(range(1, 21, 2))
print(f"The first three odd numbers are: {odd_numbers[:3]}")
print(f"The next three odd numbers are: {odd_numbers[3:6]}")
print(f"The last three odd numbers are: {odd_numbers[-3:]}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
The first three odd numbers are: [1, 3, 5]
The next three odd numbers are: [7, 9, 11]
The last three odd numbers are: [15, 17, 19]
```

</details>

---

### Assignment 4.11 - My Pizzas, Your Pizzas

Start with your program from Exercise 4-1. Make a copy of the list called
`friend_pizzas`, add a different pizza to each list, and prove they are
separate by printing both with for loops.

<details>
<summary>Spoiler Code</summary>

```python
my_pizzas = ["margherita", "spinach and garlic", "feta and black olive"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("pepperoni")
friend_pizzas.append("sausage and green pepper")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f" - {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f" - {pizza}")
```

</details>

---

### Assignment 4.12 - More Loops

Choose a version of `foods.py` and write two for loops to print each list of
foods.

<details>
<summary>Spoiler Code</summary>

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for food in my_foods:
    print(f" - {food}")
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f" - {food}")
```

</details>

---

### Assignment 4.13 - Buffet

Think of five simple foods and store them in a tuple.

- Use a for loop to print each food.
- Try to modify one item and confirm Python rejects it.
- Replace the tuple with a new one and print the updated menu.

<details>
<summary>Spoiler Code</summary>

```python
menu = ("sandwich", "pastry", "coffee", "tea", "bagel")
print("Menu:")
for food in menu:
    print(f" - {food}")

# menu[0] = "toast"  # Uncomment to see TypeError

menu = ("toast", "pastry", "coffee", "tea", "yogurt")
print("Updated Menu:")
for food in menu:
    print(f" - {food}")
```

</details>

---

### Assignment 4.14 - PEP 8

Look through the PEP 8 style guide at
[https://peps.python.org/pep-0008](https://peps.python.org/pep-0008).

<details>
<summary>Spoiler Code</summary>

```python
# This is a research task - no code needed.
```

</details>

---

### Assignment 4.15 - Code Review

Choose three programs from this chapter and modify each to comply with PEP 8.

**To set tab size to 4 spaces in VS Code** (already the default):

1. Press `CTRL`+`SHIFT`+`P`
2. Search for `settings` and select `Preferences: Open Settings (UI)`
3. Search for `tab size` and confirm `Editor: Tab Size` is `4`

**To set a column ruler at 120 characters:**

1. Press `CTRL`+`SHIFT`+`P`
2. Search for `settings` and select `Preferences: Open User Settings (JSON)`
3. Add a comma after the last entry inside the curly braces, then add:
   `"editor.rulers": [120]`

You can add multiple rulers: `"editor.rulers": [80, 120]`

<details>
<summary>Spoiler Code</summary>

```python
# Do this one on your own.
```

</details>

---
