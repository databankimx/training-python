# NumPy Fundamentals

## What is NumPy?

NumPy is a Python library used for working with arrays of numbers.

It has functions for working in domains of

* Linear Algebra
* Fourier Transformation
* Matrices

NumPy was created in 2005 by Travis Oliphant. It is an open source 
project and you can use it freely.

NumPy stands for *Numerical Python*.

---

### Why Use NumPy?

* In Python we have lists that serve the purpose of arrays, but they are 
  slow to process.
* NumPy aims to provide an array object that can be much faster than lists for many
  numerical operations.
* The array object in NumPy is called `ndarray`. It provides a lot of 
  supporting functions that make working with `ndarray` very easy.
* Arrays are very frequently used in data science, where speed and 
  resources are very important.

---

### Why is NumPy Faster Than Lists?

* NumPy arrays are stored at one continuous space in memory unlike lists, 
  so processes can access and manipulate them very efficiently.
    * This behavior is called *locality of reference* in computer science.
    * This is the main reason why NumPy is faster than lists.
* Also, NumPy is optimized to work with latest CPU architectures.

The source code for NumPy is located at this github repository:  
[https://github.com/numpy/numpy](https://github.com/numpy/numpy)

---

### Installing NumPy

Like many libraries, `numpy` must be installed before it can be used.

After ensuring that you are in an active virtual environment, run the 
following command:

```
python -m pip install numpy
```

> Note: Depending on your Python installation, `numpy` may already be 
> installed in your virtual environment.

---

### Topics

We'll cover the following topics in **NumPy Fundamentals**:

* [NumPy Arrays](./01_arrays.md)
* [Array Dimensions](./02_dimensions.md)
* [Array Indexing](./03_indices.md)
* [Array Slicing](./04_slices.md)
* [NumPy Data Types](./05_types.md)
* [Copy and View](./06_copy_view.md)
* [Array Shapes](./07_shape.md)
* [Reshaping Arrays](./08_reshaping.md)
* [Iterating Arrays with `for` Loops](./09_loop.md)
* [Iterating Arrays with `nditer`](./10_nditer.md)
* [Joining Arrays](./11_join.md)
* [Splitting Arrays](./12_split.md)
* [Sorting Arrays](./13_sort.md)
* [Searching Arrays](./14_search.md)
* [Filtering Arrays](./15_filter.md)

---
