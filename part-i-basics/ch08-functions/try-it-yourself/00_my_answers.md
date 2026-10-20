## Chapter 8 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 8 try-it-yourself exercises.

---

### Assignment 8.1 - Message

Write a function called display_message() that prints one sentence telling 
everyone what you are learning about in this chapter. Call the function, and 
make sure the message displays correctly.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def display_message():
    print("I am learning about Python functions.")

display_message()
```

</details>
<br>

<details>
<summary>Output</summary>

```
I am learning about Python functions.
```

</details>

---

### Assignment 8.2 - Favorite Book

Write a function called `favorite_book()` that accepts one parameter, 
`title`. The function should print a message, such as  
`One of my favorite books is Alice in Wonderland.`  
Call the function, making sure to include a book title as an argument in the 
function call.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Snow Crash")
```

</details>
<br>

<details>
<summary>Output</summary>

```
One of my favorite books is Snow Crash.
```

</details>

---

### Assignment 8.3 - T-Shirt

Write a function called `make_shirt()` that accepts a `size` and the text of 
a `message` that should be printed on the shirt. The function should print a 
sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. Call the 
function a second time using keyword arguments.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def make_shirt(size, message):
    """Print a message describing a shirt order"""
    print(f"You ordered a {size} t-shirt saying '{message}'.")

my_size = "large"
my_message = "I ♥ Python"
make_shirt(my_size, my_message)
make_shirt(message=my_message, size=my_size)
```

</details>
<br>

<details>
<summary>Output</summary>

```
You ordered a large t-shirt saying 'I ♥ Python'.
You ordered a large t-shirt saying 'I ♥ Python'.
```

</details>

---

### Assignment 8.4 - Large Shirts

Modify the `make_shirt()` function so that shirts are large by default with a 
message that reads `I love Python`. Make a large shirt and a medium shirt 
with the default message, and a shirt of any size with a different message.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def make_shirt(size="large", message="I ♥ Python"):
    """Print a message describing a shirt order"""
    print(f"You ordered a {size} t-shirt saying '{message}'.")

my_size = "medium"
my_message = "I ♥ Coding"
make_shirt()
make_shirt(size=my_size)
make_shirt(message=my_message)
```

</details>
<br>

<details>
<summary>Output</summary>

```
You ordered a large t-shirt saying 'I ♥ Python'.
You ordered a medium t-shirt saying 'I ♥ Python'.
You ordered a large t-shirt saying 'I ♥ Coding'.
```

</details>

---

### Assignment 8.5 - Cities

Write a function called `describe_city()` that accepts the name of a city and 
its country. The function should print a simple sentence, such as:  
`Reykjavik is in Iceland.`  
Give the parameter for the country a default value. Call your function for 
three different cities, at least one of which is not in the default country.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def describe_city(city, country="united states"):
    """Print a description of a city"""
    prefix = ""
    if country.lower() == "united states":
        prefix = "the "
    print(f"{city.title()} is in {prefix}{country.title()}")

describe_city("dallas")
describe_city("cleveland")
describe_city("ensenada", "mexico")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Dallas is in the United States
Cleveland is in the United States
Ensenada is in Mexico
```

</details>

---

### Assignment 8.6 - City Names

Write a function called `city_country()` that takes in the name of a city and 
its country. The function should return a string formatted like this:  
`Santiago, Chile`  
Call your function with at least three city-country pairs, and print the 
values that are returned.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def city_country(city, country):
    """Return a string formatted as 'City, Country'"""
    return f"{city.title()}, {country.title()}"

place = city_country("ensenada", "mexico")
print(place)

place = city_country("dublin", "ireland")
print(place)

place = city_country("vienna", "austria")
print(place)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Ensenada, Mexico
Dublin, Ireland
Vienna, Austria
```

</details>

---

### Assignment 8.7 - Album

Write a function called `make_album()` that builds a dictionary describing a 
music album. The function should take in an artist name and an album title, 
and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the dictionaries are storing the album 
information correctly.

Use `None` to add an optional parameter to `make_album()` that allows you to 
store the number of songs on an album. If the calling line includes a value 
for the number of songs, add that value to the album's dictionary. Make at 
least one new function call that includes the number of songs on an album.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def make_album(artist, album, songs=None):
    """Return a dictionary describing a music album"""
    album = {"Artist": artist.title(), "Title": album.title()}
    if songs:
        album["Tracks"] = songs
    return album

