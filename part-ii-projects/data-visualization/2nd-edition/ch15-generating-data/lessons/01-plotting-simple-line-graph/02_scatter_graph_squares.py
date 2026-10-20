"""Lesson 1.2 - Plotting a Simple Scatter Graph"""

import os
import matplotlib.pyplot as plt

ROOT_DIR = os.path.dirname(__file__)

max_x = 1000

x_values = range(1, max_x + 1)
y_values = [x ** 2 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
# pylint: disable=no-member
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Set size of tick labels.
ax.tick_params(axis = "both", which = "major", labelsize = 14)
# Using the 'plain' ticklabel format will prevent expressing our y-axis in scientific notation
ax.ticklabel_format(style = "plain")

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

file_path = os.path.join(ROOT_DIR, "files", "squares_plot.png")
plt.savefig(file_path, bbox_inches = "tight")
plt.show()
