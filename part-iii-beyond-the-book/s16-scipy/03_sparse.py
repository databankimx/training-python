"""Working with Sparse Matrices"""

import numpy as np
from scipy.sparse import csr_matrix, csc_matrix
from utilities import clear_terminal, pause

def sparse_row_matrix(arr: np.ndarray) -> None:
    """Create a CSR matrix"""
    clear_terminal()
    print("Compressed Row Matrix:\n")
    print(f"Array:\n{arr}\n")
    csr = csr_matrix(arr)
    print(f"Non-Zero Values: {csr.count_nonzero()}")
    print(f"CSR Data: {csr.data}")
    print(f"CSR Shape: {csr.data.shape}\n")
    print(f"CSR Matrix:\n{csr}")
    pause()

def sparse_col_matrix(arr: np.ndarray) -> None:
    """Create a CSC matrix"""
    clear_terminal()
    print("Compressed Column Matrix:\n")
    print(f"Array:\n{arr}\n")
    csc = csc_matrix(arr)
    print(f"Non-Zero Values: {csc.count_nonzero()}")
    print(f"CSC Data: {csc.data}")
    print(f"CSC Shape: {csc.data.shape}\n")
    print(f"CSC Matrix:\n{csc}")
    pause()

def remove_zeroes(arr: np.ndarray) -> None:
    """Remove zeroes from CSR matrix"""
    clear_terminal()
    print("Remove Zeroes:\n")
    print(f"Array:\n{arr}\n")
    csr = csr_matrix(arr)
    csr.eliminate_zeros()
    print("Removed zeroes.\n")
    print(f"CSR Data: {csr.data}")
    print(f"CSR Shape: {csr.data.shape}\n")
    print(f"CSR Matrix:\n{csr}")
    pause()

def merge_duplicates(arr: np.ndarray) -> csr_matrix:
    """Sum duplicates from CSR matrix"""
    clear_terminal()
    print("Sum Duplicates:\n")
    print(f"Array:\n{arr}\n")
    csr = csr_matrix(arr)
    csr.sum_duplicates()
    print("Summed duplicates.\n")
    print(f"CSR Data: {csr.data}")
    print(f"CSR Shape: {csr.data.shape}\n")
    print(f"CSR Matrix:\n{csr}")
    pause()
    return csr

def convert(csr: csr_matrix) -> None:
    """Convert CSR matrix to CSC matrix"""
    clear_terminal()
    print("Convert CSR to CSC:\n")
    csc = csr.tocsc()
    print(f"CSR:\n{csr}\n")
    print(f"CSC: {csc}")
    pause(end=True)

def main() -> None:
    """Main function"""
    arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]], dtype=np.int8)
    sparse_row_matrix(arr)
    sparse_col_matrix(arr)
    remove_zeroes(arr)
    csr = merge_duplicates(arr)
    convert(csr)

if __name__ == "__main__":
    main()
