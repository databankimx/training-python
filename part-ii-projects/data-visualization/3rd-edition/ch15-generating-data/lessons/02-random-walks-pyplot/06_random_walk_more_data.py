"""Lesson 2.6 - Adding More Data Points to a Random Walk"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Increase the number of data points
    rw = RandomWalk(20_000)
    rw.fill_walk()

    plt.style.use("classic")
    fix, ax = plt.subplots()
    # pylint: disable=no-member
    ax.scatter(rw.x_values, rw.y_values, s=5, c=range(rw.num_points),
               cmap=plt.cm.viridis, edgecolors="none")
    ax.set_aspect("equal")
    ax.scatter(0, 0, color=(0, .9, 0), edgecolors="none", s=25)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=25)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    again = input("Make another walk? (y/n): ")
    if again and again.lower()[0] != "y":
        break
