## Checking for Even Numbers

Whether a number is odd or even is one of the most common checks in a program.
There are two ways to make it: the modulo operator you probably learned first,
and a bitwise AND. The code for this lesson is in
[11_even_numbers.py](./11_even_numbers.py).

---

### Using Modulo

The modulo (or remainder) operator `%` gives the remainder after division. An
even number divides by 2 with no remainder, so `n % 2` is `0` for even numbers
and `1` for odd numbers. Because `0` is false in Python, `not n % 2` is `True`
for even numbers:

```python
def is_even_mod(n: int) -> bool:
    """Check if a number is even (using modulo)"""
    return not n % 2
```

---

### Using Bitwise AND

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

The result is zero, so 42 is even.

> |||
> |-:|-:|
> |$0100~1001_2$|$(73_{10})$|
> |$\underline{\&~0000~0001_2}$|$(1_{10})$|
> |$0000~0001_2$|$(1_{10})$|

The result is one, so 73 is odd.

---

### Running the Script

The script checks both numbers with both methods:

```python
for n in [42, 73]:
    print(f"Using 'n % 2', {n} is {('even' if is_even_mod(n) else 'odd')}")
    print(f"Using 'n & 1', {n} is {('even' if is_even_and(n) else 'odd')}")
```

Output:

```
Using 'n % 2', 42 is even
Using 'n & 1', 42 is even
Using 'n % 2', 73 is odd
Using 'n & 1', 73 is odd
```

Both methods give the same answers. In practice, the choice rarely matters, since
modern compilers usually turn `n % 2` into the same instructions as `n & 1`.

---

### Try It

Add a few more numbers to the list in the script, including zero and a large
number, and check that both methods still agree.

---
