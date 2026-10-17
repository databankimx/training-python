"""Assignment 15.05"""
# Refactoring: The fill_walk() method is lengthy. Create a new method called
#              get_step() to determine the direction and distance for each step,
#              and then calculate the step. You should end up with two calls to
#              get_step() in fill_walk():
# ------------------------------------------------------------------------------
#              x_step = self.get_step()
#              y_step = self.get_step()
# ------------------------------------------------------------------------------
#              This refactoring should reduce the size of fill_walk() and make
#              the method easier to read and understand.

import matplotlib.pyplot as plt
from refactored_random_walk import RandomWalk

print("Try-it-Yourself:")
print("Assignment 15.5")

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("seaborn-v0_8")
    fix, ax = plt.subplots(figsize=(16, 9))
    ax.plot(rw.x_values, rw.y_values, color="gray", linewidth=2, zorder=1)
    ax.set_aspect("equal")
    # I added the zorder argument to make sure the dots appear on top of the line ploy
    ax.scatter(0, 0, color=(0, .8, 0), edgecolors="none", s=75, zorder=2, marker="*")
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=75,
               zorder=3, marker="*")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    again = input("Make another walk? (y/n): ")
    if again and again.lower()[0] != "y":
        break
