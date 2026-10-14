## LCM and GCD

When performing computations using groups of numbers, it is common to need
to calculate the least common multiple (*LCM*) or the greatest common
divisor (*GCD*) of the numbers.

In fact these concepts are so ubiquitous to problem solving that beginner
programming students are often tasked with building algorithms for them.

* Least Common Multiple
    * This is the smallest number that, can be divided evenly by all
      numbers in the sample.
        * For example, if we have the set `[2, 3, 6]`, the least common
          multiple is `6`, because `2 * 3 = 6`, `3 * 2 = 6` and `6 * 1 = 6`
    * Some common uses of the least common multiple include:
        * Arithmetic with fractions with different denominators
        * Solving problems involving different units
        * Computing smallest time interval for some multiple of events
        * Improving performance computing statistical modes and medians

* Greatest Common Divisor
    * Also called the greatest common factor, the GCD is the largest number
      that evenly divides all the numbers in the sample.
        * For example, if we have the set `4, 6, 8`, the greatest common
          divisor is `2`.
    * Some common uses of the greatest common divisor include:
        * Algebraic factorization, where it is necessary to know the GCD of
          the coefficients.
        * Simplifying fractions using the GCD of the numerator and
          denominator.
        * Computing ratios and scaling values

---

### Common Implementations

Let's look at how we traditionally implement GCD and LCM functions.

> Note!  
> In Python 3.9 and later, `gcd()` and `lcm()` functions are built into
> the `math` module that ships as part of the standard library.

---

#### Computing Greatest Common Divisor

We can create a simple function that uses Euclid's algorithm to calculate
the greatest common divisor of any two integers like this:

```python
def my_gcd(x: int, y: int) -> int:
    """Calculate GCD for two integers"""
    return x if y == 0 else my_gcd(y, x % y)

x, y = 30, 18
print(f"GCD of {x} and {y}: {my_gcd(x, y)}")
```

Output:

```
GCD of 30 and 18: 6
```

---

#### Computing Least Common Multiple

Using the GCD function we just created, we can also implement a very simple
function for the least common multiple of two integers:

```python
def my_lcm(x: int, y: int) -> int:
    """Calculate LCM for two integers"""
    return x * y // my_gcd(x, y)

x, y = 30, 18
print(f"LCM of {x} and {y}: {my_lcm(x, y)}")
```

Output:

```
LCM of 30 and 18: 90
```

---

### Dealing with More than Two Values

If we need to calculate GCD or LCM of more than two integers, it gets a 
little more complicated.

---

#### Computing Greatest Common Divisor of a List

We can create a function that iterates over a list of integers and performs
the GCD function for each number encountered.

```python
def my_list_gcd(arr: list[int]) -> int:
    """Calculate GCD for multiple integers"""
    arr = list(set(arr))
    gcf = arr[0]
    for n in arr[1:]:
        gcf = my_gcd(gcf, n)
    return gcf

arr = [12, 15, 27, 30]
print(f"My GCD of the list {arr}: {my_list_gcd(arr)}")
```

Output:

```
My GCD of the list [12, 15, 27, 30]: 3
```

---

#### Computing Least Common Multiple of a List

We can apply the same strategy to compute the least common multiple of a
list of integers:

```python
def my_list_lcm(lst: list[int]) -> int:
    """Calculate LCM for multiple integers"""
    lst = list(set(lst))
    lcm = lst[0]
    for n in lst[1:]:
        lcm = my_lcm(lcm, n)
    return lcm

arr = [12, 15, 27, 30]
print(f"My LCM of the list {arr}: {my_list_lcm(arr)}")
```

Output:

```
My LCM of the list [12, 15, 27, 30]: 540
```

---

#### But Are These Optimal?

Even if we don't have a design to create a more optimal solution for these
computations, we should have an intuitive sense that these algorithms are
not optimized.

Looking at the `my_list_gcd()` and `my_list_lcm()` functions, we can see 
that we're iterating over a loop, inside of which we're executing a 
recursive function.

That isn't conclusive proof that we have a non-optimal solution, but it's
worth considering.

Remembering that `ufunc` functions are designed to replace iterative
processes with vectorized functions for performance, we should consider 
the NumPy alternatives.

---

### NumPy GCD

NumPy exposes the `np.gcd()` function to compute the greatest common
divisor.

You can call the function directly like `np.gcd(x, y)`, if you are just
computing GCD of two numbers.

To compute the GCD of a list or array of numbers, you need to use the 
`reduce()` function to reduce the dimension of the array by one.

```python
import numpy as np

arr = np.array([12, 15, 27, 30])
print(f"NumPy GCD of the array {arr}: {np.gcd.reduce(arr)}")
```

Output:

```
NumPy GCD of the array [12 15 27 30]: 3
```

---

### NumPy LCM

NumPy exposes the `np.lcm()` function to compute least common multiple.

As with GCD, we need to use the `reduce()` function when calling this with
an array.

```python
import numpy as np

arr = np.array([12, 15, 27, 30])
print(f"NumPy LCM of the array {arr}: {np.lcm.reduce(arr)}")
```

Output:

```
NumPy LCM of the array [12 15 27 30]: 540
```

---

### So, which is better?

I've created test functions to time each of the four computations.

I am using the `@timer` decorator function (code in
[utility_functions.py](./utility_functions.py))

```python
import numpy as np
from utility_functions import timer

# -- SNIP --

@timer
def test_my_gcd(lst: list[int]) -> int:
    """Timed test of my_list_gcd()"""
    return my_list_gcd(lst)

@timer
def test_my_lcm(lst: list[int]) -> int:
    """Timed test of my_list_lcm()"""
    return my_list_lcm(lst)

@timer
def test_np_gcd(arr: np.ndarray) -> int:
    """Timed test of np.gcd.reduce()"""
    return np.gcd.reduce(arr)

@timer
def test_np_lcm(arr: np.ndarray) -> int:
    """Timed test of np.lcm.reduce()"""
    return np.lcm.reduce(arr)

lst = [12, 15, 27, 30]
arr = np.array(lst)

print(f"My GCD of the list {lst}: {test_my_gcd(lst)}\n")
print(f"NumPy GCD of the array {arr}: {test_np_gcd(arr)}\n")

print(f"My LCM of the list {lst}: {test_my_lcm(lst)}\n")
print(f"NumPy LCM of the array {arr}: {test_np_lcm(arr)}\n")
```

Output:

```
Execution Time: 4.0 µs
My GCD of the list [12, 15, 27, 30]: 3

Execution Time: 3.4 µs
NumPy GCD of the array [12 15 27 30]: 3

Execution Time: 5.7999 µs
My LCM of the list [12, 15, 27, 30]: 540

Execution Time: 3.7 µs
NumPy LCM of the array [12 15 27 30]: 540
```

For CGD, NumPy's function appears to run about 15% faster.  
For LCM, NumPy's function appears to run about 36% faster.

Considering that NumPy has to reduce the array first, it seems that the
vectorized `ufunc` functions are better optimized.

---
