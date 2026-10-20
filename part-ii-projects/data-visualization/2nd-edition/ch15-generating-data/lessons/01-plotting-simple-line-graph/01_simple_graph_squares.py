"""Lesson 1.1 - Plotting a Simple Line Graph"""

# matplotlib provides graphing/charting capabilities
# Samples here: https://matplotlib.org/gallery/
# You may need to run the following to get this to work
# > python -m pip install matplotlib

import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")
input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
squares = [value ** 2 for value in input_values]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Set size of tick labels.
ax.tick_params(axis = "both", labelsize = 14)

plt.show()
