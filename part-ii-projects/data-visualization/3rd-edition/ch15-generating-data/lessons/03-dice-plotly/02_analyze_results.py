"""Lesson 3.2 - Analyzing Results"""

from die import Die

die = Die()

results = []
for _ in range(1000):
    results.append(die.roll())

# Process the results and stash the number of times each value occurs in a new list
frequencies = []
poss_results = range(1, die.num_sides + 1)
for n in poss_results:
    frequency = results.count(n)
    frequencies.append(frequency)

print(frequencies)
