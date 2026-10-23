## Chapter 3 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 3 try-it-yourself exercises.

---

### Assignment 3.1 - Names

Store the names of a few of your friends in a list called names. Print each
person's name by accessing each element in the list, one at a time.

<details>
<summary>Spoiler Code</summary>

```python
friends = ["Matt", "Danica", "Becky", "Alex"]
print(friends[0])
print(friends[1])
print(friends[-2])
print(friends[-1])
```

</details>
<br>

<details>
<summary>Output</summary>

```
Matt
Danica
Becky
Alex
```

</details>

---

### Assignment 3.2 - Greetings

Start with the list you used in Exercise 3.1, but instead of just printing
each person's name, print a message to them. The text of each message should
be the same, but each message should be personalized with the person's name.

<details>
<summary>Spoiler Code</summary>

```python
friends = ["Matt", "Danica", "Becky", "Alex"]
print(f"Hi there, {friends[0]}. You're my friend.")
print(f"Hi there, {friends[1]}. You're my friend.")
print(f"Hi there, {friends[-2]}. You're my friend.")
print(f"Hi there, {friends[-1]}. You're my friend.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Hi there, Matt. You're my friend.
Hi there, Danica. You're my friend.
Hi there, Becky. You're my friend.
Hi there, Alex. You're my friend.
```

</details>

---

### Assignment 3.3 - Your Own List

Think of your favorite mode of transportation, such as a motorcycle or a car,
and make a list that stores several examples. Use your list to print a series
of statements about these items, such as "I would like to own a Honda
motorcycle."

<details>
<summary>Spoiler Code</summary>

```python
cars = ["challenger", "mustang", "camaro"]
print(f"These are some common muscle cars: {cars}")
print(f"The {cars[0]} is my favorite.")
print(f"I like the look of older {cars[1]}s from the 60s and 70s.")
print(f"I don't like the {cars[2]}.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
These are some common muscle cars: ['challenger', 'mustang', 'camaro']
The challenger is my favorite.
I like the look of older mustangs from the 60s and 70s.
I don't like the camaro.
```

</details>

---

### Assignment 3.4 - Guest List

If you could invite anyone, living or deceased, to dinner, who would you
invite? Make a list that includes at least three people you'd like to invite
to dinner. Then use your list to print a message to each person, inviting
them to dinner.

<details>
<summary>Spoiler Code</summary>

```python
guests = [
    "Charles Babbage",
    "Ada Lovelace",
    "George Boole",
    "Grace Hopper",
    "Alan Turing",
    "Tim Berners-Lee"
]
print(f"{guests[0]}, would you like to join me for dinner?")
print(f"{guests[1]}, would you like to join me for dinner?")
print(f"{guests[2]}, would you like to join me for dinner?")
print(f"{guests[3]}, would you like to join me for dinner?")
print(f"{guests[4]}, would you like to join me for dinner?")
print(f"{guests[5]}, would you like to join me for dinner?")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Charles Babbage, would you like to join me for dinner?
Ada Lovelace, would you like to join me for dinner?
George Boole, would you like to join me for dinner?
Grace Hopper, would you like to join me for dinner?
Alan Turing, would you like to join me for dinner?
Tim Berners-Lee, would you like to join me for dinner?
```

</details>

---

### Assignment 3.5 - Changing Guest List

You just heard that one of your guests can't make the dinner, so you need to
send out a new set of invitations. You'll have to think of someone else to
invite.

<details>
<summary>Spoiler Code</summary>

```python
guests = [
    "Charles Babbage",
    "Ada Lovelace",
    "George Boole",
    "Grace Hopper",
    "Alan Turing",
    "Tim Berners-Lee"
]
print(f"{guests[5]} can't join us for dinner.")
guests[5] = "Linus Torvalds"
print(f"{guests[0]}, would you like to join me for dinner?")
print(f"{guests[1]}, would you like to join me for dinner?")
print(f"{guests[2]}, would you like to join me for dinner?")
print(f"{guests[3]}, would you like to join me for dinner?")
print(f"{guests[4]}, would you like to join me for dinner?")
print(f"{guests[5]}, would you like to join me for dinner?")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Tim Berners-Lee can't join us for dinner.
Charles Babbage, would you like to join me for dinner?
Ada Lovelace, would you like to join me for dinner?
George Boole, would you like to join me for dinner?
Grace Hopper, would you like to join me for dinner?
Alan Turing, would you like to join me for dinner?
Linus Torvalds, would you like to join me for dinner?
```

