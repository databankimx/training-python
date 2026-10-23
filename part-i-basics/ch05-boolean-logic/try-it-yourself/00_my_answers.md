## Chapter 5 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 5 try-it-yourself exercises.

---

### Assignment 5.1 - Conditional Tests

Write a series of conditional tests. Print a statement describing each test
and your prediction for the results of each test. Create at least ten tests -
five True, five False.

<details>
<summary>Spoiler Code</summary>

```python
make = "Dodge"
model = "Challenger"
print("Is make == 'fiat'? I predict False.")
print(make == "fiat")
print("Is make == 'dodge'? I predict False.")
print(make == "dodge")
print("Is make == 'Dodge'? I predict True.")
print(make == "Dodge")
print("Is case-insensitive make == 'dodge'? I predict True.")
print(make.lower() == "dodge")
print("Is model == 'charger'? I predict False.")
print(model == "charger")
print("Is model != 'charger'? I predict True.")
print(model != "charger")
print("Is model == 'challenger'? I predict False.")
print(model == "challenger")
print("Is model == 'Challenger'? I predict True.")
print(model == "Challenger")
print("Is case-insensitive model == 'charger'? I predict False.")
print(model.lower() == "charger")
print("Is case-insensitive model == 'challenger'? I predict True.")
print(model.lower() == "challenger")
```

</details>

---

### Assignment 5.2 - More Conditional Tests

At least one True and one False for each: string equality/inequality, `lower()`,
numerical comparisons, `and`/`or`, `in`, `not in`.

<details>
<summary>Spoiler Code</summary>

```python
make = "Dodge"
model = "Challenger"
year = 2014

print(make == "fiat")         # False
print(make != "fiat")         # True
print(make.lower() == "fiat") # False
print(make.lower() == "dodge") # True

print(year == 2014)   # True
print(year == 2020)   # False
print(year != 2020)   # True
print(year > 2020)    # False
print(year >= 2020)   # False
print(year < 2020)    # True
print(year <= 2020)   # True

print(make.lower() == "dodge" and model.lower() == "challenger") # True
print(make.lower() == "dodge" and model.lower() == "charger")   # False
print(make.lower() == "dodge" or model.lower() == "charger")    # True
print(make.lower() == "fiat" or model.lower() == "spider")      # False

stats = [2014, "dodge", "challenger"]
print("fiat" in stats)           # False
print("dodge" in stats)          # True
print("charger" not in stats)    # True
print("challenger" not in stats) # False
```

</details>

---

### Assignment 5.3 - Alien Colors #1

Create `alien_color` with a value of `green`, `yellow`, or `red`. Write an
`if` statement that prints a message if green. Write one version that passes
and one that fails.

<details>
<summary>Spoiler Code</summary>

```python
alien_color = "red"
if alien_color == "green":
    print("You earned 5 points!")   # Does not print

alien_color = "green"
if alien_color == "green":
    print("You earned 10 points!")  # Prints
```

</details>
<br>

<details>
<summary>Output</summary>

```
You earned 10 points!
```

</details>

---

### Assignment 5.4 - Alien Colors #2

Write an `if`-`else` chain. Green: 5 points. Not green: 10 points. Write one
version running the `if` block and one running `else`.

<details>
<summary>Spoiler Code</summary>

```python
alien_color = "red"
if alien_color == "green":
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

alien_color = "green"
if alien_color == "green":
    print("You earned 5 points!")
else:
    print("You earned 10 points!")
```

</details>
<br>

<details>
<summary>Output</summary>

```
You earned 10 points!
You earned 5 points!
```

</details>

---

### Assignment 5.5 - Alien Colors #3

Turn the `if`-`else` into an `if`-`elif`-`else` chain. Green: 5 pts. Yellow:
10 pts. Red: 15 pts. Write three versions.

One loop handles all three colors, so the single loop below covers all three versions.

<details>
<summary>Spoiler Code</summary>

```python
alien_colors = ["green", "yellow", "red"]
for alien_color in alien_colors:
    if alien_color == "green":
        points = 5
    elif alien_color == "yellow":
        points = 10
    elif alien_color == "red":
        points = 15
    else:
        points = 0
    print(f"You earned {points} points!")
```

</details>
<br>

<details>
<summary>Output</summary>

```
You earned 5 points!
You earned 10 points!
You earned 15 points!
```

</details>

---

### Assignment 5.6 - Stages of Life

Write an `if`-`elif`-`else` chain that determines a person's stage of life.
`< 2`: baby | `2-3`: toddler | `4-12`: kid | `13-19`: teenager |
`20-64`: adult | `65+`: elder.

