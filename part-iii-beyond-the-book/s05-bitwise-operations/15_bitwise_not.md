## Using Bitwise NOT (`~`)

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

The bitwise NOT operator (`~`) is used with a single value and returns the
one's complement of the original value (reverses the values of each bit).

You can see the per-bit behavior in the truth table we created previously.

|~|$b$|
|:-:|:-:|
|$0$|$1$|
|$1$|$0$|

---

### An Example

Consider this scenario:

||
|-:|
|$a=1001~1100_2=156_{10}$|
|$~a=0110~0011_2=~~99_{10}$|

```python
b = 0b10011100
print(f"b = {b:>08b}")
n = ~b

# Note: This doesn't give the expected answer
print("n =", bin(n).split('b')[1], "*wrong")
```

Output:

```
b = 10011100
n = 10011101 *wrong
```

---

### A Word of Warning

In Python, all integers are signed. 

Additionally, integers are of arbitrary size.

Because of this, the bitwise NOT operation is going to return unexpected 
results if you're treating a bitwise value as unsigned.

For example, when Python processes the following, it yields the wrong answer.

|||
|-:|-:|
|$a=1001~1100_2=156_{10}$||
|$~a=1001~1101_2=157_{10}$|(*wrong answer)|

```python
b = 0b10011100
n = ~b

# Note: This doesn't give the expected answer
print(f{"n:>08b"})  # -10011101  (*wrong answer)
```

---

### Oh No! Can We Fix It?

However, we can create a function to perform the bitwise NOT operation and
yield the expected result.

```python
def bitwise_not(n, num_bits=8) -> int:
    # Note: I'm cheating a little using a bit-shift here
    #       Don't worry - That lesson is coming up soon
    return ~n & ((1 << num_bits) - 1)

# -- SNIP --

b = 0b10011100
n = bitwise_not(b)  # 01100011 (*right answer)
```

This works because the value of `(1 << num_bits) - 1` (with an 8-bit 
value) will be `1111 1111`

The `&` operation in `~n & ((1 << num_bits) - 1)` will lose the 
sign bit and yield the correct answer.

---

### Real-World Applications

Outside of systems level programming, bitwise NOT doesn't have a ton of 
uses, but it is used (under the covers) in:

* Several encryption algorithms
* High-performance mathematical algorithms
* Bit-masking for IP address computations
* And others

One example where bitwise NOT can be used is when implementing a function 
to set an arbitrary bit in an integer "word"

```python
def set_bit(word: int, pos: int, value: int) -> int:
    # Note: I'm cheating a little using a bit-shift here
    #       Don't worry - That lesson is coming up soon
    mask = 1 << pos
    if value == 0:
        return word & ~mask
    elif value == 1:
        return word | mask
    else:
        return word

def main() -> None:
    for pos in range(0, 8):
        print(set_bit(0, pos, 1))

if __name__ == "__main__":
    main()
```

Output:

```
1
2
4
8
16
32
64
128
```

---
