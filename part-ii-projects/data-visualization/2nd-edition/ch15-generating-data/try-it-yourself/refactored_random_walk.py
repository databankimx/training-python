"""Refactored Random Walk Class"""

from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points = 5_000):
        """Initialize walk attributes"""
        self.num_points = num_points

        # Walks begin at coordinates (0, 0)
        self.x_values = [0]
        self.y_values = [0]

        self.fill_walk()

    def fill_walk(self):
        """Calculate points in the walk"""

        # Iterate until the walk list has enough points
        while len(self.x_values) < self.num_points:
            x = self.x_values[-1]
            y = self.y_values[-1]
            point = [x, y]
            while point == [x, y]:
                point = self.get_new_point(x, y)
            self.x_values.append(point[0])
            self.y_values.append(point[1])

    def get_new_point(self, x, y):
        """Create a new point"""
        return [self.get_new_num(x), self.get_new_num(y)]

    def get_new_num(self, num):
        """Compute a new number"""
        direction = choice([1, 0, -1])
        distance = choice(list(range(0, 9)))
        step = direction * distance
        return num + step
