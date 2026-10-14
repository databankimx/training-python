## Bit_Shift - Real-World Example: Reconstructing Integers

Bit-shifting can be very useful when we know that a byte represents some 
other value.

### Scenario

You have an incoming data stream that you've read into a byte array.

You know that the incoming data represents $32$-bit integer values and 
that within each set of four bytes, the least significant digits come 
first and the most significant digits last.

You need to reconstruct the integer values from the byte array.

---

### Structure of the Data

Let's imagine that the array contains only one $32$-bit integer, broken up 
into four bytes:

```python
bytes = [ 0b1101_0010, 0b0000_0010, 0b1001_0110, 0b0100_1001 ]
```

---

### First Byte is Easy

We know the first byte represents bits $0$ through $7$, so we can take it 
as-is.

```python
num = bytes[0] # 73
```

---

### Second Byte is Less So

The second byte, however, represents bits $8$ through $15$.

The value of $0000_0010_2$ in isolation is $2_{10}$, and we might naively 
decide to add it to the value we've stored:

```python
# This won't work
num += bytes[1] # 75
```

---

### Fixing the Wrong Answer

But that value doesn't make sense. We know that bits $8$ through $15$ have 
values from $256$ to $32,768$. So, given that at least one of those bits 
is set, we can't possibly have a result less than $256$.

Instead, we need to multiply this byte by $256$ to get the result we expect

```python
num += bytes[1] * 256 # 585
```

---

### Simplifying with Bit-Shift

And that will work, but we'd then have to multiply the third byte by 65,536 
and the fourth by 16,777,216.

Those numbers are pretty easy to remember, but the process would get more 
difficult as we started working with items that are larger than four bytes.

But since they are all powers of two, we can accomplish the same thing by 
bit-shifting:

|Byte|Low Bit|Shift|Value|
|:-:|:-:|:-:|-:|
|$0$|$2^0$|none|$1$|
|$1$|$2^8$|$\ll~8$|$256$|
|$2$|$2^16$|$\ll~16$|$65,536$|
|$3$|$2^24$|$\ll~24$|$16,777,216$|

We can modify the code to use the bit-shift like this:

```python
num += bytes[1] << 8 # 585
```

---

#### Looping Through the Bytes

So, a loop like this would handle each four-byte set:

```python
num = 0
for p in range(4):
    num += bytes[p] << (p * 8)
```

---

### The Whole Solution

I have included an example of this process.

See [reconstructing_integers.py](./19_reconstructing_integers.py)

<details>
<summary>program</summary>
<br>

```python
"""Module to reconstruct integers from a data stream"""

def reconstruct_integers(byte_arr: list[int], size: int=4) -> list[int]:
    """Construct integers from data stream"""
    assert len(byte_arr) % size == 0, "Invalid data!"

    num_units = len(byte_arr) // size

    integers = []

    for n in range(0, num_units * size, size):
        data = byte_arr[n:n+size]
        integers.append(reconstruct_integer(data, size))

    return integers

def reconstruct_integer(data: list[int], size: int=4) -> int:
    """Construct integer from data set"""
    assert len(data) == size, "Invalid data!"

    num = 0
    for i, n in enumerate(data):
        num += n << (i * 8)
    return num

def main() -> None:
    """Test the reconstruct_integers function"""
    byte_arr = [
        0b0000_0000, 0b0000_0000, 0b0000_0000, 0b0000_0000,
        0b1101_0010, 0b0000_0010, 0b1001_0110, 0b0100_1001,
        0b0001_0101, 0b1100_1101, 0b0101_1011, 0b0000_0111,
        0b1111_1111, 0b1111_1111, 0b1111_1111, 0b1111_1111
    ]
    values = reconstruct_integers(byte_arr)
    for value in values:
        out = f"{value:,}"
        print(f"{out:>13}")

if __name__ == "__main__":
    main()
```

</details><br>

Output:

```
            0
1,234,567,890
  123,456,789
4,294,967,295
```

Try putting in some different sets of bytes and see what your output looks 
like.

---
