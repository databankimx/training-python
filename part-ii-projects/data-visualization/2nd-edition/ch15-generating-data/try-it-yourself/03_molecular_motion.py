"""Assignment 15.03"""
# Molecular Motion: Modify rw_visual.py by replacing ax.scatter() with ax.plot().
#                   To simulate the path of a pollen grain on the surface of a
#                   drop of water, pass in the rw.x_values and rw.y_values, and
#                   include a linewidth argument. Use 5000 instead of 50,000 points.

import matplotlib.pyplot as plt
from random_walk import RandomWalk

print("Try-it-Yourself:")
print("Assignment 15.3")

num_points = 5_000

while True:
    # Make a random walk
    rw = RandomWalk(num_points)

    # Plot the points
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, color="gray", linestyle=":", linewidth=1, zorder=1)

    # Emphasize first and last points
    for i in [0, -1]:
        dot_color = "green"
        if i == -1 :
            dot_color = "red"
        ax.scatter(rw.x_values[i], rw.y_values[i], c=dot_color, edgecolors="none",
                   s=50, zorder=2)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("\nMake another walk? (y|n)\n> ")
    if keep_running.lower() != "y":
        break
