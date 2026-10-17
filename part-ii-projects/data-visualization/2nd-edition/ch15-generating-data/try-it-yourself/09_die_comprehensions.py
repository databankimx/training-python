"""Assignment 15.09"""
# Die Comprehensions: For clarity, the listings in this section use the long form
#                     of for loops. If you're comfortable using list comprehensions,
#                     try writing a comprehension for one or both of the loops in
#                     each of these programs.

import os
from plotly import offline
from plotly.graph_objs import Bar, Layout
from die import Die
print("Try-it-Yourself:")
print("Assignment 15.9")


# Dice settings
settings = {
    "num": 4,
    "sides": 6,
    "rolls": 10_000
}
settings["max_value"] = settings["num"] * settings["sides"]

# Create 4d6
dice = [Die(settings["sides"]) for _ in range(settings["num"])]

# Make some rolls and store the results in a list
results = [sum([die.roll() for die in dice]) for _ in range(settings["rolls"])]

# Analyze the results
frequencies = [results.count(value) for value in range(
    len(dice), settings["max_value"] + 1)]

# Visualize the results
x_values = list(range(settings["num"], settings["max_value"] + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
suffix = "" if settings["rolls"] == 1 else "s"
heading = f"Results of rolling {settings['num']} D{dice[1].num_sides} " + \
    f"{settings['rolls']} time{suffix}"
my_layout = Layout(title=heading, xaxis=x_axis_config, yaxis=y_axis_config)
ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(
    ROOT_DIR, "Files", f"multiply_{settings['num']}_D{settings['sides']}.html")
offline.plot({"data": data, "layout": my_layout}, filename=file_path)
