"""Lesson 8.4"""

print("Chapter 8:")
print("Exercise 4 - Default Parameter Values")

def describe_pet_def(pet_name, animal_type="dog"):
    """Print a description of a pet by type and name"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_def("willie")
describe_pet_def(pet_name = "willie")

describe_pet_def("harry", "hamster")
describe_pet_def(pet_name="harry", animal_type="hamster")
