"""Lesson 2.2 - Plotting a Random Walk Multiple Times"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make random walks until user decides to quit
while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("classic")
    fix, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=5)
    ax.set_aspect("equal")

    plt.show()

    again = input("Make another walk? (y/n): ")
    if again and again.lower()[0] != "y":
        break
