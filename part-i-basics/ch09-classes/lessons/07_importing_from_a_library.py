"""Lesson 9.7"""

from random import randint, choice
from sm_utils import pause

print("Chapter 9:")
print("Exercise 7 - Importing Random from the Python Standard Library\n")

dice = [randint(1, 6), randint(1, 6)]
print(f"You rolled {sum(dice)}\n")

players = ["charles", "martina", "michael", "florence", "eli"]
first_up = choice(players)
print(f"First Up: {first_up.title()}")

# Wait until user hits enter to proceed
pause()
print("Done...")