</details>

---

### Assignment 3.6 - More Guests

You just found a bigger dinner table, so now more space is available. Think
of three more guests to invite to dinner.

<details>
<summary>Spoiler Code</summary>

```python
guests = [
    "Charles Babbage",
    "Ada Lovelace",
    "George Boole",
    "Grace Hopper",
    "Alan Turing",
    "Tim Berners-Lee"
]
print(f"I found a bigger table that can seat {len(guests) + 3} people.")
guests.insert(0, "Barbara Liskov")
guests.insert(3, "Donald Knuth")
guests.append("Margaret Hamilton")
print(guests)

print(f"{guests[0]}, would you like to join me for dinner?")
print(f"{guests[1]}, would you like to join me for dinner?")
print(f"{guests[2]}, would you like to join me for dinner?")
print(f"{guests[3]}, would you like to join me for dinner?")
print(f"{guests[4]}, would you like to join me for dinner?")
print(f"{guests[5]}, would you like to join me for dinner?")
print(f"{guests[6]}, would you like to join me for dinner?")
print(f"{guests[7]}, would you like to join me for dinner?")
print(f"{guests[8]}, would you like to join me for dinner?")
```

</details>
<br>

<details>
<summary>Output</summary>

```
I found a bigger table that can seat 9 people.
['Barbara Liskov', 'Charles Babbage', 'Ada Lovelace', 'Donald Knuth', 'George Boole', 'Grace Hopper', 'Alan Turing', 'Tim Berners-Lee', 'Margaret Hamilton']
Barbara Liskov, would you like to join me for dinner?
Charles Babbage, would you like to join me for dinner?
Ada Lovelace, would you like to join me for dinner?
Donald Knuth, would you like to join me for dinner?
George Boole, would you like to join me for dinner?
Grace Hopper, would you like to join me for dinner?
Alan Turing, would you like to join me for dinner?
Tim Berners-Lee, would you like to join me for dinner?
Margaret Hamilton, would you like to join me for dinner?
```

</details>

---

### Assignment 3.7 - Shrinking Guest List

You just found out that your new dinner table won't arrive in time for the
dinner, and you have space for only two guests.

<details>
<summary>Spoiler Code</summary>

```python
guests = [
    "Barbara Liskov",
    "Charles Babbage",
    "Ada Lovelace",
    "Donald Knuth",
    "George Boole",
    "Grace Hopper",
    "Alan Turing",
    "Tim Berners-Lee",
    "Margaret Hamilton"
]

print("Oh no! I can only invite two people to dinner!")
print(f"I'm sorry, {guests.pop(-1)}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop(0)}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"{guests[0]}, you are still invited.")
print(f"{guests[1]}, you are still invited.")
del guests[-1]
del guests[0]
print(guests)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Oh no! I can only invite two people to dinner!
I'm sorry, Margaret Hamilton. I can't invite you to dinner.
I'm sorry, Barbara Liskov. I can't invite you to dinner.
I'm sorry, Tim Berners-Lee. I can't invite you to dinner.
I'm sorry, Alan Turing. I can't invite you to dinner.
I'm sorry, Grace Hopper. I can't invite you to dinner.
I'm sorry, George Boole. I can't invite you to dinner.
I'm sorry, Donald Knuth. I can't invite you to dinner.
Charles Babbage, you are still invited.
Ada Lovelace, you are still invited.
[]
```

</details>

---

### Assignment 3.8 - Seeing the World

Think of at least five places in the world you'd like to visit. Store them in
a list and use sort, sorted, reverse, and reversed on them.

