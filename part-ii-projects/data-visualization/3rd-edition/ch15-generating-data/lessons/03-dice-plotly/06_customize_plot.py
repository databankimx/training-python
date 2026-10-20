"""Lesson 3.6 - Customizing the Graph"""

import plotly.express as px
from die import Die

# Create two dice
dice = [Die(), Die()]

# Make some rolls and store in a list
results = []
for _ in range(1000):
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
title = "Result of Rolling Two D6 Dice 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Set the 'ticks' property to ensure every column is labeled
fig.update_layout(xaxis_dtick=1)

fig.show()
