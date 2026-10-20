"""Lesson 6.13"""

print("Chapter 6:")
print("Exercise 13 - Nesting Lists in a Dictionary")

pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

if pizza["toppings"]:
    print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
    for topping in pizza["toppings"]:
        print(f"\t{topping}")
else:
    print(f"You ordered a {pizza['crust']}-crust plain pizza")

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell", "rust"],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")
