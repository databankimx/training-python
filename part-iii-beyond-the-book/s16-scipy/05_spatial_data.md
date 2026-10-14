## Spatial Data

Spatial data describes things in a geometric space, such as points on a
coordinate plane. Many problems depend on the position of points, for example:

* Finding whether a point is inside a boundary
* Finding the points closest to a given location
* Measuring how similar two points are

SciPy's `scipy.spatial` module provides functions for these tasks. The code for
this lesson is in [05_spatial_data.py](./05_spatial_data.py).

---

### Triangulation

A *triangulation* divides an area into triangles that connect a set of points.
Each point is a corner of at least one triangle. `Delaunay()` builds a
triangulation that avoids long, thin triangles where possible.

```python
import numpy as np
from scipy.spatial import Delaunay

points = np.array([
    [2, 4], [3, 4], [3, 0], [2, 2], [4, 1],
    [1, 2], [5, 0], [3, 1], [1, 2], [0, 2]
])
tri = Delaunay(points)
print(tri.simplices)
```

The `simplices` attribute is a list of triangles. Each row holds the indices of
the three points that form one triangle. The triangles are listed by index,
not by coordinates, so use the indices to look up the points.

---

### Convex Hull

A *convex hull* is the smallest polygon that covers all of the points. You can
picture it as a rubber band stretched around the outside of the points.

```python
from scipy.spatial import ConvexHull

hull = ConvexHull(points)
print(hull.vertices)
print(hull.volume)
```

The `vertices` attribute lists the points that sit on the outside of the hull.
For two-dimensional points, `volume` is the area of the hull.

---

### Nearest Neighbors with a KD-Tree

A *KD-tree* is a data structure that answers nearest-neighbor questions quickly.
Building the tree once and then querying it is much faster than checking every
point each time.

```python
from scipy.spatial import KDTree

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
tree = KDTree(points)
distance, index = tree.query((1, 1))
print(f"Nearest point is index {index} at distance {distance:.4f}")
```

Output:

```
Nearest point is index 0 at distance 2.0000
```

The point `(1, -1)` is the closest to `(1, 1)`, two units away.

---

### Distance Metrics

The distance between two points depends on how you measure it. SciPy's
`scipy.spatial.distance` module provides several metrics. Machine learning
algorithms such as K-nearest neighbors depend heavily on the metric they use.

Using the points `(1, 0)` and `(10, 2)`:

```python
from scipy.spatial.distance import euclidean, cityblock, cosine

p1 = (1, 0)
p2 = (10, 2)
print(f"Euclidean:  {euclidean(p1, p2):.4f}")
print(f"City block: {cityblock(p1, p2):.4f}")
print(f"Cosine:     {cosine(p1, p2):.4f}")
```

Output:

```
Euclidean:  9.2195
City block: 11.0000
Cosine:     0.0194
```

* **Euclidean** is the straight-line distance.
* **City block** (Manhattan) distance counts steps along the grid, with movement
  only up, down, left, or right. It adds 9 across and 2 up, giving 11.
* **Cosine** distance measures the angle between the two points, seen from the
  origin, and does not depend on how far away they are.

The **Hamming** distance is different. It compares binary values, and it is
the proportion of positions where the values differ:

```python
from scipy.spatial.distance import hamming

print(hamming((True, False, True), (False, True, True)))
```

Two of the three positions differ, so the result is `0.6667`.

---

### Try It

Add a new point to the nearest-neighbor example that is closer to `(1, 1)` than
`(1, -1)` is. Run the query again and check that the index changes.

---
