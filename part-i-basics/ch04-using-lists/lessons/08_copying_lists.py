"""Lesson 4.8"""

print("Chapter 4:")
print("Exercise 8 - Copying Lists")

my_foods = ["pizza", "falafel", "carrot cake"]
print(f"My favorite foods are:          {my_foods}")
friend_foods = my_foods[:]
print(f"My friend's favorite foods are: {friend_foods}")

my_foods.append("cannoli")
friend_foods.append("ice cream")
print(f"My favorite foods are:          {my_foods}")
print(f"My friend's favorite foods are: {friend_foods}")

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods
my_foods.append("cannoli")
friend_foods.append("ice cream")

print(f"My favorite foods are:          {my_foods}")
print(f"My friend's favorite foods are: {friend_foods}")
