"""Assignment 15.09"""
# Die Comprehensions: For clarity, the listings in this section use the long form
#                     of for loops. If you're comfortable using list comprehensions,
#                     try writing a comprehension for one or both of the loops in
#                     each of these programs.

import plotly.express as px
from die import Die
from numpy import prod

print("Try-it-Yourself:")
print("Assignment 15.9")

settings = {
    "num_dice": 2,
    "rolls": 1000,
    "sides": 6
}

# Create three dice
dice = [Die(settings["sides"]) for _ in range(settings["num_dice"])]

# Make some rolls and store in a list
results = [prod([d.roll() for d in dice]) for _ in range(settings["rolls"])]

# Analyze the results
max_result = prod([d.num_sides for d in dice])
poss_results = range(settings["num_dice"], max_result + 1)
frequencies = [results.count(n) for n in poss_results]

# Visualize results
title = f"Result of Rolling {len(dice)} D{dice[0].num_sides} {settings['rolls']} Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

fig.show()
