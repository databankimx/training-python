"""Lesson 3.4 - Improving the Graph"""

from die import Die
import plotly.express as px
# python -m pip install plotly.express

die = Die()

results = []
for _ in range(1000):
    results.append(die.roll())

frequencies = []
poss_results = range(1, die.num_sides + 1)
for n in poss_results:
    frequency = results.count(n)
    frequencies.append(frequency)

# Visualize results

# Create title and labels and add them to the plot
title = "Result of Rolling One D6 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.show()
