"""Assignment 15.02"""
# Colored Cubes: Apply a colormap to your cubes plot.

import matplotlib.pyplot as plt

print("Try-it-Yourself:")
print("Assignment 15.2")

# max_x = 5
max_x = 5_000

x_values = range(1, max_x + 1)
y_values = [value ** 3 for value in x_values]

plt.style.use("bmh")
fig, ax = plt.subplots()
# pylint: disable=no-member
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Reds, s = 5)
# ax.scatter(x_values, y_values, c = y_values, s = 5)

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize = 16)
ax.set_xlabel("Value", fontsize = 10)
ax.set_ylabel("Cube of Value", fontsize = 10)

# Set size of tick labels.
ax.tick_params(axis = "both", which = "major", labelsize = 8)
# Using the 'plain' ticklabel format will prevent expressing our y-axis in scientific notation
ax.ticklabel_format(style = "plain")

# Set the range for each axis.
ax.axis([0, 5_000, 0, 125_000_000_000])

plt.show()
