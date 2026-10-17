"""Assignment 15.03"""
# Molecular Motion: Modify rw_visual.py by replacing ax.scatter() with ax.plot().
#                   To simulate the path of a pollen grain on the surface of a drop
#                   of water, pass in the rw.x_values and rw.y_values, and include
#                   a linewidth argument. Use 5000 instead of 50,000 points.

import matplotlib.pyplot as plt
from random_walk import RandomWalk

print("Try-it-Yourself:")
print("Assignment 15.3")

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("seaborn-v0_8")
    fix, ax = plt.subplots(figsize=(16, 9))
    ax.plot(rw.x_values, rw.y_values, color="gray", linewidth=2, zorder=1)
    ax.set_aspect("equal")
    # I added the zorder argument to make sure the dots appear on top of the line ploy
    ax.scatter(0, 0, color=(0, .8, 0), edgecolors="none", s=75, zorder=2, marker="*")
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none",
               s=75, zorder=3, marker="*")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    again = input("Make another walk? (y/n): ")
    if again and again.lower()[0] != "y":
        break
