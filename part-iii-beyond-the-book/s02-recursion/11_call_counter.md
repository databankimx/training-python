## Discussing Inefficiency: The Fibonacci Sequence

At the beginning of this topic, I mentioned that one of the most famous
recursion examples is the Fibonacci Sequence.

Many computer science courses (including, lamentably, my original version of
this section of lessons) use the Fibonacci Sequence as the first (and 
sometimes only) example for recursion, with the result that many students fail
to see the utility of recursive functions, instead viewing them in the light
of an intellectual curiosity.

Instead of beginning here, then, we'll use the Fibonacci Sequence as an
example of how to find and improve inefficiencies in our recursive algorithms.

---

### How Will We Keep Track of Efficiency?

For this topic, instead of timing completion (which is still important), we'll
track the number of recursive calls are necessary for our function to compute
a given solution.

For this purpose, I have provided a special class `CountCalls` that can be
used as a decorator on the functions we develop and test.

This class implements an override of the `__call__()` method to wrap a
function with a counter and expose its value after all recursive calls
complete.

See [count_calls.py](./count_calls.py)

```python
class CountCalls:
    """Class to allow counting the times a recursive function is called"""

    def __init__(self, func: callable):
        """Initialize"""
        self._count = 0
        self._func = func

    def __call__(self, *args, **kwargs):
        """Magic method override to add to counter and execute function"""
        self._count += 1
        return self._func(*args, **kwargs)
    
    @property
    def call_count(self):
        """Number of times the recursive function has been called"""
        return self._count
```

We implement this in our code by decorating a function thus:

```python
from count_calls import CountCalls

@CountCalls
def recursive_function(*args, **kwargs) -> return:
    ...

recursive_function()
print(recursive_function.call_count)
```

---

### History of the Fibonacci Sequence

The Fibonacci Sequence is a well-known mathematical sequence with ties to
countless real-world phenomena. Although its discovery is credited to
Leonardo Fibonacci (or Leonardo of Pisa) around 1170 CE (and published in
his book *Liber Abaci* in 1202), ancient Sanskrit texts predating Leonardo by
centuries have been found containing both descriptions and formulae for the 
sequence.

Regardless of its history, the Fibonacci Sequence is of profound importance in
both mathematical and physical investigations of our world.

---

### Properties of the Fibonacci Sequence

The rules of the Fibonacci Sequence are quite simple: the value of any term in
the sequence is the sum of the prior two terms.

`0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, …`

In mathematical terms, the properties are then:

* `F(0) = 0`
* `F(1) = 1`  
  and for all other non-negative integers:
* `F(n) = F(n-1) + F(n-2)`

You can see that for integers larger than one, the formula defining the 
Fibonacci Sequence is recursive even before we implement any code. By
definition, we have to call the formula to solve the formula.

> Note: An interesting property of the Fibonacci Sequence is that as *n*
> gets larger, F(*n*) / F(*n*-1) approaches phi (φ), the golden ratio:  
> F(*n*) / F(*n*-1) ≈ φ ≈ 1.618

---
