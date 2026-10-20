"""A class to generate random walks"""

from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points: int=5000) -> None:
        """Initialize attributes of a random walk"""
        # Set the number of points to generate
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self) -> None:
        """Populate the points for the given walk"""
        # Keep stepping until walk reaches the specified length
        while len(self.x_values) < self.num_points:
            x = self.x_values[-1]
            y = self.y_values[-1]
            point = [x, y]
            while point == [x, y]:
                point = self.get_new_point(x, y)
            self.x_values.append(point[0])
            self.y_values.append(point[1])

    def get_new_point(self, x: int, y: int) -> list[int]:
        """Calculate a new point"""
        return [self.get_new_num(x), self.get_new_num(y)]

    def get_new_num(self, num: int) -> int:
        """Calculate a new number"""
        direction = choice([1, 0, -1])
        distance = choice(list(range(0, 9)))
        step = direction * distance
        return num + step
