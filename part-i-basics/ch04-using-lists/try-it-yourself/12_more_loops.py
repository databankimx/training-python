"""Assignment 4.12"""

# More Loops: Choose a version of foods.py and write two for loops
#             to print each list of foods.

print("Try-it-Yourself:")
print("Assignment 4.12")

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for food in my_foods:
    print(f" - {food}")
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f" - {food}")
