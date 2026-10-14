## Using SciPy with Sparse Data

Sometimes you will have a data array where very little data is filled in.
In this case, you could wind up performing a large amount of work on entries
that contain no information. We call this *sparse data*.

* Sparse Data: A dataset where the majority of the values are zero:  
  Example: `[1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]`
* Dense Data: A dataset where the majority of the values are non-zero:  
  Example: `[1, 4, 2, 2, 7, 3, 4, 0, 1, 6, 2, 0]`

In data science, sparse data frequently occurs when computing partial
derivatives.

SciPy provides two types of sparse data matrices:

* CSC (Compressed Sparse Column)
    * Compresses the data along the columns
    * Useful for fast column slicing and efficient arithmetic
* CSR (Compressed Sparse Row)
    * Compresses the data across the rows
    * Useful for fast row slicing and faster matrix vector products

One thing to note: When you review the reportable data from either, you may 
not see a difference between them, but the underlying structures are 
different, so you should choose the structure best suited to your process.

---

### Creating a CSR Matrix

To create a Compressed Sparse Row matrix, use the `csr_matrix()` function,
which takes an `ndarray` as its argument.

```python
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]], dtype=np.int8)
print("Compressed Row Matrix:\n")
print(f"Array:\n{arr}\n")
csr = csr_matrix(arr)
print(f"Non-Zero Values: {csr.count_nonzero()}")
print(f"CSR Data: {csr.data}")
print(f"CSR Shape: {csr.data.shape}\n")
print(f"CSR Matrix:\n{csr}")
```

Output:

```
Compressed Row Matrix:

Array:
[[0 0 0]
 [0 0 1]
 [1 0 2]]

Non-Zero Values: 3
CSR Data: [1 1 2]
CSR Shape: (3,)

CSR Matrix:
<Compressed Sparse Row sparse matrix of dtype 'int8'
        with 3 stored elements and shape (3, 3)>
  Coords        Values
  (1, 2)        1
  (2, 0)        1
  (2, 2)        2
```

You can see, the matrix is only concerned with non-zero values.

---

### Creating a CSC Matrix

To create a Compressed Sparse Column matrix, use the `csc_matrix()` 
function, which takes an `ndarray` as its argument.

```python
import numpy as np
from scipy.sparse import csc_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]], dtype=np.int8)
print("Compressed Column Matrix:\n")
print(f"Array:\n{arr}\n")
csc = csc_matrix(arr)
print(f"Non-Zero Values: {csc.count_nonzero()}")
print(f"CSC Data: {csc.data}")
print(f"CSC Shape: {csc.data.shape}\n")
print(f"CSC Matrix:\n{csc}")
```

Output:

```
Compressed Column Matrix:

Array:
[[0 0 0]
 [0 0 1]
 [1 0 2]]

Non-Zero Values: 3
CSC Data: [1 1 2]
CSC Shape: (3,)

CSC Matrix:
<Compressed Sparse Column sparse matrix of dtype 'int8'
        with 3 stored elements and shape (3, 3)>
  Coords        Values
  (2, 0)        1
  (1, 2)        1
  (2, 2)        2
```

This result is very similar to the CSR matrix with the exception of the
indices, which are implemented column-wise.

---

### Removing Zeroes

If there are explicit zero values in the matrix, we can use the 
`eliminate_zeros()` function to remove them from the matrix.

```python
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]], dtype=np.int8)
print("Remove Zeroes:\n")
print(f"Array:\n{arr}\n")
csr = csr_matrix(arr)
csr.eliminate_zeros()
print("Removed zeroes.\n")
print(f"CSR Data: {csr.data}")
print(f"CSR Shape: {csr.data.shape}\n")
print(f"CSR Matrix:\n{csr}")
```

Output:

```
Remove Zeroes:

Array:
[[0 0 0]
 [0 0 1]
 [1 0 2]]

Removed zeroes.

CSR Data: [1 1 2]
CSR Shape: (3,)

CSR Matrix:
<Compressed Sparse Row sparse matrix of dtype 'int8'
        with 3 stored elements and shape (3, 3)>
  Coords        Values
  (1, 2)        1
  (2, 0)        1
  (2, 2)        2
```

We don't see any difference in the behavior, since the array's zero
elements are already empty in the CSR.

---

### Removing Duplicates

If there are duplicate values in the matrix, we can use the 
`sum_duplicates()` function to remove them from the matrix but summation.

```python
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]], dtype=np.int8)
print("Sum Duplicates:\n")
print(f"Array:\n{arr}\n")
csr = csr_matrix(arr)
csr.sum_duplicates()
print("Summed duplicates.\n")
print(f"CSR Data: {csr.data}")
print(f"CSR Shape: {csr.data.shape}\n")
print(f"CSR Matrix:\n{csr}")
```

Output:

```
Sum Duplicates:

Array:
[[0 0 0]
 [0 0 1]
 [1 0 2]]

Summed duplicates.

CSR Data: [1 1 2]
CSR Shape: (3,)

CSR Matrix:
<Compressed Sparse Row sparse matrix of dtype 'int8'
        with 3 stored elements and shape (3, 3)>
  Coords        Values
  (1, 2)        1
  (2, 0)        1
  (2, 2)        2
```

We don't see any difference in the behavior, our array does not contain 
duplicate data.

---

### Converting the Matrix Type

We can use the `tocsc()` function to convert a CSR matrix to CSC or the
`tocsr()` function for the reverse.

```python
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]], dtype=np.int8)
csr = csr_matrix(arr)
csc = csr.tocsc()
print("Convert CSR to CSC:\n")
print(f"CSR:\n{csr}\n")
print(f"CSC: {csc}")
```

Output:

```
Convert CSR to CSC:

CSR:
<Compressed Sparse Row sparse matrix of dtype 'int8'
        with 3 stored elements and shape (3, 3)>
  Coords        Values
  (1, 2)        1
  (2, 0)        1
  (2, 2)        2

CSC: <Compressed Sparse Column sparse matrix of dtype 'int8'
        with 3 stored elements and shape (3, 3)>
  Coords        Values
  (2, 0)        1
  (1, 2)        1
  (2, 2)        2
```

---
