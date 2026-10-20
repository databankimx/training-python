"""Assignment 15.10"""
# Practicing with Both Libraries: Try using Matplotlib to make a die-rolling
#     visualization, and use Plotly to make the visualization for a random walk.
#     (You'll need to consult the documentation for each library to complete
#     this exercise.)

import matplotlib.pyplot as plt
import plotly.express as px
from die import Die
from random_walk import RandomWalk

print("Try-it-Yourself:")
print("Assignment 15.10")

# Part 1: Matplotlib - roll one D6 1,000 times and plot how often each face came up
die = Die()
rolls = 1_000

results = [die.roll() for _ in range(rolls)]
faces = list(range(1, die.num_sides + 1))
frequencies = [results.count(face) for face in faces]

plt.style.use("bmh")
fig, ax = plt.subplots()
ax.bar(faces, frequencies, color="steelblue")
ax.set_title(f"Result of Rolling One D6 {rolls:,} Times", fontsize=16)
ax.set_xlabel("Result", fontsize=12)
ax.set_ylabel("Frequency of Result", fontsize=12)
ax.set_xticks(faces)
plt.show()

# Part 2: Plotly - plot a random walk, coloring each point by when it was reached
rw = RandomWalk()
rw.fill_walk()

walk = px.scatter(
    x=rw.x_values,
    y=rw.y_values,
    color=list(range(rw.num_points)),
    color_continuous_scale="Blues",
    title=f"Random Walk of {rw.num_points:,} Points",
)
walk.update_traces(marker_size=3)
walk.update_layout(xaxis_visible=False, yaxis_visible=False)
walk.show()
