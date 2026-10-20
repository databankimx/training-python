"""Lesson 1.4 - Using a Style Sheet"""

import matplotlib.pyplot as plt

# We can set a built-in stylesheet to be used for the plot
#     (this must be done before calling plt.subplots())
plt.style.use("seaborn-v0_8")

# If you use the following (book example), you'll receive a warning indicating that
#     the style is deprecated
# plt.style.use("seaborn")

# List of styles: https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
# You could use the following code to identify the available stylesheet names
# for s in plt.style.available:
#     print(s)

numbers = list(range(1, 6))
squares = [x ** 2 for x in numbers]
fig, ax = plt.subplots()
ax.plot(numbers, squares, linewidth = 3)
ax.set_title("Squared Numbers", fontsize = 18)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params(axis = "both", labelsize = 14)

plt.show()
