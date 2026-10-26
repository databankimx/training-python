## Chapter 10 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 10 try-it-yourself exercises.

> Because the 2nd and 3rd editions of the textbook present different
> approaches to file system interaction, I will present separate solutions for
> these editions for each problem. This file covers the 2nd edition answers.

---

### Assignment 10.1 - Learning Python

Open a blank file in your text editor and write a few lines summarizing what you've learned about Python so far. Start each line with the phrase `In Python you can...` Save the file as `learning_python.txt` in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block.

<details>
<summary>File Contents</summary>

In [Files/learning_python.txt](./Files/learning_python.txt)

```
In Python you can open a file.
In Python you can read the file's lines.
In Python you can store the file's lines in a list.
```

</details>
<br>

Solution:

<details>
<summary>Spoiler Code</summary>

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "learning_python.txt")

with open(file_path, encoding="UTF-8") as file:
    result = file.read()
    print(result.rstrip())

print()

with open(file_path, encoding="UTF-8") as file:
    for line in file:
        print(line.rstrip())

print()

with open(file_path, encoding="UTF-8") as file:
    lines = file.readlines()
for line in lines:
    print(line.rstrip())
```

</details>
<br>

<details>
<summary>Output</summary>

```
In Python you can open a file.
In Python you can read the file's lines.
In Python you can store the file's lines in a list.

In Python you can open a file.
In Python you can read the file's lines.
In Python you can store the file's lines in a list.

In Python you can open a file.
In Python you can read the file's lines.
In Python you can store the file's lines in a list.
```

</details>

---

### Assignment 10.2 - Learning C

You can use the `replace()` method to replace any word in a string with a different word. Here's a quick example showing how to replace `dog` with `cat` in a sentence:

```python
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
```

Read in each line from the file you just created, learning_python.txt, and replace the word Python with the name of another language, such as C. Print each modified line to the screen.

<details>
<summary>File Contents</summary>

In [Files/learning_python.txt](./Files/learning_python.txt)

```
In Python you can open a file.
In Python you can read the file's lines.
In Python you can store the file's lines in a list.
```

</details>
<br>

Solution:

<details>
<summary>Spoiler Code</summary>

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "learning_python.txt")

with open(file_path, encoding="UTF-8") as file:
    for line in file:
        line = line.replace("Python", "C++")
        print(line.rstrip())
```

</details>
<br>

<details>
<summary>Output</summary>

```
In C++ you can open a file.
In C++ you can read the file's lines.
In C++ you can store the file's lines in a list.
```

</details>

---

### Assignment 10.3 - Guest

Write a program that prompts the user for their name. When they respond, write their name to a file called `guest.txt`.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "guest.txt")

name = input("Please enter your name:\n> ")
with open(file_path, "w", encoding="UTF-8") as file:
    file.write(name)

with open(file_path, "r", encoding="UTF-8") as file:
    print(file.read())
```

</details>
<br>

<details>
<summary>File Contents</summary>

In [guest.txt](./Files/guest.txt)

```
Scott
```

</details>
<br>

<details>
<summary>Output</summary>

```
Please enter your name:
> Scott
Scott
```

</details>

---

### Assignment 10.4 - Guest Book

Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called `guest_book.txt`. Make sure each entry appears on a new line in the file.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "guest_book.txt")

while True:
    name = input("Please enter your name (or 'quit'):\n> ")
    if name.lower() == "quit":
        break
    with open(file_path, "a", encoding="UTF-8") as file:
        file.write(f"{name}\n")

with open(file_path, "r", encoding="UTF-8") as file:
    print(file.read())
```

</details>
<br>

<details>
<summary>File Contents</summary>

In [guest_book.txt](./Files/guest_book.txt)

```
Scott
Talia
```

</details>
<br>

<details>
<summary>Output</summary>

```
Please enter your name (or 'quit'):
> Scott
Please enter your name (or 'quit'):
> Talia
Please enter your name (or 'quit'):
> quit
Scott
Talia

```

</details>

---

### Assignment 10.5 - Programming Poll

Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
import os

ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", "poll_results.txt")

