"""Working with spatial data using SciPy"""

import numpy as np
#pylint: disable=no-name-in-module
from scipy.spatial import Delaunay, ConvexHull, KDTree
from scipy.spatial.distance import euclidean, cityblock, cosine, hamming

def triangulate(points: np.ndarray) -> None:
    """Show the Delaunay triangles that connect the points"""
    print("Delaunay triangulation:")
    tri = Delaunay(points)
    print(f"Number of triangles: {len(tri.simplices)}")
    print(f"Triangle vertices (point indices):\n{tri.simplices}\n")

def convex_hull(points: np.ndarray) -> None:
    """Find the smallest polygon that covers all of the points"""
    print("Convex hull:")
    hull = ConvexHull(points)
    print(f"Hull vertices (point indices): {hull.vertices}")
    print(f"Hull area: {hull.volume:.4f}\n")

def nearest_neighbor(points: list[tuple], target: tuple) -> None:
    """Find the point closest to the target using a KD-tree"""
    print("Nearest neighbor (KD-tree):")
    tree = KDTree(points)
    distance, index = tree.query(target)
    print(f"Nearest point to {target} is index {index} at distance {distance:.4f}\n")

def distances(p1: tuple, p2: tuple) -> None:
    """Compare several distance metrics between two points"""
    print(f"Distances between {p1} and {p2}:")
    print(f"Euclidean:  {euclidean(p1, p2):.4f}")
    print(f"City block: {cityblock(p1, p2):.4f}")
    print(f"Cosine:     {cosine(p1, p2):.4f}\n")

def binary_distance(b1: tuple, b2: tuple) -> None:
    """Hamming distance compares binary values position by position"""
    print(f"Hamming distance between {b1} and {b2}:")
    print(f"Hamming: {hamming(b1, b2):.4f}\n")

def main() -> None:
    """Main function"""
    points = np.array([
        [2, 4], [3, 4], [3, 0], [2, 2], [4, 1],
        [1, 2], [5, 0], [3, 1], [1, 2], [0, 2]
    ])
    triangulate(points)
    convex_hull(points)

    kd_points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
    nearest_neighbor(kd_points, (1, 1))

    distances((1, 0), (10, 2))
    binary_distance((True, False, True), (False, True, True))

if __name__ == "__main__":
    main()