album = make_album("pink floyd", "animals")
print(album)
album = make_album("simon & garfunkel", "sounds of silence")
print(album)
album = make_album("they might be giants", "flood")
print(album)
album = make_album("john prine", "fair & square", 14)
print(album)
```

</details>
<br>

<details>
<summary>Output</summary>

```
{'Artist': 'Pink Floyd', 'Title': 'Animals'}
{'Artist': 'Simon & Garfunkel', 'Title': 'Sounds Of Silence'}
{'Artist': 'They Might Be Giants', 'Title': 'Flood'}
{'Artist': 'John Prine', 'Title': 'Fair & Square', 'Tracks': 14}
```

</details>

---

### Assignment 8.8 - User Albums

Start with your program from Exercise 8.7. Write a while loop that allows 
users to enter an album's artist and title. Once you have that information, 
call `make_album()` with the user's input and print the dictionary that's 
created. Be sure to include a quit value in the while loop.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def make_album(artist, album, songs=None):
    """Return a dictionary describing a music album"""
    album = {"Artist": artist.title(), "Title": album.title()}
    if songs:
        album["Tracks"] = songs
    return album


while True:
    print("\nPlease tell me about your album:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == "q":
        break

    title = input("Album Title: ")
    if title == "q":
        break

    album = make_album(artist, title)
    print(f"\n{album}!")
```

</details>

---

### Assignment 8.9 - Messages

Make a list containing a series of short text messages. Pass the list to a function called `show_messages()`, which prints each text message.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def show_messages(messages):
    """Print each message from the list"""
    for message in messages:
        print(message)

messages = ["Hi there!", "Having fun at code camp!", "Python is great!"]
show_messages(messages)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Hi there!
Having fun at code camp!
Python is great!
```

</details>

---

### Assignment 8.10 - Sending Messages

Start with a copy of your program from Exercise 8.9. Write a function called 
`send_messages()` that prints each text message and moves each message to a 
new list called `sent_messages` as it's printed. After calling the function, 
print both of your lists to make sure the messages were moved correctly.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def send_messages(messages, sent_messages):
    """Move messages to sent_messages list"""
    while messages:
        message = messages.pop(0)
        print(f"Sending message: {message}")
        sent_messages.append(message)


messages = ["Hi there!", "Having fun at code camp!", "Python is great!"]
sent_messages = []
send_messages(messages, sent_messages)
print("Messages:\n", messages)
print("Sent Messages:\n", sent_messages)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Sending message: Hi there!
Sending message: Having fun at code camp!
Sending message: Python is great!
Messages:
 []
Sent Messages:
 ['Hi there!', 'Having fun at code camp!', 'Python is great!']
```

</details>

---

### Assignment 8.11 - Archived Messages

Start with your work from Exercise 8.10. Call the function `send_messages()` with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def send_messages(messages, sent_messages):
    """Move messages to sent_messages list"""
    while messages:
        message = messages.pop(0)
        print(f"Sending message: {message}")
        sent_messages.append(message)

messages = ["Hi there!", "Having fun at code camp!", "Python is great!"]
sent_messages = []
send_messages(messages[:], sent_messages)
print("Messages:\n", messages)
print("Sent Messages:\n", sent_messages)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Sending message: Hi there!
Sending message: Having fun at code camp!
Sending message: Python is great!
Messages:
 ['Hi there!', 'Having fun at code camp!', 'Python is great!']
Sent Messages:
 ['Hi there!', 'Having fun at code camp!', 'Python is great!']
```

</details>

---

### Assignment 8.12 - Sandwiches

Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the 
function call provides, and it should print a summary of the sandwich that's 
being ordered. Call the function three times, using a different number of 
arguments each time.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def make_sandwich(*toppings):
    """List out the provided sandwich toppings"""
    print("Making a sandwich with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

make_sandwich("corned beef", "sauerkraut")
make_sandwich("pastrami", "onions", "mustard")
make_sandwich("salami", "swiss cheese", "lettuce", "tomato", "mayonnaise")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Making a sandwich with the following toppings:
 - corned beef
 - sauerkraut
Making a sandwich with the following toppings:
 - pastrami
 - onions
 - mustard
Making a sandwich with the following toppings:
 - salami
 - swiss cheese
 - lettuce
 - tomato
 - mayonnaise
```

