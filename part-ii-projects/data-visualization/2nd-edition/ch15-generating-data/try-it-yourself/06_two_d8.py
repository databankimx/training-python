"""Assignment 15.06"""
# Two D8s: Create a simulation showing what happens when you roll two eight-sided
#          dice 1000 times. Try to picture what you think the visualization will
#          look like before you run the simulation; then see if your intuition was
#          correct. Gradually increase the number of rolls until you start to see
#          the limits of your system's capabilities.

import os
from plotly import offline
from plotly.graph_objs import Bar, Layout
from die import Die

print("Try-it-Yourself:")
print("Assignment 15.6")


# Create 2d8
dice = [Die(8), Die(8)]
roll_count = 1_000

# Make some rolls and store the results in a list
results = []
for roll_num in range(roll_count):
    result = 0
    for die in dice:
        result += die.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = 0
for die in dice:
    max_result += die.num_sides
for value in range(len(dice), max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
heading = f"Results of rolling two D{dice[0].num_sides} {roll_count} times"
my_layout = Layout(title=heading, xaxis=x_axis_config, yaxis=y_axis_config)
ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(
    ROOT_DIR, "Files", f"D{dice[0].num_sides}_D{dice[1].num_sides}.html")
offline.plot({"data": data, "layout": my_layout}, filename=file_path)
