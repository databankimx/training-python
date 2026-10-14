## Using Bitwise XOR (`^`)

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

The bitwise XOR operator (`^`) compares two values and returns 1 in 
each position where the bits are not equal across the two values. That is, 
one or the other of the bits (but not both) contains a 1.

This *exclusive* OR operation follows the truth table below:

|$b_1$|^|$b_2$|
|:-|:-:|-:|
|$1$|$0$|$1$|
|$1$|$1$|$0$|
|$0$|$1$|$1$|
|$0$|$0$|$0$|

---

### An Example

Consider this scenario:

||
|-:|
|$a=1001~1100_2=156_{10}$|
|$b=0011~0100_2=~~52_{10}$|
|$a~\^~~b=1010~1000_2=168_{10}$|

Any position where either value's bit is $1$ (excluding when both are set) 
will return a $1$.

As long as we understand that what's being compared are the individual
bits, we can express the values in any base with the same results

```python
a = 0b10011100 # 156
b = 0b00110100 # 52
print(f"{(a ^ b):>08b}") # --> 10101000 (168)

x = 156
y = 52
print(x ^ y) # --> 168
```

Output:

```
10101000
168
```

---

### A Simple Use-Case: Swapping Two Values

A simple example of using bitwise XOR is swapping two values without
creating a temp variable.

```python
def swap_values(a: int, b: int) -> tuple[int, int]:
    a = a ^ b
    b = b ^ a
    a = a ^ b
    return a, b

a = 5
b = 8
print(f"a = {a}, b = {b}")
# Of course, in Python, we could, just do `a, b = b, a` to swap values
#    but we'll use the XOR method to see how it works
a, b = swap_values(a, b)
print(f"a = {a}, b = {b}")
```

Output

```
a = 5, b = 8
a = 8, b = 5
```

---

Let's look at how this works.

At the start:

* $a=5_{10}=0101_2$
* $b=8_{10}=1000_2$

So, the swap process looks like this:

Step 1: ```a = a ^ b```

||
|-:|
|$0101_2$|
|$\underline{\^~~~1000_2}$
|$1101_2$|

Step 2: ```b = a ^ b```

||
|-:|
|$1101_2$|
|$\underline{\^~~~1000_2}$
|$0101_2$|

... now $b$ contains $a$'s original value

Step 3: ```a = a ^ b```

||
|-:|
|$1101_2$|
|$\underline{\^~~~1000_2}$
|$0101_2$|

... now $a$ contains $b$'s original value

---
