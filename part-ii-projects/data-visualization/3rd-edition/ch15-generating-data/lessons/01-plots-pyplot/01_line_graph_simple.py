"""Lesson 1.1 - Plotting a Simple Line Graph"""

# matplotlib provides graphing/charting capabilities
# Samples here: https://matplotlib.org/gallery/
# You may need to run the following command to install matplotlib
# > python -m pip install matplotlib

import matplotlib.pyplot as plt

# Create some data to graph
squares = [1, 4, 9, 16, 25]

# fig is the standard abbreviation for the figure, and ax for the axes.
fig, ax = plt.subplots()

# Now we plot the values (points are x=index and y=value from the list being plotted)
ax.plot(squares)
# Because the index values start from 0, the y-values will be off

# Finally, we draw the figure and display in the matplotlib viewer for the end user
plt.show()