<details>
<summary>Spoiler Code</summary>

```python
age = int(input("Enter your age: "))
if age < 2:
    print("You are a baby!")
elif age < 4:
    print("You are a toddler!")
elif age < 13:
    print("You are a kid!")
elif age < 20:
    print("You are a teenager!")
elif age < 65:
    print("You are an adult!")
else:
    print("You are an elder!")
```

</details>

---

### Assignment 5.7 - Favorite Fruit

Make a list of favorite fruits. Write five independent `if` statements checking
for certain fruits.

<details>
<summary>Spoiler Code</summary>

```python
favorite_fruits = ["grapefruit", "key lime", "apple", "blackberry"]
fruit = "peach"
if fruit in favorite_fruits:
    print(f"{fruit} is one of your favorites")
fruit = "apple"
if fruit in favorite_fruits:
    print(f"{fruit} is one of your favorites")
fruit = "guava"
if fruit in favorite_fruits:
    print(f"{fruit} is one of your favorites")
fruit = "blackberry"
if fruit in favorite_fruits:
    print(f"{fruit} is one of your favorites")
fruit = "grapefruit"
if fruit in favorite_fruits:
    print(f"{fruit} is one of your favorites")
```

</details>
<br>

<details>
<summary>Output</summary>

```
apple is one of your favorites
blackberry is one of your favorites
grapefruit is one of your favorites
```

</details>

---

### Assignment 5.8 - Hello Admin

Loop through a list of usernames. Print a special greeting for `admin` and a
generic greeting for everyone else.

<details>
<summary>Spoiler Code</summary>

```python
usernames = ["anna", "bob", "charlie", "diana", "admin"]
for user in usernames:
    if user.lower() == "admin":
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Hello Anna, thank you for logging in again.
Hello Bob, thank you for logging in again.
Hello Charlie, thank you for logging in again.
Hello Diana, thank you for logging in again.
Hello admin, would you like to see a status report?
```

</details>

---

### Assignment 5.9 - No Users

Add an `if` test to check the list is not empty. Clear the list and confirm
the correct message prints.

<details>
<summary>Spoiler Code</summary>

```python
usernames = []
if usernames:
    for user in usernames:
        if user.lower() == "admin":
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")
```

</details>
<br>

<details>
<summary>Output</summary>

```
We need to find some users!
```

</details>

---

### Assignment 5.10 - Checking Usernames

Simulate unique username enforcement. Check each new username case-insensitively
against current users, print availability.

<details>
<summary>Spoiler Code</summary>

```python
current_users = ["Anna", "Bob", "Charlie", "Diana", "Admin"]
lower_case_users = [user.lower() for user in current_users]
new_users = ["abigail", "bob", "curtis", "diana", "edward"]
for user in new_users:
    if user.lower() in lower_case_users:
        print(f"Sorry. Username {user} is already in use. Choose another username")
    else:
        print(f"Username {user} is available.")
        current_users.append(user.title())
        lower_case_users.append(user.lower())
print("Final list of users:")
print(current_users)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Username abigail is available.
Sorry. Username bob is already in use. Choose another username
Username curtis is available.
Sorry. Username diana is already in use. Choose another username
Username edward is available.
Final list of users:
['Anna', 'Bob', 'Charlie', 'Diana', 'Admin', 'Abigail', 'Curtis', 'Edward']
```

</details>

---

### Assignment 5.11 - Ordinal Numbers

Store 1-9 in a list. Loop and print each with the correct ordinal suffix.

<details>
<summary>Spoiler Code</summary>

```python
numerals = list(range(1, 10))
for numeral in numerals:
    if numeral == 1:
        suffix = "st"
    elif numeral == 2:
        suffix = "nd"
    elif numeral == 3:
        suffix = "rd"
    else:
        suffix = "th"
    print(f"{numeral}{suffix}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
1st
2nd
3rd
4th
5th
6th
7th
8th
9th
```

</details>

---

### Assignment 5.12 - Styling `if` Statements

Review programs from this chapter and make sure conditional tests are styled
correctly - one space on either side of comparison operators.

<details>
<summary>Spoiler Code</summary>

```python
# No separate code - complete this in your other files.
# Consider using the Pylint extension in VS Code.
```

</details>

---

### Assignment 5.13 - Your Ideas

Record any new program ideas. Consider games, data sets, or web applications.

<details>
<summary>Spoiler Code</summary>

```python
# No code needed - complete this on your own.
```

</details>

---
