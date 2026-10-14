# SciPy Introduction

# What is SciPy?
# SciPy is a scientific computation library that uses NumPy underneath.
# SciPy stands for Scientific Python.
# It provides more utility functions for optimization, stats and signal processing.
# Like NumPy, SciPy is open source so we can use it freely.
# SciPy was created by NumPy's creator Travis Olliphant.

# Why Use SciPy?
# If SciPy uses NumPy underneath, why can we not just use NumPy?
# SciPy has optimized and added functions that are frequently used in NumPy and Data Science.

# Which Language is SciPy Written in?
# SciPy is predominantly written in Python, but a few segments are written in C.

# Where is the SciPy Codebase?
# The source code for SciPy is located at this github repository https://github.com/scipy/scipy

# Installation:
# > python -m pip install scipy

import scipy

print(scipy.__version__)

from scipy import constants

print("1 liter =", constants.liter, "m^2")
