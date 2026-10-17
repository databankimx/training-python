"""Assignment 15.08"""
# Multiplication: When you roll two dice, you usually add the two numbers together
#                 to get the result. Create a visualization that shows what happens
#                 if you multiply these numbers instead.

import os
from plotly.graph_objs import Bar, Layout
from plotly import offline
from numpy import prod
from die import Die

print("Try-it-Yourself:")
print("Assignment 15.8")

# Create 2d6
settings = {"num": 2, "sides": 6, "rolls": 10_000}
dice = []
for n in range(settings["num"]):
    dice.append(Die(settings["sides"]))

# Make some rolls and store the results in a list
results = []
for roll in range(settings["rolls"]):
    results.append(prod([die.roll() for die in dice]))

# Analyze the results
frequencies = []
max_value =  settings["sides"] ** settings["num"]
frequencies = [results.count(value) for value in range(len(dice) - 1, max_value + 1)]

# Visualize the results
x_values = list(range(settings["num"] - 1, max_value + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
suffix = "" if settings["rolls"] == 1 else "s"
heading = f"Results of rolling {settings['num']} D{dice[1].num_sides} " + \
    f"{settings['rolls']} time{suffix}"
my_layout = Layout(title = heading, xaxis = x_axis_config, yaxis = y_axis_config)
ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", f"multiply_{settings['num']}_D{settings['sides']}.html")
offline.plot({"data": data, "layout": my_layout}, filename = file_path)
