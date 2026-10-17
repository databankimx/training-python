"""Assignment 15.08"""
# Multiplication: When you roll two dice, you usually add the two numbers together
#                 to get the result. Create a visualization that shows what happens
#                 if you multiply these numbers instead.

import plotly.express as px
# I am implementing this for access to the prod() method - a bit of a cheat... sue me.
from numpy import prod
from die import Die

print("Try-it-Yourself:")
print("Assignment 15.8")

settings = {
    "num_dice": 2,
    "rolls": 1000,
    "sides": 6
}

# Create three dice
dice = [Die(settings["sides"]) for _ in range(settings["num_dice"])]

# Make some rolls and store in a list
results = []
for _ in range(settings["rolls"]):
    result = prod([d.roll() for d in dice])
    results.append(result)

# Analyze the results
max_result = prod([d.num_sides for d in dice])
poss_results = range(settings["num_dice"], max_result + 1)
frequencies = []
for n in poss_results:
    frequency = results.count(n)
    frequencies.append(frequency)

# Visualize results
title = f"Result of Rolling {len(dice)} D{dice[0].num_sides} {settings['rolls']} Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

fig.show()
