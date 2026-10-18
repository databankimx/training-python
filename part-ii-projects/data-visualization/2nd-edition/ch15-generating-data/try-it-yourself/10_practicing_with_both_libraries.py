"""Assignment 15.10"""
# Practicing with Both Libraries: Try using Matplotlib to make a die-rolling
#            visualization, and use Plotly to make the visualization for a
#            random walk. (You'll need to consult the documentation for each
#            library to complete this exercise.)
import os
import matplotlib.pyplot as plt
from plotly import offline
from plotly.graph_objs import Layout, Scatter
from die import Die
from random_walk import RandomWalk

print("Try-it-Yourself:")
print("Assignment 15.10")

# Part 1: Matplotlib - roll one D6 1,000 times and plot how often each face came up
die = Die()
roll_count = 1_000

results = [die.roll() for _ in range(roll_count)]
faces = list(range(1, die.num_sides + 1))
frequencies = [results.count(face) for face in faces]

plt.style.use("bmh")
fig, ax = plt.subplots()
ax.bar(faces, frequencies, color="steelblue")
ax.set_title(f"Results of rolling one D6 {roll_count:,} times", fontsize=16)
ax.set_xlabel("Result", fontsize=12)
ax.set_ylabel("Frequency of Result", fontsize=12)
ax.set_xticks(faces)
plt.show()

# Part 2: Plotly - plot a random walk, coloring each point by when it was reached
num_points = 5_000
rw = RandomWalk(num_points)

trace = Scatter(
    x=rw.x_values,
    y=rw.y_values,
    mode="markers",
    marker={"size": 3, "color": list(range(num_points)), "colorscale": "Blues"},
)
layout = Layout(
    title=f"Random Walk of {num_points:,} Points",
    xaxis={"visible": False},
    yaxis={"visible": False},
)
ROOT_DIR = os.path.dirname(__file__)
file_path = os.path.join(ROOT_DIR, "files", "random_walk.html")
offline.plot({"data": [trace], "layout": layout}, filename=file_path)
