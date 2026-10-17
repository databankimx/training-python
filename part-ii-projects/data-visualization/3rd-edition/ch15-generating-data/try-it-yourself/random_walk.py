"""A class to generate random walks"""

from random import choice

# pylint: disable=too-few-public-methods
class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a random walk"""
        # Set the number of points to generate
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self, max_dist=5):
        """Populate the points for the given walk"""
        # Keep stepping until walk reaches the specified length
        while len(self.x_values) < self.num_points:
            # Decide direction and distance
            x_direction = choice([1, -1])
            x_distance = choice(list(range(max_dist)))
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice(list(range(max_dist)))
            y_step = y_direction * y_distance

            # Ignore non-moving points
            if x_step == 0 and y_step == 0:
                continue

            # Calculate new (x, y) coordinates
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # Append the new coordinates
            self.x_values.append(x)
            self.y_values.append(y)
