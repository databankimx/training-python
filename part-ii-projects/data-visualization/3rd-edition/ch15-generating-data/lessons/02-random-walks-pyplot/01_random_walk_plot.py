"""Lesson 2.1 - Plotting a Random Walk"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make random walk
rw = RandomWalk()
rw.fill_walk()

# Plot the points
plt.style.use("classic")
fix, ax = plt.subplots()

ax.scatter(rw.x_values, rw.y_values, s=5)
ax.set_aspect("equal")

plt.show()
