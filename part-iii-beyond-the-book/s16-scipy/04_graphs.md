## SciPy Graphs

A graph is a set of *nodes* (also called vertices) connected by *edges*. Graphs
model many real-world problems: road networks, social connections, and
dependencies between tasks.

SciPy's `scipy.sparse.csgraph` module provides algorithms for graphs stored as
sparse matrices. Each entry in the matrix is the weight of the edge between
two nodes. A zero means there is no edge, which is why graphs are a natural
fit for sparse matrices.

The code for this lesson is in [04_graphs.py](./04_graphs.py).

---

### The Graph

We'll use this small undirected graph with three nodes:

```python
import numpy as np

arr = np.array([[0, 1, 2], [1, 0, 0], [2, 0, 0]])
```

Node 0 is connected to node 1 (weight 1) and to node 2 (weight 2). Because the
matrix is symmetric, the connections run in both directions.

We store it as a CSR matrix, so the zeros are not stored:

```python
from scipy.sparse import csr_matrix

csr = csr_matrix(arr)
```

---

### Connected Components

Two nodes are in the same *connected component* if there is a path between
them. The `connected_components()` function returns how many components a
graph has, along with a label for each node:

```python
from scipy.sparse.csgraph import connected_components

num_components, labels = connected_components(csr)
print(f"Number of connected components: {num_components}")
```

Output:

```
Number of connected components: 1
```

All three nodes are reachable from one another, so there is one component.

---

### Shortest Paths from One Node: Dijkstra's Algorithm

`dijkstra()` finds the shortest distance from a starting node to every other
node. Passing `indices=0` starts from node 0. Passing `return_predecessors=True`
also returns, for each node, the node that comes before it on its shortest path.

```python
from scipy.sparse.csgraph import dijkstra

distances, predecessors = dijkstra(csr, return_predecessors=True, indices=0)
print(f"Distances from node 0: {distances}")
print(f"Predecessors: {predecessors}")
```

The distance from node 0 to itself is 0, to node 1 is 1, and to node 2 is 2.
Node 0 has no predecessor, which SciPy marks with `-9999`.

---

### All Shortest Paths: Floyd-Warshall

`floyd_warshall()` computes the shortest distance between every pair of nodes,
returning a matrix:

```python
from scipy.sparse.csgraph import floyd_warshall

all_distances = floyd_warshall(csr)
print(all_distances)
```

The result is symmetric. For example, the distance from node 1 to node 2 is 3,
because the path goes through node 0 (1 + 2).

---

### Shortest Paths with Negative Weights: Bellman-Ford

`bellman_ford()` works like Dijkstra's algorithm, but it also handles negative
edge weights. Dijkstra's algorithm assumes every weight is non-negative.

```python
from scipy.sparse.csgraph import bellman_ford

distances, predecessors = bellman_ford(csr, return_predecessors=True, indices=0)
print(distances)
```

For this graph, all weights are positive, so Bellman-Ford returns the same
distances as Dijkstra's algorithm.

To see the difference, the script also runs Bellman-Ford on a graph where one
edge has a negative weight, `-1`. Dijkstra's algorithm can give wrong answers
in that case, but Bellman-Ford still finds the shortest paths, as long as the
graph has no cycle whose total weight is negative.

```python
arr = np.array([[0, -1, 2], [1, 0, 0], [2, 0, 0]])
csr = csr_matrix(arr)
print(bellman_ford(csr, return_predecessors=True, indices=0))
```

---

### Traversing the Graph

The `depth_first_order()` and `breadth_first_order()` functions visit every
node reachable from a starting node. Both take the graph and the starting node.

* **Depth-first** goes as far as it can along one path before backing up to try
  another.
* **Breadth-first** visits all the neighbors of a node before moving further away.

Each function returns the order in which the nodes were visited, along with the
predecessor of each node:

```python
from scipy.sparse.csgraph import depth_first_order, breadth_first_order

print(depth_first_order(csr, 1))
print(breadth_first_order(csr, 1))
```

The script runs both traversals on a four-node graph. Run it and compare the two
orders: the depth-first order follows one branch to the end before it returns.

---

### Try It

Run the script, and press Enter to move through each section:

```pwsh
python 04_graphs.py
```

Then change the matrix to add a fourth node that is not connected to the
others. Check how the component count changes.

---