while True:
    print("What do you like about programming?")
    response = input("Please enter your answer (or 'quit'):\n> ")
    if response.lower() == "quit":
        break
    with open(file_path, "a", encoding="UTF-8") as file:
        file.write(f"{response}\n")

with open(file_path, "r", encoding="UTF-8") as file:
    print(file.read())
```

</details>
<br>

<details>
<summary>File Contents</summary>

In [poll_results.txt](./Files/poll_results.txt)

```
It makes me think
Programs are more logical than people
```

</details>
<br>

<details>
<summary>Output</summary>

```
What do you like about programming?
Please enter your answer (or 'quit'):
> It makes me think
What do you like about programming?
Please enter your answer (or 'quit'):
> Programs are more logical than people
What do you like about programming?
Please enter your answer (or 'quit'):
> quit
It makes me think
Programs are more logical than people

```

</details>

---

### Assignment 10.6 - Addition

One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an `int`, you'll get a `ValueError`. Write a program that prompts for two numbers. Add them together and print the result. Catch the `ValueError` if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
print("Enter two integers and I will add them.")

numbers = []

while len(numbers) < 2:
    response = input("Enter a number:\n> ")
    if response is None or len(response) < 1:
        print("You cannot leave the entry blank.")
        continue
    try:
        number = int(response)
        numbers.append(number)
    except ValueError:
        print("Please only enter numbers.")

my_sum = numbers[0] + numbers[1]
print(f"\n{numbers[0]} + {numbers[1]} = {my_sum}")
```

</details>
<br>

<details>
<summary>Output (OK)</summary>

```
Enter two integers and I will add them.
Enter a number:
> 17
Enter a number:
> 25

17 + 25 = 42
```

</details>
<br>

<details>
<summary>Output (Error)</summary>

```
Enter two integers and I will add them.
Enter a number:
> seventeen
Please only enter numbers.
Enter a number:
> 17
Enter a number:
> twenty-five
Please only enter numbers.
Enter a number:
> 25

17 + 25 = 42
```

</details>

> Note: the code file turns off a Sonar warning on the blank-entry check. That
> comment stays in the code file.

---

### Assignment 10.7 - Addition Calculator

Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
active = True

while True:
    print("Enter two integers and I will add them.")

    numbers = []

    while len(numbers) < 2:
        response = input("Enter a number:\n> ")
        if response is None or len(response) < 1:
            print("You cannot leave the entry blank.")
            continue
        if response.lower()[0] == "q":
            active = False
            break
        try:
            number = int(response)
            numbers.append(number)
        except ValueError:
            print("Please only enter numbers.")

    if not active:
        break

    my_sum = numbers[0] + numbers[1]
    print(f"\n{numbers[0]} + {numbers[1]} = {my_sum}\n")

print("\nGoodbye...\n")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Enter two integers and I will add them.
Enter a number:
> 17
Enter a number:
> 25

17 + 25 = 42

Enter two integers and I will add them.
Enter a number:
> seventeen
Please only enter numbers.
Enter a number:
> 17
Enter a number:
> 25

17 + 25 = 42

Enter two integers and I will add them.
Enter a number:
> q

Goodbye...

```

</details>

> Note: the code file turns off a Sonar warning on the blank-entry check. That
> comment stays in the code file.

---

### Assignment 10.8 - Cats and Dogs

Make two files, `cats.txt` and `dogs.txt`. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.

<details>
<summary>File Contents</summary>

In [cats.txt](./Files/cats.txt)

```
fluffy
felix
shadow
```

In [dogs.txt](./Files/dogs.txt)

```
fido
rover
spot
```

</details>
<br>

Solution:

<details>
<summary>Spoiler Code</summary>

```python
import os

ROOT_DIR = os.path.dirname(__file__)

