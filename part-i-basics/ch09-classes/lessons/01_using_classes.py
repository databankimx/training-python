"""Lesson 9.1"""

print("Chapter 9:")
print("Exercise 1 - Creating and Using a Class")

class Dog:
    """This is a simple model for a dog"""

    def __init__(self, name, age):
        """Initialize a new instance of the Dog class"""
        self.name = name.title()
        self.age = age

    def sit(self):
        """Tell the Dog to sit"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Tell the Dog to roll over"""
        print(f"{self.name} has rolled over.")

my_dog = Dog("fido", 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

print()

my_dog = Dog("rover", 6)
your_dog = Dog("lucy", 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()
