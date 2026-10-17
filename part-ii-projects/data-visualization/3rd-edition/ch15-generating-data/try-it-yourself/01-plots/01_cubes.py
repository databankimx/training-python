"""Assignment 15.01"""
# Cubes: A number raised to the third power is a cube. Plot the first five cubic numbers, 
#        and then plot the first 5000 cubic numbers.

import matplotlib.pyplot as plt

numbers = list(range(1, 5001))
cubes = [x ** 3 for x in numbers]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

ax.set_title("Squared Numbers", fontsize = 18)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params(axis = "both", labelsize = 14)

ax.plot(numbers, cubes, linewidth = 3)
plt.show()
