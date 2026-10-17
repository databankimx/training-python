"""Lesson 3.1 - Rolling a D6"""

from die import Die

# Create a D6
die = Die()

# Roll a few times and store in a list
results = []
for _ in range(100):
    results.append(die.roll())

print(results)
