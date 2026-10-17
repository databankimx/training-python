"""Lesson 1.10 - Saving a Scatter Graph as an Image"""

import matplotlib.pyplot as plt
from relative_paths import get_path

numbers = list(range(1, 1001))
squares = [x ** 2 for x in numbers]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

# pylint: disable=no-member
ax.scatter(numbers, squares, s=10, c=squares, cmap=plt.cm.viridis)
ax.set_title("Squared Numbers", fontsize = 18)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params(axis = "both", labelsize = 14)
ax.axis([0, 1_000, 0, 1_000_000])
ax.ticklabel_format(style="plain")

# To save as an image, use plt.savefig() instead of plt.show()
plt.savefig(get_path("squares_graph.png"), bbox_inches="tight")
print("File saved...")
