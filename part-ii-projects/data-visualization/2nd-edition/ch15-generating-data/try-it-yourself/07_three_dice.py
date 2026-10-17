"""Assignment 15.07"""
# Three Dice: When you roll three D6 dice, the smallest number you can roll is 3
#             and the largest number is 18.
#             Create a visualization that shows what happens when you roll three D6 dice.

import os
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

print("Try-it-Yourself:")
print("Assignment 15.7")

# Create 3d6
settings = {"num": 3, "sides": 6, "rolls": 10_000}
dice = []
for n in range(settings["num"]):
    dice.append(Die(settings["sides"]))

# Make some rolls and store the results in a list
results = []
for roll in range(settings["rolls"]):
    results.append(sum([die.roll() for die in dice]))

# Analyze the results
frequencies = []
max_value = settings["num"] * settings["sides"]
frequencies = [results.count(value) for value in range(len(dice), max_value + 1)]

# Visualize the results
x_values = list(range(settings["num"], max_value + 1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
suffix = "" if settings["rolls"] == 1 else "s"
heading = f"Results of rolling {settings['num']} D{dice[1].num_sides} " + \
    f"{settings['rolls']} time{suffix}"
my_layout = Layout(title = heading, xaxis = x_axis_config, yaxis = y_axis_config)
ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "Files", f"sum_{settings['num']}_d{settings['sides']}.html")
offline.plot({"data": data, "layout": my_layout}, filename = file_path)
