"""Assignment 15.02"""
# Colored Cubes: Apply a colormap to your cubes plot.

import matplotlib.pyplot as plt

print("Try-it-Yourself:")
print("Assignment 15.2")

numbers = list(range(1, 5001))
cubes = [x ** 3 for x in numbers]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

ax.set_title("Squared Numbers", fontsize = 18)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params(axis = "both", labelsize = 14)

# pylint: disable=no-member
ax.scatter(numbers, cubes, s=10, c=cubes, cmap=plt.cm.viridis)
plt.show()
