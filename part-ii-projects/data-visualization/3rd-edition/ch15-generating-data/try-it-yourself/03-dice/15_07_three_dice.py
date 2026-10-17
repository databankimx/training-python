"""Assignment 15.07"""
# Three Dice: When you roll three D6 dice, the smallest number you can roll is 3
#             and the largest number is 18. Create a visualization that shows what
#             happens when you roll three D6 dice.

import plotly.express as px
from die import Die

print("Try-it-Yourself:")
print("Assignment 15.7")

num_dice = 3
rolls = 1_000

# Create three dice
dice = [Die()] * num_dice

# Make some rolls and store in a list
results = []
for _ in range(rolls):
    result = sum([d.roll() for d in dice])
    results.append(result)

# Analyze the results
frequencies = []
max_result = sum([d.num_sides for d in dice])
poss_results = range(num_dice, max_result + 1)

for n in poss_results:
    frequency = results.count(n)
    frequencies.append(frequency)

# Visualize results
title = f"Result of Rolling {len(dice)} D{dice[0].num_sides} {rolls} Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

fig.show()
