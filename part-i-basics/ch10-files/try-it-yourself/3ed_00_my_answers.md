## Chapter 10 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 10 try-it-yourself exercises.

> Because the 2nd and 3rd editions of the textbook present different 
> approaches to file system interaction, I will present separate solutions for
> these editions for each problem. This file covers the 3rd edition answers.

For all 3rd edition problems, I will use the code below:

<details>
<summary>Relative Paths Module</summary>

In [relative_paths.py](./relative_paths.py)

```python
"""A module to expose a simple method to interact with files via relative path"""

from os import path

ROOT_DIR = None

def get_path(file_name: str, folder: str=None, parent_levels: int=0, debug: bool=False) -> str:
    """Returns a relative path to a specified file"""
    initialize(debug)
    for _ in range(parent_levels):
        file_name = path.join("..", file_name)
    file_path = path.join(ROOT_DIR, file_name) if folder == None else path.join(ROOT_DIR, folder, file_name)
    if debug:
        print(f"Set file path: {file_path}")
    return file_path

def initialize(debug: bool) -> None:
    """Store the root directory"""
    global ROOT_DIR
    if ROOT_DIR != None: return
    ROOT_DIR = path.dirname(__file__)
    if debug:
        print(f"Set root directory: {ROOT_DIR}")
```

</details>

---

### Assignment 10.1 - Learning Python

Open a blank file in your text editor and write a few lines summarizing what
you've learned about Python so far. Start each line with the phrase
`In Python you can...` Save the file as `learning_python.txt` in the same 
directory as your exercises from this chapter. Write a program that reads the 
file and prints what you wrote three times. Print the contents once by 
reading in the entire file, once by looping over the file object, and once by 
storing the lines in a list and then working with them outside the with block.

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

Solution

<details>
<summary>Spoiler Code</summary>

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("learning_python.txt", "Files")

path_object = Path(file_path)
text = path_object.read_text()
print(text.rstrip())

print()

lines = text.splitlines()
for line in lines:
    print(line.rstrip())

print()

with Path(file_path).open(encoding="utf-8") as file:
    for line in file:
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
<br>

---

### Assignment 10.2 - Learning C

You can use the `replace()` method to replace any word in a string with a 
different word. Here's a quick example showing how to replace `dog` with 
`cat` in a sentence:

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
from relative_paths import get_path
from pathlib import Path

file_path = get_path("learning_python.txt", "Files")

file = Path(file_path)
text = file.read_text()
for line in text.splitlines():
    print(line.rstrip().replace("Python", "C++"))
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
<br>

---

### Assignment 10.3 - Simpler Code

The program [`file_reader.py`](../Textbook%20Downloads/E3/reading_from_a_file/file_reader.py) in this section uses a temporary variable, lines, to show how 
`splitlines()` works. You can skip the temporary variable and loop directly 
over the list that `splitlines()` returns:

```python
for line in contents.splitlines():
    ...
```

Remove the temporary variable from each of the programs in this section, to 
make them more concise.

<details>
<summary>File Contents</summary>

In [pi_digits.txt](./Files/pi_digits.txt)

```
3.1415926535 
  8979323846 
  2643383279
```

</details>
<br>

Solution:

<details>
<summary>Spoiler Code</summary>

```python
from relative_paths import get_path
from pathlib import Path

text = Path(get_path("pi_digits.txt", "Files")).read_text()

for line in text.splitlines():
    print(line.rstrip())
```

</details>
<br>

<details>
<summary>Output</summary>

```
3.1415926535
  8979323846
  2643383279
```

</details>
<br>

---

### Assignment 10.4 - Guest

Write a program that prompts the user for their name. When they respond, write their name to a file called `guest.txt`.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("guest.txt", "Files")

file = Path(file_path)

name = input("Please enter your name:\n> ")
file.write_text(name + "\n")

print(file.read_text())
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
<br>

---

### Assignment 10.5 - Guest Book

Write a while loop that prompts users for their name. When they enter their 
name, print a greeting to the screen and add a line recording their visit in 
a file called `guest_book.txt`. Make sure each entry appears on a new line in 
the file.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
from relative_paths import get_path
from pathlib import Path

