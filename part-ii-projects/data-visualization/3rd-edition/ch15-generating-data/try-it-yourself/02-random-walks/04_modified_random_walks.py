"""Assignment 15.04"""
# Modified Random Walks: In the RandomWalk class, x_step and y_step are generated from
#                        the same set of conditions. The direction is chosen randomly from
#                        the list [1, -1] and the distance from the list [0, 1, 2, 3, 4].
#                        Modify the values in these lists to see what happens to the overall
#                        shape of your walks. Try a longer list of choices for the distance,
#                        such as 0 through 8, or remove the –1 from the x or y direction list.

import matplotlib.pyplot as plt
from random_walk import RandomWalk

print("Try-it-Yourself:")
print("Assignment 15.4")

while True:
    rw = RandomWalk()
    # Changing distance list
    rw.fill_walk(max_dist=10)

    plt.style.use("classic")
    fix, ax = plt.subplots(figsize=(16, 9))
    # pylint: disable=no-member
    ax.scatter(rw.x_values, rw.y_values, s=5, c=range(rw.num_points),
               cmap=plt.cm.viridis, edgecolors="none")
    ax.set_aspect("equal")
    ax.scatter(0, 0, color=(0, .8, 0), edgecolors="none", s=100, marker="*")
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100, marker="*")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    again = input("Make another walk? (y/n): ")
    if again and again.lower()[0] != "y":
        break
