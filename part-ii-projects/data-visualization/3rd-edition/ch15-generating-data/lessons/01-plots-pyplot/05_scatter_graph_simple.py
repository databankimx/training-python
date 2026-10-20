"""Lesson 1.5 - A Simple Scatter Graph"""

import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

# For a scatter graph, use ax.scatter() instead of ax.plot()
# Here, we're passing a single point (x=2, y=4)
ax.scatter(2, 4)

plt.show()
