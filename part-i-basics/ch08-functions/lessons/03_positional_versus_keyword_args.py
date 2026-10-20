"""Lesson 8.3"""

print("Chapter 8:")
print("Exercise 3 - Positional Versus Keyword Arguments")

def describe_pet(animal_type, pet_name):
    """Print a description of a pet by type and name"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("hamster", "harry")
describe_pet("dog", "willie")

describe_pet("harry", "hamster")

describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="willie", animal_type="dog")

# This will result in a TypeError
# describe_pet("augie")

message1, message2 = describe_pet("cat", "reginald"), describe_pet("fish", "bubbles")
print("\n", message1, message2)
