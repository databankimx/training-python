"""Assignment 15.04"""
# Modified Random Walks: In the RandomWalk class, x_step and y_step are generated from the same set of conditions.
#                        The direction is chosen randomly from the list [1, -1] and the distance from the list [0, 1, 2, 3, 4].
#                        Modify the values in these lists to see what happens to the overall shape of your walks.
#                        Try a longer list of choices for the distance, such as 0 through 8, or remove the –1
#                        from the x or y direction list.

import matplotlib.pyplot as plt
from modified_random_walk import RandomWalk

print("Try-it-Yourself:")
print("Assignment 15.4")

num_points = 5_000

while True:
    # Make a random walk
    rw = RandomWalk(num_points)

    # Plot the points
    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    # pylint: disable=no-member
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors="none", s=10)

    # Emphasize first and last points
    for i in [0, -1]:
        dot_color = "green"
        if i == -1:
            dot_color = "red"
        ax.scatter(rw.x_values[i], rw.y_values[i], c=dot_color, edgecolors="none", s=30)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("\nMake another walk? (y|n)\n> ")
    if keep_running.lower() != "y":
        break
