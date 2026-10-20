"""Assignment 15.01"""
# Cubes: A number raised to the third power is a cube. Plot the first five cubic numbers,
#        and then plot the first 5000 cubic numbers.

import math
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, MultipleLocator


def plot_cubes(max_x: int) -> None:
    """Plot the cubes of the numbers 1 to max_x"""
    numbers = list(range(1, max_x + 1))
    cubes = [x ** 3 for x in numbers]

    plt.style.use("seaborn-v0_8")
    _, ax = plt.subplots()

    ax.set_title("Cube Numbers", fontsize = 18)
    ax.set_xlabel("Value", fontsize = 14)
    ax.set_ylabel("Cube of Value", fontsize = 14)
    ax.tick_params(axis = "both", labelsize = 14)

    ax.plot(numbers, cubes, linewidth = 3)

    if max_x <= 10:
        # With only a few points, label each whole number on the x-axis,
        # and step the y-axis up in tens
        top = 10 * math.ceil(max_x ** 3 / 10)
        ax.axis([0, max_x, 0, top])
        ax.set_xticks(numbers)
        ax.yaxis.set_major_locator(MultipleLocator(10))
    else:
        # With many points, show whole numbers on the x-axis and let matplotlib choose the rest
        ax.axis([0, max_x, 0, max_x ** 3])
        ax.xaxis.set_major_locator(MaxNLocator(integer = True))

    plt.show()


plot_cubes(5)
plot_cubes(5000)