file_path = get_path("guest_book.txt", "Files")

print("Try-it-Yourself:")
print("Assignment 10.5\n")

names = ""

while True:
    name = input("Please enter your name (or 'quit'):\n> ")
    if name.lower() == "quit":
        break
    names += name + "\n"

file = Path(file_path)

file.write_text(names, encoding="utf-8")

print(file.read_text(encoding="utf-8"))
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
<br>

---

### Assignment 10.6 - Addition

One common problem when prompting for numerical input occurs when people 
provide text instead of numbers. When you try to convert the input to an 
`int`, you'll get a `ValueError`. Write a program that prompts for two 
numbers. Add them together and print the result. Catch the `ValueError` if 
either input value is not a number, and print a friendly error message. Test 
your program by entering two numbers and then by entering some text instead 
of a number.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
numbers = []

while len(numbers) < 2:
    response = input("Enter a number:\n> ")
    if response == None or len(response) < 1:
        print("You cannot leave the entry blank.")
        continue
    try:
        number = int(response)
        numbers.append(number)
    except ValueError:
        print("Please only enter numbers.")

sum = numbers[0] + numbers[1]
print(f"\n{numbers[0]} + {numbers[1]} = {sum}")
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
<br>

---

### Assignment 10.7 - Addition Calculator

Wrap your code from Exercise 10-6 in a while loop so the user can continue 
entering numbers even if they make a mistake and enter text instead of a 
number.

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
        if response == None or len(response) < 1:
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

    sum = numbers[0] + numbers[1]
    print(f"\n{numbers[0]} + {numbers[1]} = {sum}\n")

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
> 17
Enter a number:
> twenty-five
Please only enter numbers.
Enter a number:
> 25

17 + 25 = 42

Enter two integers and I will add them.
Enter a number:
> q

Goodbye...
```

</details>
<br>

---

### Assignment 10.8 - Cats and Dogs

Make two files, `cats.txt` and `dogs.txt`. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a `try`-`except` block to catch the `FileNotFound` error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.

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
from relative_paths import get_path
from pathlib import Path

def read_file(file_name):
    """Read the selected file"""
    file_path = get_path(file_name, "Files")
    try:
        file = Path(file_path)
        content = file.read_text()
    except FileNotFoundError:
        print(f"File [{file_name}] not found!\n")
    else:
        print(f"{file_name}:")
        print(content)

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
<br>

---

### Assignment 10.9 - Silent Cats and Dogs

Modify your except block in Exercise 10-8 to fail silently if either file is 
missing.

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
from relative_paths import get_path
from pathlib import Path

log_path = get_path("missing_files.log", "Files")
log_file = Path(log_path)

def read_file(file_name):
    """Read the selected file"""
    file_path = get_path(file_name, "Files")
    try:
        file = Path(file_path)
        content = file.read_text()
    except FileNotFoundError:
        with log_file.open("a") as l:
            l.write(f"Missing File:\n{file_path}\n\n")
        pass
    else:
        print(f"{file_name}:")
        print(content)

file_names = ["cats.txt", "dogs.txt", "pets.txt"]

for file_name in file_names:
    read_file(file_name)
```

</details>
<br>

<details>
<summary>Output File</summary>

In [`missing_files.log`](./Files/missing_files.log)

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
<br>

---

### Assignment 10.10 - Common Words

