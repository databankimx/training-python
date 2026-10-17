"""Lesson 3.8 - Saving Results to a File"""

import plotly.express as px
from die import Die
from relative_paths import get_path

# Create two dice (this time different numbers of sides)
dice = [Die(), Die(10)]

# Make some rolls and store in a list
results = []
for _ in range(50_000):
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
title = "Result of Rolling a D6 and a D10 50000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)

# Create a filename with extension "html"
filename = "d6d10_visualization.html"
# Get a path (just like we did in the ch 10)
filepath = get_path(filename, "Files")

# Write the figure to an HTML file
# Note: If you have plotly 5.12 installed, this will generate an encoding error.
#       Upgrade to at least 5.13
fig.write_html(filepath)
print(f"Stored file: {filepath}")
