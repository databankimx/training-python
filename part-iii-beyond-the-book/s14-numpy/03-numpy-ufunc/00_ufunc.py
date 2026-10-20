"""NumPy Universal Functions (ufunc)"""

import numpy as np

def traditional_zip(lx: list[int], ly: list[int]) -> None:
    """Merge two lists using traditional zip"""
    lz = []
    for x, y in zip(lx, ly):
        lz.append(x + y)
    print("Traditional Zip:")
    print(f"List X: {lx}")
    print(f"List Y: {ly}")
    print(f"Result: {lz}\n")

def ufunc_add(lx: list[int], ly: list[int]) -> None:
    """Merge two lists using NumPy's ufunc `add`"""
    az = np.add(lx, ly)
    print("NumPy Add:")
    print(f"List X: {lx}")
    print(f"List Y: {ly}")
    print(f"Result: {az}\n")

def ufunc_add_arrays(lx: np.ndarray[int], ly: np.ndarray[int]) -> None:
    """Merge two arrays using NumPy's ufunc `add`"""
    az = np.add(lx, ly)
    print("NumPy Add Arrays:")
    print(f"Array X: {lx}")
    print(f"Array Y: {ly}")
    print(f"Result: {az}\n")

def main() -> None:
    """Main function"""
    lx = [1, 2, 3, 4]
    ly = [5, 6, 7, 8]
    traditional_zip(lx, ly)
    ufunc_add(lx, ly)
    ax = np.array(lx)
    ay = np.array(ly)
    ufunc_add_arrays(ax, ay)

if __name__ == "__main__":
    main()
