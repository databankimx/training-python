"""Lesson 1.9 - Customizing a Scatter Graph"""

import matplotlib.pyplot as plt

# Increase the size of the data lists
numbers = list(range(1, 1001))
squares = [x ** 2 for x in numbers]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

# Set the point color using the color argument (can use name or RGB values tuple
#    where the values range from 0.0 to 1.0)
# ax.scatter(numbers, squares, s=10, color="red")
# ax.scatter(numbers, squares, s=10, color=(0.85, 0, 0))

# Or set a color map instead of a single color (which provides a kind of gradient of colors)
# c sets which axis values are reflected in the map, and cmap which map to use
# List of color maps: https://matplotlib.org/stable/tutorials/colors/colormaps.html
# pylint: disable=no-member
ax.scatter(numbers, squares, s=10, c=squares, cmap=plt.cm.viridis)

ax.set_title("Squared Numbers", fontsize = 18)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params(axis = "both", labelsize = 14)
ax.axis([0, 1_000, 0, 1_000_000])

# Customize the tick labels
ax.ticklabel_format(style="plain")

plt.show()