</details>

---

### Assignment 8.13 - User Profile

Start with a copy of
[`user_profile.py`](../textbook-downloads/3rd-edition/lessons/user_profile.py). Build a profile of yourself by calling `build_profile()`, using your first and last names and three other key-value pairs that describe you.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def build_profile(first, last, **user_info):
    """Populate a user-profile dictionary"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

me = build_profile("scott", "mclean",
                   profession="programmer",
                   avocation="musician",
                   hobby="cobbler")
print(me)
```

</details>
<br>

<details>
<summary>Output</summary>

```
{'profession': 'programmer', 'avocation': 'musician', 'hobby': 'cobbler', 'first_name': 'scott', 'last_name': 'mclean'}
```

</details>

---

### Assignment 8.14 - Cars

Write a function that stores information about a car in a dictionary. The 
function should always receive a manufacturer and a model name. It should 
then accept an arbitrary number of keyword arguments.

Call the function with the required information and two other name-value 
pairs, such as a color or an optional feature. Your function should work for 
a call like this one:

```python
car = make_car("subaru", "outback", color = "blue", tow_package = True)
```

Print the dictionary that's returned to make sure all the information was 
stored correctly.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
def make_car(make, model, **details):
    """Create a dictionary describing a car"""
    details["Make"] = make.title()
    details["Model"] = model.title()
    return details

car = make_car("dodge", "challenger", color="header orange",
               feature="shaker", year=2014)
print(car)
```

</details>
<br>

<details>
<summary>Output</summary>

```
{'color': 'header orange', 'feature': 'shaker', 'year': 2014, 'Make': 'Dodge', 'Model': 'Challenger'}
```

</details>

---

### Assignment 8.15 - Printing Models

Put the functions for the example
[`printing_models.py`](../textbook-downloads/3rd-edition/lessons/printing_models.py) in a 
separate file called `printing_functions.py`. Write an import statement at 
the top of `printing_models.py`, and modify the file to use the imported
functions.

Solution:

<details>
<summary>Spoiler Code</summary>

[printing_functions.py](./printing_functions.py)

```python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
```

Calling Code

```python
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
```

</details>
<br>

<details>
<summary>Output</summary>

```
Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case

The following models have been printed:
dodecahedron
robot pendant
phone case
```

</details>

---

### Assignment 8.16 - Imports

Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches: 

* `import module_name`
* `from module_name import function_name`
* `from module_name import function_name as fn`
* `import module_name as alias`
* `from module_name import *`

Solution:

<details>
<summary>Spoiler Code</summary>

[`album.py`](./album.py)

```python
def make_album(artist, album, songs = None):
    album = {"Artist": artist.title(), "Title": album.title()}
    if songs:
        album["Tracks"] = songs
    return album
```

Calling Code

```python
import album
import album as a
from album import make_album
from album import make_album as ma
from album import *

my_album = album.make_album("Pink Floyd", "Dark Side of the Moon")
print(my_album)

my_album = a.make_album("Fleetwood Mac", "Rumors")
print(my_album)

my_album = make_album("David Bowie", "The Rise and Fall of Ziggy Stardust")
print(my_album)

my_album = ma("The Beatles", "Abbey Road")
print(my_album)
```

</details>
<br>

<details>
<summary>Output</summary>

```
{'Artist': 'Pink Floyd', 'Title': 'Dark Side Of The Moon'}
{'Artist': 'Fleetwood Mac', 'Title': 'Rumors'}
{'Artist': 'David Bowie', 'Title': 'The Rise And Fall Of Ziggy Stardust'}
{'Artist': 'The Beatles', 'Title': 'Abbey Road'}
```

</details>

---

### Assignment 8.17 - Styling Functions

Choose any three programs you wrote for this chapter, and make sure they 
follow the styling guidelines described in this section.

Solution:

<details>
<summary>Spoiler Code</summary>

```python
# Code will be in other solutions
print("Perform this exercise on your own to check your comprehension")
```

</details>

---
