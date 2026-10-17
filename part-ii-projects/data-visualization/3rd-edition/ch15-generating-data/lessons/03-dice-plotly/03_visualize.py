"""Lesson 3.3 - Visualizing Results with Plotly Express"""

from die import Die
import plotly.express as px
# python -m pip install pandas
# python -m pip install plotly
# python -m pip --upgrade plotly      (make sure this one is v5.13 or higher due to a bug in 5.12)
# python -m pip install plotly.express

die = Die()

results = []
for _ in range(1000):
    results.append(die.roll())

frequencies = []
poss_results = range(1, die.num_sides + 1)
for n in poss_results:
    frequency = results.count(n)
    frequencies.append(frequency)

# Visualize results

# With Plotly Express, we can easily generate a bar graph with x and y values
fig = px.bar(x=poss_results, y=frequencies)
# The graph launches in your default browser
fig.show()
