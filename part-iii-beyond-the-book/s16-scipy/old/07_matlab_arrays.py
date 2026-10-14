# SciPy Matlab Arrays
#
# Working With Matlab Arrays
# We know that NumPy provides us with methods to persist the data in readable formats for Python.
#   But SciPy provides us with interoperability with Matlab as well.
# SciPy provides us with the module scipy.io, which has functions for working with Matlab arrays.

from scipy import io
import numpy as np
import os

def root_path():
    """Return the root execution path of the script"""
    return os.path.dirname(__file__)

# Exporting Data in Matlab Format
# The savemat() function allows us to export data in Matlab format.
# The method takes the following parameters:
# - filename - the file name for saving data.
# - mdict - a dictionary containing the data.
# - do_compression - a boolean value that specifies whether to compress the result or not. Default False.

arr = np.arange(10)
io.savemat(os.path.join(root_path(), "07_arr.mat"), {"vec": arr})

# Import Data from Matlab Format
# The loadmat() function allows us to import data from a Matlab file.
# The function takes one required parameter:
# - filename - the file name of the saved data.
# It will return a structured array whose keys are the variable names,
#   and the corresponding values are the variable values.

my_data = io.loadmat(os.path.join(root_path(), "07_arr.mat"))
print(my_data)
print()
print(my_data["vec"])
print()

# The squeeze_me attribute will remove unnecessary dimensions
my_data = io.loadmat(os.path.join(root_path(), "07_arr.mat"), squeeze_me=True)
print(my_data["vec"])
