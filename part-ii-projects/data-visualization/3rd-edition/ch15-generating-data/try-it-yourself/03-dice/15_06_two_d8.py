"""Assignment 15.06"""
# Two D8s: Create a simulation showing what happens when you roll two eight-sided
#          dice 1000 times. Try to picture what you think the visualization will
#          look like before you run the simulation; then see if your intuition was
#          correct. Gradually increase the number of rolls until you start to see
#          the limits of your system’s capabilities.

import plotly.express as px
from die import Die

print("Try-it-Yourself:")
print("Assignment 15.6")

# Create two dice
dice = [Die(8)] * 2
rolls = 1_000

# Make some rolls and store in a list
results = []
for _ in range(rolls):
    result = dice[0].roll() + dice[1].roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = sum([d.num_sides for d in dice])
poss_results = range(2, max_result + 1)

for n in poss_results:
    frequency = results.count(n)
    frequencies.append(frequency)

# Visualize results
title = f"Result of Rolling Two D8 {rolls} Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

fig.show()
