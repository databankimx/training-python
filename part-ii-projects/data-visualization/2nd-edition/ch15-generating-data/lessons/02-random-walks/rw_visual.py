"""Lesson 2 - Random Walk (pyplot)"""

import matplotlib.pyplot as plt
from random_walk import RandomWalk

num_points = 5_000

while True:
    # Make a random walk
    rw = RandomWalk(num_points)

    # Plot the points
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    point_numbers = range(rw.num_points)
    # pylint: disable=no-member
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolors="none", s=10)

    # Emphasize first and last points
    for i in [0, -1]:
        dot_color = "green"
        if i == -1:
            dot_color = "red"
        ax.scatter(rw.x_values[i], rw.y_values[i],
                   c=dot_color, edgecolors="none", s=30)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("\nMake another walk? (y|n)\n> ")
    if keep_running.lower() != "y":
        break
