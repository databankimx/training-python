"""Lesson 8.3"""

print("Chapter 8:")
print("Exercise 3 - Positional Versus Keyword Arguments")


def describe_pet(animal_type, pet_name):
    """Print a description of a pet by type and name"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("dog", "fido")
describe_pet("fido", "dog")
describe_pet(pet_name="fido", animal_type="dog")

# Uncomment to see the TypeError from a missing argument
# describe_pet("fido")

message = describe_pet("fish", "bubbles") #pylint: disable=assignment-from-no-return
print(message)