Visit [Project Gutenberg](https://gutenberg.org/) and find a few texts you'd 
like to analyze. Download the text files for these works, or copy the raw 
text from your browser into a text file on your computer. You can use the 
`count()` method to find out how many times a word or phrase appears in a 
string. For example, the following code counts the number of times `row` 
appears in a string:

```python
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
```

Notice that converting the string to lowercase using `lower()` catches all 
appearances of the word you're looking for, regardless of how it's formatted. 
Write a program that reads the files you found at Project Gutenberg and 
determines how many times the word `the` appears in each text. This will be 
an approximation because it will also count words such as `then` and `there`. 
Try counting `the `, with a space in the string, and see how much lower your 
count is.

<details>
<summary>File Contents</summary>
<br>

See Files:

* [frankenstein.txt](./Files/frankenstein.txt)
* [little_fuzzy.txt](./Files/little_fuzzy.txt)
* [star_hunter](./Files/star_hunter.txt)
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
from relative_paths import get_path
from pathlib import Path

def examine_file(file_name, search_words):
    """Count word occurrences in file passed"""
    file_path = get_path(file_name, "Files")
    terminators = [" ", ".", ",", "?", "\n"]

    try:
        file = Path(file_path)
        content = file.read_text()
    except:
        print(f"\nFile {file_name} could not be found!")
    else:
        print(f"\nWord analysis in [{file_name}]:")
        for word in search_words:
            num = 0
            for start_term in terminators:
                for end_term in terminators:
                    num += content.count(f"{start_term}{word}{end_term}")
            print(f"{word}: {num}")

file_names = ["frankenstein.txt", "little_fuzzy.txt",
              "star_hunter.txt", "snow_crash.txt", "the_republic.txt"]
search_terms = ["man", "woman", "person"]

for file_name in file_names:
    examine_file(file_name, search_terms)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Word analysis in [frankenstein.txt]:
man: 120
woman: 20
person: 21

Word analysis in [little_fuzzy.txt]:
man: 60
woman: 7
person: 9

Word analysis in [star_hunter.txt]:
man: 107
woman: 2
person: 9

File snow_crash.txt could not be found!

Word analysis in [the_republic.txt]:
man: 341
woman: 19
person: 47
```

</details>
<br>

---

### Assignment 10.11 - Favorite Number

Write a program that prompts for the user's favorite number. Use json.dump() 
to store this number in a file. Write a separate program that reads in this 
value and prints the message,  
`I know your favorite number! It's _____.`

Solution:

<details>
<summary>Spoiler Code</summary>

```python
from relative_paths import get_path
from pathlib import Path
import json

def get_favorite_number():
    """Get the user's favorite number"""    
    num = None

    while num == None:
        response = input("Please enter your favorite number:\n> ")
        try:
            num = int(response)
        except ValueError:
            print("Your entry must be a number!")

    file = Path(file_path)
    file.write_text(json.dumps(num))

    print(f"I saved {num} as your favorite number!\n")
    return num

def read_favorite_number():
    """Read the user's favorite number from a file"""    
    file = Path(file_path)
    if file.exists():
        num = json.loads(file.read_text())
        return num
    else:
        return get_favorite_number()

file_name = "favorite_number.json"
file_path = get_path(file_name, "Files")

number = read_favorite_number()

if number:
    print(f"I know your favorite number is {number}.\n")
else:
    print("Something went wrong!")
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

I know your favorite number is 42.
```

</details>
<br>

---

### Assignment 10.12 - Favorite Number Remembered

Combine the two programs from Exercise 10.11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user's favorite number and store it in a file. Run the program twice to see that it works.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
from relative_paths import get_path
from pathlib import Path
import json

def store_favorite_number(file_path):
    """Get the user's favorite number and store it in a file"""
    num = None
    while num == None:
        response = input("Please enter your favorite number:\n> ")
        try:
            num = int(response)
        except ValueError:
            print("Your entry must be a number!\n")
    file = Path(file_path)
    file.write_text(json.dumps(num))
    print(f"I saved {num} as your favorite number!\n")
    return num

def get_favorite_number(file):
    """Attempt to read user's favorite number from a file"""
    file = Path(file_path)
    if file.exists():
        num = json.loads(file.read_text())
        return num
    else:
        return store_favorite_number(file)

file_name = "favorite_number_remembered.json"
file_path = get_path(file_name, "Files")

number = get_favorite_number(file_path)
if number:
    print(f"I know your favorite number is {number}.\n")
else:
    print("Something went wrong!")
```

</details>
<br>

<details>
<summary>File Contents</summary>

In [favorite_number_remembered.json](./Files/favorite_number_remembered.json)

```

```

</details>
<br>

<details>
<summary>Output (No Saved File)</summary>

```
Please enter your favorite number:
> 42
I saved 42 as your favorite number!

I know your favorite number is 42.
```

</details>
<br>

<details>
<summary>Output (With Saved File)</summary>

```
I know your favorite number is 42.
```

</details>
<br>

---

### Assignment 10.13 - User Dictionary

The [remember_me.py](../Textbook%20Downloads/E3/storing_data/remember_me.py) 
example only stores one piece of information, the username. Expand this 
example by asking for two more pieces of information about the user, then 
store all the information you collect in a dictionary. Write this dictionary 
to a file using `json.dumps()`, and read it back in using `json.loads()`. 
Print a summary showing exactly what your program remembers about the user.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
from relative_paths import get_path
from pathlib import Path
import json

file_name = "user_info.json"
file_path = get_path(file_name, "Files")

file = Path(file_path)

if file.exists():
    user = json.loads(file.read_text())
    print(f"Welcome back, {user['username']}!")
    print("Here's what I know about you:")
    for key, value in user.items():
        if key == "username": continue
        print(f"{key.replace('_', ' ').title()}: {value}")
else:
    user = {}
    user_keys = ["first_name", "last_name", "job_title", "location"]
    for key in user_keys:
        user[key] = input(f"Enter your {key.replace('_', ' ')}:\n> ")

    user["username"] = f"{user['first_name'][0]}{user['last_name']}".upper()

    file.write_text(json.dumps(user))

    print(f"We'll remember you when you come back, {user['username']}")
```

</details>
<br>

<details>
<summary>File Contents</summary>

In [user_info.json](./Files/user_info.json)

```
{"first_name": "Scott", "last_name": "McLean", "job_title": "Programmer", "location": "Dallas", "username": "SMCLEAN"}
```

</details>
<br>

<details>
<summary>Output (No Saved File)</summary>

```
Enter your first name:
> Scott
Enter your last name:
> McLean
Enter your job title:
> Programmer
Enter your location:
> Dallas
We'll remember you when you come back, SMCLEAN
```

</details>
<br>

<details>
<summary>Output (With Saved File)</summary>

```
Welcome back, SMCLEAN!
Here's what I know about you:
First Name: Scott
Last Name: McLean
Job Title: Programmer
Location: Dallas
```

</details>
<br>

---

### Assignment 10.14 - Verify User

The final listing for
[remember_me.py](../Textbook%20Downloads/E3/storing_data/remember_me.py) 
assumes either that the user has already entered their username or that the 
program is running for the first time. We should modify it in case the 
current user is not the person who last used the program. Before printing a 
welcome back message in `greet_user()`, ask the user if this is the correct 
username. If it's not, call `get_new_username()` to get the correct username.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
from relative_paths import get_path
from pathlib import Path
import json

def store_user(file_path):
    """Store the username to JSON file"""
    first_name = input("Enter your first name:\n> ")
    last_name = input("Enter your last name:\n> ")

    username = f"{first_name[0]}{last_name}".upper()

    file = Path(file_path)
    file.write_text(json.dumps(username))

    return username

def get_stored_user(file_path):
    """Attempt to retrieve the username from JSON file"""
    file = Path(file_path)

    if file.exists():
        username = json.loads(file.read_text())
        return username
    else:
        return None

def greet_user(file_path):
    """Show desired greeting to user"""
    username = get_stored_user(file_path)
    matched = False

    if username:
        answer = input(f"Are you {username.upper()}? (Y|N)\n> ")
        matched = answer[0].lower() == "y"
        if not matched:
            username = store_user(file_path)
    else:
        username = store_user(file_path)

    if matched:
        print(f"\nWelcome back, {username.upper()}\n")
    else:
        print(f"\nWe'll remember you when you come back, {username.upper()}\n")

file_name = "username.json"
file_path = get_path(file_name, "Files")

greet_user(file_path)
```

</details>
<br>

<details>
<summary>Output (No Saved File)</summary>

```
Enter your first name:
> John
Enter your last name:
> Smith

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
<summary>Output (With Saved File - Same User)</summary>

```
Are you JSMITH? (Y|N)
> y

Welcome back, JSMITH
```

</details>
<br>

<details>
<summary>Output (With Saved File - Different User)</summary>

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
<br>

---

