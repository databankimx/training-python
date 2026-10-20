"""Lesson 1.3 - Correcting a Simple Line Graph"""

import matplotlib.pyplot as plt

# We'll create a list of x-axis values
numbers = list(range(1, 6))
# And modify the y-axis values
squares = [x ** 2 for x in numbers]

fig, ax = plt.subplots()

# Now we can specify the x-axis values instead of assuming the indices
ax.plot(numbers, squares, linewidth = 3)

ax.set_title("Squared Numbers", fontsize = 18)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params(axis = "both", labelsize = 14)

plt.show()