<details>
<summary>Spoiler Code</summary>

```python
places = ["cairo", "tokyo", "antarctica", "beijing", "australia"]
print(places)
print("---")
print(sorted(places))
print(places)
print("---")
print(sorted(places, reverse=True))
print(places)
print("---")
places.reverse()
print(places)
print("---")
places.reverse()
print(places)
print("---")
places.sort()
print(places)
print("---")
places.sort(reverse=True)
print(places)
```

</details>
<br>

<details>
<summary>Output</summary>

```
['cairo', 'tokyo', 'antarctica', 'beijing', 'australia']
---
['antarctica', 'australia', 'beijing', 'cairo', 'tokyo']
['cairo', 'tokyo', 'antarctica', 'beijing', 'australia']
---
['tokyo', 'cairo', 'beijing', 'australia', 'antarctica']
['cairo', 'tokyo', 'antarctica', 'beijing', 'australia']
---
['australia', 'beijing', 'antarctica', 'tokyo', 'cairo']
---
['cairo', 'tokyo', 'antarctica', 'beijing', 'australia']
---
['antarctica', 'australia', 'beijing', 'cairo', 'tokyo']
---
['tokyo', 'cairo', 'beijing', 'australia', 'antarctica']
```

</details>

---

### Assignment 3.9 - Dinner Guests

Use `len()` to print a message indicating the number of people you are
inviting to dinner.

<details>
<summary>Spoiler Code</summary>

```python
guests = [
    "Charles Babbage",
    "Ada Lovelace",
    "George Boole",
    "Grace Hopper",
    "Alan Turing",
    "Tim Berners-Lee"
]
print(f"I am inviting {len(guests)} people to dinner.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
I am inviting 6 people to dinner.
```

</details>

---

### Assignment 3.10 - Every Function

Think of something you could store in a list and write a program that uses
each function introduced in this chapter at least once.

<details>
<summary>Spoiler Code</summary>

```python
# Part 1: a list of snacks
snacks = ["popcorn", "pretzels", "apple"]
print(f"We start with {len(snacks)} snacks: {snacks}")   # len()
print(snacks[0])                                          # indexing
snacks[1] = "trail mix"                                   # modifying a value
snacks.append("cheese")                                   # append()
snacks.insert(0, "chips")                                 # insert()
snacks.remove("apple")                                    # remove()
print(snacks)
last = snacks.pop()                                       # pop()
first = snacks.pop(0)                                     # pop() with an index
print(f"Popped {last} and {first}: {snacks}")
del snacks[0]                                             # del
print(snacks)

# Part 2: sorting and reversing a list of numbers
scores = [13, 7, 28, 3]
scores.sort()                                             # sort()
print(scores)
print(sorted(scores, reverse=True))                       # sorted()
scores.reverse()                                          # reverse()
print(scores)
print(list(reversed(scores)))                             # reversed()
scores.clear()                                            # clear()
print(scores)
```

</details>
<br>

<details>
<summary>Output</summary>

```
We start with 3 snacks: ['popcorn', 'pretzels', 'apple']
popcorn
['chips', 'popcorn', 'trail mix', 'cheese']
Popped cheese and chips: ['popcorn', 'trail mix']
['trail mix']
[3, 7, 13, 28]
[28, 13, 7, 3]
[28, 13, 7, 3]
[3, 7, 13, 28]
[]
```

</details>

---

### Assignment 3.11 - Intentional Error

If you haven't received an index error yet, try to make one happen. Make
sure you correct the error before closing the program.

<details>
<summary>Spoiler Code</summary>

```python
guests = ["Charles Babbage", "Ada Lovelace", "George Boole",
          "Grace Hopper", "Alan Turing", "Tim Berners-Lee"]
print(guests[6])  # IndexError: list index out of range
```

</details>
<br>

<details>
<summary>Output</summary>

```
Traceback (most recent call last):
  File "...\11_intentional_error.py", line 2, in <module>
    print(guests[6])
          ~~~~~~^^^
IndexError: list index out of range
```

</details>

---
