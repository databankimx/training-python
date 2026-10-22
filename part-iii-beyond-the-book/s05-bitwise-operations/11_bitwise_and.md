## Using Bitwise AND (`&`)

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

The bitwise AND operator (`&`) is used to compare two values and return
only the intersection of their set ($1$) bits.

At each binary position ($i$), the result of the operation is equivalent to
multiplying the bits together and can be expressed as follows.

$$(a~\&~b)_i=a_i\times b_i$$

Since $1\times1=1$, and for any number $n\times0=0$, we can see that 
this matches the bitwise truth table we laid out for this operator, where 
a $1$ is returned only in bit positions where both of the compared values 
contain $1$.

> |$b_1$|$\&$|$b_2$|
> |:-|:-:|-:|
> |$1$|$1$|$1$|
> |$1$|$0$|$0$|
> |$0$|$0$|$1$|
> |$0$|$0$|$0$|

---

### Example

Consider this scenario:

> ||
> |-:|
> |$a=1001~1100_2=156_{10}$|
> |$b=0011~0100_2=~~52_{10}$|
> |$a~\&~b=0001~0100_2=~~20_{10}$|

Only the positions where the bit is $1$ in both $a$ and $b$ return a $1$ 
from the $\&$ operation.

As long as we understand that what's being compared are the individual
bits, we can express the values in any base with the same results

The code for this lesson is in [11_bitwise_and.py](./11_bitwise_and.py).

```python
a = 0b10011100 # 156
b = 0b00110100 # 52
print(f"{bin(a & b)[2:]:>08}") # --> 00010100 (20)

x = 156
y = 52
print(x & y) # --> 20
```

Output:

```
00010100
20
```

---

### A Simple Example: Checking for Even Numbers

There are many places where it's useful to check if a number is odd or even.
There are two ways to check it: the modulo operator you probably learned first,
and a bitwise AND.

#### Using Modulo

The modulo (or remainder) operator `%` gives the remainder after division. An
even number divides by 2 with no remainder, so `n % 2` is `0` for even numbers
and `1` for odd numbers. Because `0` is false in Python, `not n % 2` is `True`
for even numbers:

```python
def is_even_mod(n: int) -> bool:
    """Check if a number is even (using modulo)"""
    return not n % 2
```

#### Using Bitwise AND

Every number is stored in binary, and the ones place (the rightmost bit) is
`1` only for odd numbers. Since the only other bits are powers of two, which
are all even, `n & 1` keeps just the ones-place bit. So `n & 1` is `0` for
even numbers and `1` for odd numbers:

```python
def is_even_and(n: int) -> bool:
    """Check if a number is even (using bitwise AND)"""
    return not n & 1
```

Let's check the number 42 and the number 73 by hand:

> |||
> |-:|-:|
> |$0010~1010_2$|$(42_{10})$|
> |$\underline{\&~0000~0001_2}$|$(1_{10})$|
> |$0000~0000_2$|$(0_{10})$|

Since no position has ones in both numbers, the result is zero (even).

> |||
> |-:|-:|
> |$0100~1001_2$|$(73_{10})$|
> |$\underline{\&~0000~0001_2}$|$(1_{10})$|
> |$0000~0001_2$|$(1_{10})$|

The ones place has ones in both numbers, as it must for an odd number, 
since $2^0=1$ is the only odd power of two, so the result is one (odd).

#### Running the Checks

The script's `main()` checks both numbers with both methods, after the AND
examples above:

```python
for n in [42, 73]:
    print(f"Using 'n % 2', {n} is {('even' if is_even_mod(n) else 'odd')}")
    print(f"Using 'n & 1', {n} is {('even' if is_even_and(n) else 'odd')}")
```

Full output of the script:

```
00010100
20
Using 'n % 2', 42 is even
Using 'n & 1', 42 is even
Using 'n % 2', 73 is odd
Using 'n & 1', 73 is odd
```

Both methods give the same answers. Historically, a bitwise check was faster than
a modulo computation, because division was costly for the hardware. Compilers now
optimize well-known patterns like this one, so in Python the speed difference is
negligible, and you should choose whichever reads better for your code.

---

### Try It

Add a few more numbers to the list in `main()`, including zero, a large number,
and a negative number, and check that both methods still agree.

---
