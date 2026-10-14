"""Working with Graphs"""

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components, dijkstra
from scipy.sparse.csgraph import floyd_warshall, bellman_ford
# from scipy.sparse.csgraph import depth_first_order, breadth_first_order
from utilities import clear_terminal, pause

def create_csr(arr: np.ndarray) -> csr_matrix:
    """Create a CSR matrix"""
    clear_terminal()
    print("CSR Matrix:\n")
    print(f"Array:\n{arr}\n")
    csr = csr_matrix(arr)
    print(f"CSR Matrix:\n{csr}")
    pause()
    return csr

def count_connected_components(csr: csr_matrix) -> None:
    """Count the number of connected components in the CSR matrix"""
    clear_terminal()
    print(f"CSR Matrix:\n{csr}\n")
    num_components, _ = connected_components(csr)
    print(f"Number of connected components: {num_components}")
    pause()

def find_shortest_path(csr: csr_matrix) -> None:
    """Find the shortest path in the CSR matrix using Dijkstra's algorithm"""
    clear_terminal()
    print(f"CSR Matrix:\n{csr}\n")
    shortest_path = dijkstra(csr, return_predecessors=True, indices=0)
    print(shortest_path)
    # print(f"Shortest path from node 0 to all other nodes:")
    # for i in range(csr.shape[0]):
    #     print(f"Node {i}: {shortest_path[0][i]}")
    pause()

def find_all_shortest_paths(csr: csr_matrix) -> None:
    """Find all shortest paths in the CSR matrix using Floyd-Warshall algorithm"""
    clear_terminal()
    print(f"CSR Matrix:\n{csr}\n")
    shortest_paths = floyd_warshall(csr)
    print(shortest_paths)
    # print(f"Shortest paths between all pairs of nodes:")
    # for i in range(csr.shape[0]):
    #     for j in range(csr.shape[0]):
    #         if shortest_paths[i][j] != np.inf:
    #             print(f"Path from node {i} to node {j}: {shortest_paths[i][j]}")
    pause()

def find_shortest_path_bellman_ford(csr: csr_matrix) -> None:
    """Find the shortest path in the CSR matrix using Bellman-Ford algorithm"""
    clear_terminal()
    print(f"CSR Matrix:\n{csr}\n")
    shortest_path = bellman_ford(csr, return_predecessors=True, indices=0)
    print(shortest_path)
    # print(f"Shortest path from node 0 to all other nodes:")
    # for i in range(csr.shape[0]):
    #     print(f"Node {i}: {shortest_path[0][i]}")
    pause()

def main() -> None:
    """Main function"""
    arr = np.array([[0, 1, 2], [1, 0, 0], [2, 0, 0]])
    csr = create_csr(arr)
    count_connected_components(csr)
    find_shortest_path(csr)
    find_all_shortest_paths(csr)
    find_shortest_path_bellman_ford(csr)

if __name__ == "__main__":
    main()
