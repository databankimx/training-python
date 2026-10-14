# SciPy Spatial Data
#
# Working with Spatial Data
# Spatial data refers to data that is represented in a geometric space.
#   e.g. points on a coordinate system.
# We deal with spatial data problems on many tasks.
#   e.g. finding if a point is inside a boundary or not.
#
# SciPy provides us with the module scipy.spatial, which has functions for working with spatial data.

import numpy as np
import matplotlib.pyplot as plt

# Triangulation
# A Triangulation of a polygon is to divide the polygon into multiple triangles with which
#   we can compute an area of the polygon.
# A Triangulation with points means creating surface composed triangles in which all of the
#   given points are on at least one vertex of any triangle in the surface.
# One method to generate these triangulations through points is the Delaunay() Triangulation
from scipy.spatial import Delaunay

points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1]
])
simplices = Delaunay(points).simplices
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')
plt.show()

# Convex Hull
# A convex hull is the smallest polygon that covers all of the given points.
from scipy.spatial import ConvexHull
points = np.array([
    [2, 4],
    [3, 4],
    [3, 0],
    [2, 2],
    [4, 1],
    [1, 2],
    [5, 0],
    [3, 1],
    [1, 2],
    [0, 2]
])
hull = ConvexHull(points)
hull_points = hull.simplices
plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
    plt.plot(points[simplex,0], points[simplex,1], 'k-')
plt.show()

# KDTrees
# KDTrees are a data structure optimized for nearest neighbor queries.
# E.g. in a set of points using KDTrees we can efficiently ask which points are nearest to a certain given point.
# The KDTree() method returns a KDTree object.
# The query() method returns the distance to the nearest neighbor and the location of the neighbors.
from scipy.spatial import KDTree
points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points)
res = kdtree.query((1, 1))
print(res)

# Distance Matrix
# There are many Distance Metrics used to find various types of distances between two points in data science,
#   Euclidean distance, cosine distance etc.
# The distance between two vectors may not only be the length of straight line between them, it can also be
#   the angle between them from origin, or number of unit steps required etc.
# Many of the Machine Learning algorithm's performance depends greatly on distance matrices.
#   e.g. "K Nearest Neighbors", or "K Means" etc.

p1 = (1, 0)
p2 = (10, 2)

# Euclidean Distance
from scipy.spatial.distance import euclidean
res = euclidean(p1, p2)
print(res)
print()

# City Block Distance (Manhattan Distance)
# Is the distance computed using 4 degrees of movement.
#   e.g. we can only move: up, down, right, or left, not diagonally.
from scipy.spatial.distance import cityblock
res = cityblock(p1, p2)
print(res)
print()

# Cosine Distance
# Is the value of cosine angle between the two points A and B.
from scipy.spatial.distance import cosine
res = cosine(p1, p2)
print(res)
print()

# Hamming Distance
# Is the proportion of bits where two bits are different.
# It's a way to measure distance for binary sequences.
from scipy.spatial.distance import hamming
p1 = (True, False, True)
p2 = (False, True, True)
res = hamming(p1, p2)
print(res)
print()
