"""Reading and writing MATLAB files with SciPy"""

import os
import numpy as np
#pylint: disable=no-name-in-module
from scipy import io

MAT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "arr.mat")

def save_vector(filepath: str) -> None:
    """Save an array to a MATLAB (.mat) file"""
    arr = np.arange(10)
    io.savemat(filepath, {"vec": arr})
    print(f"Saved the vector to {os.path.basename(filepath)}\n")

def load_vector(filepath: str, squeeze: bool=False) -> np.ndarray:
    """Load the vector from a MATLAB (.mat) file"""
    data = io.loadmat(filepath, squeeze_me=squeeze)
    return data["vec"]

def main() -> None:
    """Main function"""
    save_vector(MAT_FILE)

    vec = load_vector(MAT_FILE)
    print(f"Loaded shape: {vec.shape}")
    print(f"Loaded values: {vec}\n")

    vec = load_vector(MAT_FILE, squeeze=True)
    print(f"Squeezed shape: {vec.shape}")
    print(f"Squeezed values: {vec}")

if __name__ == "__main__":
    main()
