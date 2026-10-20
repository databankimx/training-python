## Chapter 7 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 7 try-it-yourself exercises.

---

### Assignment 7.1 - Rental Car

Write a program that asks the user what kind of rental car they would like. 
Print a message about that car, such as:  
`Let me see if I can find you a Subaru.`


Solution:

<details>
<summary>Spoiler Code</summary>

```python
car = input("What kind of rental car would you like?\n> ")
print(f"Let me see if I can find you a {car.title()}.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
What kind of rental car would you like?
> Mini Cooper
Let me see if I can find you a Mini Cooper.
```

</details>

---

### Assignment 7.2 - Restaurant Seating

Write a program that asks the user how many people are in their dinner group. 
If the answer is more than eight, print a message saying they'll have to wait 
for a table. Otherwise, report that their table is ready.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
guests = input("How many guests in your party?\n> ")
guests = int(guests)
if (guests > 8):
    print("There will be a little wait for a table.")
else:
    print("Your table is ready.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
How many guests in your party?
> 6
Your table is ready.
```

</details>

---

### Assignment 7.3 - Multiples of Ten

Ask the user for a number, and then report whether the number is a multiple 
of 10 or not.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
number = int(input(
    "\nEnter a number, and I will tell you if it is a multiple of 10:\n> "))
condition = "" if number % 10 == 0 else "not "
print(f"{number} is {condition}a multiple of 10.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Enter a number, and I will tell you if it is a multiple of 10:
> 42
42 is not a multiple of 10.
```

---

</details>

### Assignment 7.4 - Pizza Toppings

Write a loop that prompts the user to enter a series of pizza toppings until 
they enter a `quit` value. As they enter each topping, print a message saying 
you'll add that topping to their pizza.


Solution:

<details>
<summary>Spoiler Code</summary>

```python
message = ""
prompt = "Enter a topping or 'quit':\n> "
while message.lower() != "quit":
    message = input(prompt)
    if message.lower() != "quit":
        print(f" - Added {message}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Enter a topping or 'quit':
> pepperoni
 - Added pepperoni
Enter a topping or 'quit':
> mushrooms
 - Added mushrooms
Enter a topping or 'quit':
> quit
```

</details>

---

### Assignment 7.5 - Movie Tickets

A movie theater charges different ticket prices depending on a person's age.

* If a person is under the age of 3, the ticket is free
* If they are between 3 and 12, the ticket is $10
* And if they are over age 12, the ticket is $15.

Write a loop in which you ask users their age, and then tell them the cost of 
their movie ticket.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
price = 0
age = 0
message = ""
prompt = "Please enter your age or 'quit':\n> "
while True:
    message = input(prompt)
    if message.lower() == 'quit':
        break
    age = int(message)
    if age < 3:
        price = 0
    elif age < 13:
        price = 10
    else:
        price = 15
    print(f"Your ticket costs ${price}.00")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Please enter your age or 'quit':
> 54
Your ticket costs $15.00
Please enter your age or 'quit':
> 12
Your ticket costs $10.00
Please enter your age or 'quit':
> 1
Your ticket costs $0.00
Please enter your age or 'quit':
> quit
```

</details>

---

### Assignment 7.6 - Three Exits

Write different versions of either Exercise 7.4 or Exercise 7.5 that do each 
of the following at least once:

* Use a conditional test in the while statement to stop the loop.
* Use an `active` variable to control how long the loop runs.
* Use a break statement to exit the loop when the user enters a `quit` value.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
message = ""
active = True
prompt = "Enter a topping or 'quit':\n> "
while active:
    message = input(prompt)
    if message.lower() == "quit":
        # Only one of these is needed (bullets 2 and 3)
        active = False
        break
    print(f" - Added {message}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Enter a topping or 'quit':
> sausage
 - Added sausage
Enter a topping or 'quit':
> green pepper
 - Added green pepper
Enter a topping or 'quit':
> quit
```

</details>

---

### Assignment 7.7 - Infinity

Write a loop that never ends, and run it. (To end the loop, press CTRL-C or 
close the window displaying the output.)

Solution:

<details>
<summary>Spoiler Code</summary>

```python
num = 1
while num <= 10:
    # num + 1
    print(num)
```

</details>
<br>

<details>
<summary>Output</summary>

```
1
1
... -- SNIP --
1
1
Traceback (most recent call last):
  File "...\07_infinity.py", line 12, in <module>
    print(num)
KeyboardInterrupt
```

</details>

---

### Assignment 7.8 - Deli

Make a list called `sandwich_orders` and fill it with the names of various sandwiches. Then make an empty list called `finished_sandwiches`. Loop through the list of sandwich orders and print a message for each order, such as `I made your tuna sandwich`. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
sandwich_orders = ["italian sub", "reuben", "croque monsieur", "pb&j"]
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich} sandwich...")
print(f"The following sandwich orders were fulfilled:\n{finished_sandwiches}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
I made your italian sub sandwich...
I made your reuben sandwich...
I made your croque monsieur sandwich...
I made your pb&j sandwich...
The following sandwich orders were fulfilled:
['italian sub', 'reuben', 'croque monsieur', 'pb&j']
```

</details>

---

### Assignment 7.9 - No Pastrami

Using the list `sandwich_orders` from Exercise 7.8, make sure the sandwich 
`pastrami` appears in the list at least three times. Add code near the 
beginning of your program to print a message saying the deli has run out of 
pastrami, and then use a while loop to remove all occurrences of `pastrami` 
from `sandwich_orders`. Make sure no pastrami sandwiches end up in 
`finished_sandwiches`.


Solution:

<details>
<summary>Spoiler Code</summary>

```python
sandwich_orders = [
    "italian sub",
    "pastrami",
    "reuben",
    "pastrami",
    "pastrami",
    "croque monsieur",
    "pastrami",
    "pb&j"
]
print("We have run out of pastrami!")
finished_sandwiches = []
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich} sandwich...")
print(f"The following sandwich orders were fulfilled:\n{finished_sandwiches}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
We have run out of pastrami!
I made your italian sub sandwich...
I made your reuben sandwich...
I made your croque monsieur sandwich...
I made your pb&j sandwich...
The following sandwich orders were fulfilled:
['italian sub', 'reuben', 'croque monsieur', 'pb&j']
```

</details>

---

### Assignment 7.10 - Dream Vacations

Write a program that polls users about their dream vacation. Write a prompt similar to  
`If you could visit one place in the world, where would you go?`  
Include a block of code that prints the results of the poll.


Solution:

<details>
<summary>Spoiler Code</summary>

```python
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?\n> ")
    response = input("Where would you take your dream vacation?\n> ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no)\n> ").lower()[0]
    if repeat == "n":
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name}'s dream vacation is to {response}.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
What is your name?
> Scott
Where would you take your dream vacation?
> Japan
Would you like to let another person respond? (yes/no)
> y

What is your name?
> Jane
Where would you take your dream vacation?
> France
Would you like to let another person respond? (yes/no)
> n

--- Poll Results ---
Scott's dream vacation is to Japan.
Jane's dream vacation is to France.
```

</details>

---