def read_file(filename):
    """Read the selected file"""
    file_path = os.path.join(ROOT_DIR, "Files", filename)
    try:
        with open(file_path, encoding="UTF-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"\nFile [{filename}] not found!\n")
    else:
        print(f"\n{filename}:")
        print(content.rstrip())

file_names = ["cats.txt", "dogs.txt", "pets.txt"]

for file_name in file_names:
    read_file(file_name)
```

</details>
<br>

<details>
<summary>Output</summary>

```
cats.txt:
fluffy
felix
shadow

dogs.txt:
fido
rover
spot

File [pets.txt] not found!

```

</details>

---

### Assignment 10.9 - Silent Cats and Dogs

Modify your except block in Exercise 10-8 to fail silently if either file is missing.

<details>
<summary>File Contents</summary>

In [cats.txt](./Files/cats.txt)

```
fluffy
felix
shadow
```

In [dogs.txt](./Files/dogs.txt)

```
fido
rover
spot
```

</details>
<br>

Solution:

<details>
<summary>Spoiler Code</summary>

```python
import os

ROOT_DIR = os.path.dirname(__file__)
log_path = os.path.join(ROOT_DIR, "Files", "missing_files.log")

def read_file(filename):
    """Read the selected file"""
    file_path = os.path.join(ROOT_DIR, "Files", filename)
    try:
        with open(file_path, encoding="UTF-8") as file:
            content = file.read()
    except FileNotFoundError:
        with open(log_path, "a", encoding="UTF-8") as log:
            log.write(f"Missing File:\n{file_path}\n\n")
    else:
        print(f"{filename}:")
        print(content)

file_names = ["cats.txt", "dogs.txt", "pets.txt"]

for file_name in file_names:
    read_file(file_name)
```

</details>
<br>

<details>
<summary>Output File</summary>

In [missing_files.log](./Files/missing_files.log)

```
Missing File:
...\Files\pets.txt

```

</details>
<br>

<details>
<summary>Output</summary>

```
cats.txt:
fluffy
felix
shadow

dogs.txt:
fido
rover
spot

```

</details>

---

### Assignment 10.10 - Common Words

Visit [Project Gutenberg](https://gutenberg.org/) and find a few texts you'd like to analyze. Download the text files for these works, or copy the raw text from your browser into a text file on your computer. You can use the `count()` method to find out how many times a word or phrase appears in a string. For example, the following code counts the number of times `row` appears in a string:

```python
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
```

Notice that converting the string to lowercase using `lower()` catches all appearances of the word you're looking for, regardless of how it's formatted. Write a program that reads the files you found at Project Gutenberg and determines how many times the word `the` appears in each text. This will be an approximation because it will also count words such as `then` and `there`. Try counting `the `, with a space in the string, and see how much lower your count is.

<details>
<summary>File Contents</summary>
<br>

See Files:

* [frankenstein.txt](./Files/frankenstein.txt)
* [little_fuzzy.txt](./Files/little_fuzzy.txt)
* [star_hunter.txt](./Files/star_hunter.txt)
* snow_crash.txt (intentionally missing)
* [the_republic.txt](./Files/the_republic.txt)

</details>
<br>

Solution:

> Note: I diverged from the planned solution by implementing a system of word
> terminators that mitigate the need for the `the` vs `the ` test.

<details>
<summary>Spoiler Code</summary>

```python
import os

ROOT_DIR = os.path.dirname(__file__)

def examine_file(filename, search_words):
    """Count word occurrences in file passed"""
    file_path = os.path.join(ROOT_DIR, "Files", filename)
    terminators = [" ", ".", ",", "?", "\n"]
    try:
        with open(file_path, encoding="UTF-8") as f:
            content = f.read().lower()
    except FileNotFoundError:
        print(f"\nFile {filename} could not be found!")
    else:
        print(f"\nWord analysis in [{filename}]:")
        for word in search_words:
            num = 0
            for start_term in terminators:
                for end_term in terminators:
                    num += content.count(f"{start_term}{word}{end_term}")
            print(f"'{word}': {num}")

file_names = ["frankenstein.txt", "little_fuzzy.txt",
              "star_hunter.txt", "snow_crash.txt", "the_republic.txt"]
search_terms = ["the", "man", "woman", "person"]

for file_name in file_names:
    examine_file(file_name, search_terms)
```

</details>
<br>

<details>
<summary>Output</summary>

```

Word analysis in [frankenstein.txt]:
'the': 4539
'man': 122
'woman': 20
'person': 21

Word analysis in [little_fuzzy.txt]:
'the': 3252
'man': 61
'woman': 7
'person': 9

Word analysis in [star_hunter.txt]:
'the': 2518
'man': 107
'woman': 2
'person': 9

File snow_crash.txt could not be found!

Word analysis in [the_republic.txt]:
'the': 7822
'man': 341
'woman': 19
'person': 47

```

</details>

---

### Assignment 10.11 - Favorite Number

Write a program that prompts for the user's favorite number. Use `json.dump()` to store this number in a file. Write a separate program that reads in this value and prints the message: `I know your favorite number! It's _____.`

Solution:

<details>
<summary>Spoiler Code</summary>

```python
import os
import json

ROOT_DIR = os.path.dirname(__file__)

file_name = "favorite_number.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

def get_favorite_number():
    """Get the user's favorite number"""
    num = None

    while num is None:
        response = input("Please enter your favorite number:\n> ")
        try:
            num = int(response)
        except ValueError:
            print("Your entry must be a number!")

    with open(file_path, "w", encoding="UTF-8") as f:
        json.dump(num, f)

    print(f"I saved {num} as your favorite number!\n")
    return num

def read_favorite_number():
    """Read the user's favorite number from a file"""
    try:
        with open(file_path, encoding="UTF-8") as f:
            num = json.load(f)
            return int(num)
    except FileNotFoundError:
        num = get_favorite_number()
    return num

print(f"I know your favorite number! It's {read_favorite_number()}")
```

</details>
<br>

<details>
<summary>File Contents</summary>

In [favorite_number.json](./Files/favorite_number.json)

```
42
```

</details>
<br>

<details>
<summary>Output</summary>

```
Please enter your favorite number:
> 42
I saved 42 as your favorite number!

I know your favorite number! It's 42
```

</details>

---

### Assignment 10.12 - Verify User

The final listing for [remember_me.py](../textbook-downloads/2nd-edition/remember_me.py) assumes either that the user has already entered their username or that the program is running for the first time. We should modify it in case the current user is not the person who last used the program. Before printing a welcome back message in `greet_user()`, ask the user if this is the correct username. If it's not, call `get_new_username()` to get the correct username.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
import os
import json

ROOT_DIR = os.path.dirname(__file__)

def store_user(filepath):
    """Store the username to JSON file"""
    first_name = input("Enter your first name:\n> ")
    last_name = input("Enter your last name:\n> ")

    username = f"{first_name[0]}{last_name}".upper()

    with open(filepath, "w", encoding="UTF-8") as f:
        json.dump(username, f)

    return username

def get_stored_user(filepath):
    """Attempt to retrieve the username from JSON file"""
    try:
        with open(filepath, encoding="UTF-8") as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user(filepath):
    """Show desired greeting to user"""
    username = get_stored_user(filepath)
    matched = False
    if username:
        answer = input(f"Are you {username.upper()}? (Y|N)\n> ")
        matched = answer[0].lower() == "y"
        if not matched:
            username = store_user(filepath)
    else:
        username = store_user(filepath)

    if matched:
        print(f"\nWelcome back, {username.upper()}\n")
    else:
        print(f"\nWe'll remember you when you come back, {username.upper()}\n")

file_name = "username.json"
file_path = os.path.join(ROOT_DIR, "Files", file_name)

greet_user(file_path)
```

</details>
<br>

<details>
<summary>Output (No Stored File)</summary>

```
Enter your first name:
> john
Enter your last name:
> smith

We'll remember you when you come back, JSMITH

```

</details>
<br>

<details>
<summary>File Contents</summary>

In [username.json](./Files/username.json)

```
"JSMITH"
```

</details>
<br>

<details>
<summary>Output (With Stored File - Same User)</summary>

```
Are you JSMITH? (Y|N)
> y

Welcome back, JSMITH

```

</details>
<br>

<details>
<summary>Output (With Stored File - Different User)</summary>

```
Are you JSMITH? (Y|N)
> n
Enter your first name:
> Jane
Enter your last name:
> Jones

We'll remember you when you come back, JJONES

```

</details>
<br>

<details>
<summary>File Contents</summary>

In [username.json](./Files/username.json)

```
"JJONES"
```

</details>

---
