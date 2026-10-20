"""Lesson 5.2"""

print("Chapter 5:")
print("Exercise 2 - Conditional Tests")

car = "bmw"
print(f"'{car}' == 'bmw': {car == 'bmw'}")
print(f"'{car}' == 'audi': {car == 'audi'}")

car = "Audi"
print(f"'{car.lower()}' == 'audi': {car.lower() == 'audi'}")
print(f"'{car.upper()}' == 'AUDI': {car.upper() == 'AUDI'}")

requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

age = 18
print(f"{age} == 18: {age == 18}")
answer = 63
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 21
print(f"{age} < 21: {age < 21}")
print(f"{age} <= 21: {age <= 21}")
print(f"{age} > 21: {age > 21}")
print(f"{age} >= 21: {age >= 21}")

print(f"'abc' < 'def': {'abc' < 'def'}")
print(f"'abc' < 'DEF': {'abc' < 'DEF'}")
