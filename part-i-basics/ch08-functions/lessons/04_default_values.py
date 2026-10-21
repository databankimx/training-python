"""Lesson 8.4"""

print("Chapter 8:")
print("Exercise 4 - Default Parameter Values")


def describe_pet_def(pet_name, animal_type="dog"):
    """Print a description of a pet by type and name"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet_def("rover")
describe_pet_def(pet_name="rover")

describe_pet_def("pickles", "cat")
describe_pet_def(pet_name="pickles", animal_type="cat")
