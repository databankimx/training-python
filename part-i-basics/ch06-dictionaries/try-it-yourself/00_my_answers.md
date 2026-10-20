## Chapter 6 Try-it-Yourself Assignments and Solutions

Here are my solutions for the chapter 6 try-it-yourself exercises.

---

### Assignment 6.1 - Person

Use a dictionary to store information about a person you know. Store their
first name, last name, age, and city. Print each piece of information.

<details>
<summary>Spoiler Code</summary>

```python
person = {"first_name": "Scott", "last_name": "McLean",
          "age": 54, "city": "Lewisville"}
print(f"First Name: {person['first_name']}")
print(f"Last Name:  {person['last_name']}")
print(f"Age:        {person['age']}")
print(f"City:       {person['city']}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
First Name: Scott
Last Name:  McLean
Age:        54
City:       Lewisville
```

</details>

---

### Assignment 6.2 - Favorite Numbers

Use a dictionary to store people's favorite numbers. Five names as keys,
one favorite number each as values. Print each person's name and number.

<details>
<summary>Spoiler Code</summary>

```python
favorite_numbers = {
    "Scott": 42,
    "Andy": 37,
    "René": 343,
    "Matt": 12,
    "John": "√-1",
}
print(f"Scott's favorite number is {favorite_numbers['Scott']}")
print(f"Andy's favorite number is {favorite_numbers['Andy']}")
print(f"René's favorite number is {favorite_numbers['René']}")
print(f"Matt's favorite number is {favorite_numbers['Matt']}")
print(f"John's favorite number is {favorite_numbers['John']}")
```

</details>

---

### Assignment 6.3 - Glossary

Five programming words as keys, their meanings as values. Print each word
and its meaning neatly.

<details>
<summary>Spoiler Code</summary>

```python
coding_terms = {
    "Program": "A collection of instructions, which perform a specific task",
    "Boolean": "An expression used for statements that are TRUE or FALSE",
    "Bug": "A term used to denote an error or defect in hardware or software",
    "Object": "Combination of related variables, which can be used together.",
    "Code": "A set of instructions using the protocols of a given language",
}
print(f"\nProgram:\n{coding_terms['Program']}")
print(f"\nBoolean:\n{coding_terms['Boolean']}")
print(f"\nBug:\n{coding_terms['Bug']}")
print(f"\nObject:\n{coding_terms['Object']}")
print(f"\nCode:\n{coding_terms['Code']}")
```

</details>

---

### Assignment 6.4 - Glossary 2

Replace the series of `print()` calls with a loop. Then add five more terms -
they should appear automatically.

<details>
<summary>Spoiler Code</summary>

```python
coding_terms = { ... }  # same as 6.3

for term, definition in coding_terms.items():
    print(f"\n{term}:\n{definition}")

more_coding_terms = {
    "List": "An ordered, mutable set of objects",
    "PEP 8": "The Python Enhancement Proposal is a style guide of Python code",
    "Literal": "A data item that has a fixed value",
    "Loop": "A loop is used for iterating over a sequence",
    "Module": "A Python code file that can be imported and reused",
}
coding_terms.update(more_coding_terms)
for term, definition in coding_terms.items():
    print(f"\n{term}:\n{definition}")
```

</details>

---

### Assignment 6.5 - Rivers

Dictionary of three rivers and the country each runs through. Loop to print
a sentence about each river, each river name, and each country.

<details>
<summary>Spoiler Code</summary>

```python
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "mississippi": "united states",
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")
for river in rivers:
    print(river.title())
for country in rivers.values():
    print(country.title())
```

</details>
<br>

<details>
<summary>Output</summary>

```
The Nile runs through Egypt
The Amazon runs through Brazil
The Mississippi runs through United States

Nile
Amazon
Mississippi

Egypt
Brazil
United States
```

</details>

---

### Assignment 6.6 - Polling

Make a list of people who should take the languages poll. Thank those who
have taken it; invite those who haven't.

