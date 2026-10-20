"""Lesson 1.7 - Adding Data to a Scatter Graph"""

import matplotlib.pyplot as plt

# Add back in some data lists
numbers = list(range(1, 6))
squares = [x ** 2 for x in numbers]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

# Change from a point to the lists for the plot
ax.scatter(numbers, squares, s=100)
ax.set_title("Squared Numbers", fontsize = 18)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params(axis = "both", labelsize = 14)

plt.show()