<details>
<summary>Spoiler Code</summary>

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
people = ["jen", "sarah", "adam", "edward", "eleanor", "phil"]
for name in people:
    if name in favorite_languages:
        print(f"Hi {name.title()}! Thanks for taking the poll.")
    else:
        print(f"Hi {name.title()}, please take the poll.")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Hi Jen! Thanks for taking the poll.
Hi Sarah! Thanks for taking the poll.
Hi Adam, please take the poll.
Hi Edward! Thanks for taking the poll.
Hi Eleanor, please take the poll.
Hi Phil! Thanks for taking the poll.
```

</details>

---

### Assignment 6.7 - People

Make two more person dictionaries, store all three in a list called `people`.
Loop through and print everything about each person.

<details>
<summary>Spoiler Code</summary>

```python
person1 = {"first_name": "Scott", "last_name": "McLean", "age": 52, "city": "Lewisville"}
person2 = {"first_name": "Jeremy", "last_name": "McLean", "age": 47, "city": "Columbus"}
person3 = {"first_name": "Hillary", "last_name": "Taylor", "age": 50, "city": "Twinsburg"}
people = [person1, person2, person3]
for person in people:
    print()
    for key, value in person.items():
        print(f"{key} = {value}")
```

</details>

---

### Assignment 6.8 - Pets

Several dictionaries each representing a pet. Store in a list called `pets`.
Loop through and print everything about each pet.

<details>
<summary>Spoiler Code</summary>

```python
charlie = {"animal": "dog", "owner": "talia"}
orville = {"animal": "guinea pig", "owner": "scott"}
bronte = {"animal": "cat", "owner": "melissa"}
pets = [charlie, orville, bronte]
for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['animal']}")
```

</details>
<br>

<details>
<summary>Output</summary>

```
Talia owns a dog
Scott owns a guinea pig
Melissa owns a cat
```

</details>

---

### Assignment 6.9 - Favorite Places

Dictionary called `favorite_places`. Three names as keys, one to three places
per person as a list. Loop through and print each person's name and places.

<details>
<summary>Spoiler Code</summary>

```python
favorite_places = {
    "scott": ["ireland", "spain", "mexico"],
    "matt": ["puerto rico"],
    "pat": ["minnesota", "scotland"],
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places include:")
    for place in places:
        print(f"\t{place.title()}")
```

</details>

---

### Assignment 6.10 - Favorite Numbers

Modify Exercise 6.2 so each person can have more than one favorite number.
Print each person's name and their numbers.

<details>
<summary>Spoiler Code</summary>

```python
favorite_numbers = {
    "Scott": [42, 73],
    "Sean": [13, 42],
    "Andy": [37],
    "Rene": [1, 2, 343],
    "Matt": [12, 6, 4, 3],
    "John": ["i", "√-1"],
}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers include:")
    for number in numbers:
        print(f"\t{number}")
```

</details>

---

### Assignment 6.11 - Cities

Dictionary called `cities`. Three city names as keys. Each value is a
dictionary with country, population, and one fact.

<details>
<summary>Spoiler Code</summary>

```python
cities = {
    "cleveland": {
        "country": "united states",
        "population": 383_331,
        "fact": "Home of the Rock & Roll Hall of Fame"
    },
    "london": {
        "country": "england",
        "population": 8_982_000,
        "fact": "Hosted the 2012 Summer Olympics"
    },
    "ensenada": {
        "country": "mexico",
        "population": 443_807,
        "fact": "Known as the 'Capital del vino Mexicano' (Capital of Mexican wine)"
    },
}
for city, facts in cities.items():
    print(f"\n{city.title()}")
    for heading, fact in facts.items():
        if heading == "country":
            fact = fact.title()
        print(f"\t{heading.upper()}:\n\t\t{fact}")
```

</details>

---

### Assignment 6.12 - Extensions

Use one of the example programs from this chapter and extend it.

<details>
<summary>Spoiler Code</summary>

```python
# As homework, try doing this assignment yourself.
```

</details>

---
