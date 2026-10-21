## Bonus Lesson: Bitwise Logic

Bitwise operators aren't a core part of this course, but they come up often in real Python
code, and they're worth understanding.

### Binary Values

Binary is the base-2 number system. It has only two digits, `0` and `1`.

Our everyday base-10 (decimal) system uses ten digits, 0 through 9. Read a decimal number
from right to left, and each position is worth ten times the one before it. The positions are
powers of ten, starting with 10⁰.

Take the base-10 number `255`. It has five 1s, five 10s, and two 100s:

|10² = 100|10¹ = 10|10⁰ = 1|
|:-:|:-:|:-:|
|2|5|5|

Binary works the same way, with powers of two. Read a binary number from right to left, and each
position is worth twice the one before it, starting with 2⁰.

The binary number `11111111` has one each of 1, 2, 4, 8, 16, 32, 64, and 128:

|2⁷ = 128|2⁶ = 64|2⁵ = 32|2⁴ = 16|2³ = 8|2² = 4|2¹ = 2|2⁰ = 1|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|

Those add up to 255, the largest value an 8-bit byte can hold. So `11111111` in binary is `255`
in decimal, and `00000000` is `0`.

Each binary digit in a computer is called a *bit*.

---

### Using Bits in Place of Booleans

A binary digit has exactly two possible values, and every number in a computer is stored as
binary underneath. So it's natural to use individual bits to store true-or-false values. Let
`1` mean `True` and `0` mean `False`.

In many languages, a boolean takes up a whole byte. Each bit, though, can hold its own yes-or-no
setting, so one byte can hold eight of them. That's the idea behind a *bit-flag*.

Let's keep it small and use only four bits. The value `1001` in binary is `8 + 0 + 0 + 1`, which is
`9` in decimal.

---

### Bitwise AND `&`

The bitwise AND operator (`&`) compares the bits in the same position of two numbers. It sets a
bit to `1` only when both bits are `1`:

|b₁|`&`|b₂|
|:-:|:-:|:-:|
|`1`|**`1`**|`1`|
|`1`|`0`|`0`|
|`0`|`0`|`1`|
|`0`|`0`|`0`|

`&` works on every bit position. Compare decimal 9 (1001 in binary) with decimal 8 (1000):

||8|4|2|1|
|:-:|-|-|-|-|
|9|1|0|0|1|
|8|1|0|0|0|
|`&`|1|0|0|0|

The result is 8.

Here's the key idea. When you `&` a number with a single power of two, the result is that power of
two if its bit is set, and zero if it isn't. Most programming languages use this to build bit-flags.

```python
my_settings = 9   # 1001 binary
my_comparison = 8 # 1000 binary
print(my_settings & my_comparison)
```

Output:

```
8
```

The result is 8, so the bit in the 8s place is set.

A real-world use is a license value that records which of several features are licensed. You can
check each feature with a loop:

```python
license = 9 # 1001 binary
for i in [2 ** x for x in range(4)]:
    if license & i == i:
        print(f"License {i} enabled")
```

Output:

```
License 1 enabled
License 8 enabled
```

---

### Bitwise OR `|`

The bitwise OR operator (`|`) sets a bit to `1` when at least one of the two bits is `1`. This is
the *inclusive* OR:

|b₁|`\|`|b₂|
|:-:|:-:|:-:|
|`1`|**`1`**|`1`|
|`1`|**`1`**|`0`|
|`0`|**`1`**|`1`|
|`0`|`0`|`0`|

Compare 9 and 8 again:

||8|4|2|1|
|:-:|-|-|-|-|
|9|1|0|0|1|
|8|1|0|0|0|
|`\|`|1|0|0|1|

The result is 9.

Here's a practical case. A user belongs to two groups, and each group has its own permissions. In a
system where a user gets every permission they're entitled to, you combine the two sets with `|`:

```python
group_a = 9 # Binary 1001
group_b = 3 # Binary 0011
permissions = group_a | group_b # Binary 1011 (decimal 11)
print(permissions)
```

Output:

```
11
```

---

### Bitwise XOR `^`

The bitwise XOR operator (`^`), for "exclusive OR," sets a bit to `1` only when exactly one of the two
bits is `1`:

|b₁|`^`|b₂|
|:-:|:-:|:-:|
|`1`|`0`|`1`|
|`1`|**`1`**|`0`|
|`0`|**`1`**|`1`|
|`0`|`0`|`0`|

Compare 9 and 8 once more:

||8|4|2|1|
|:-:|-|-|-|-|
|9|1|0|0|1|
|8|1|0|0|0|
|`^`|0|0|0|1|

The result is 1.

```python
my_settings = 9   # 1001 binary
my_comparison = 8 # 1000 binary
print(my_settings ^ my_comparison)
```

Output:

```
1
```

---

### The Reversible Property of `^`

XOR has a useful property: it can be undone. If `c = a ^ b`, then `c ^ b` gives you `a` back.

Using `a = 9` and `b = 8`:

||8|4|2|1||
|:-:|-|-|-|-|-|
|9|1|0|0|1||
|8|1|0|0|0||
|`^`|0|0|0|1|-> **1**|

||8|4|2|1||
|:-:|-|-|-|-|-|
|1|0|0|0|1||
|8|1|0|0|0||
|`^`|1|0|0|1|-> **9**|

---

### Using the Reversibility of `^` for Encryption

Because XOR can be undone, it shows up in cryptography. The scheme below is not secure, but it shows
the idea. Each character takes one byte, so any key from 0 to 255 works.

```python
plaintext = "Hello, World!"
key = 73
# Perform XOR using key on each character in the plaintext string
ciphertext = "".join(chr(ord(c) ^ key) for c in plaintext)
print("ciphertext:", ciphertext)
# Perform XOR using key on each character in the ciphertext string
plaintext = "".join(chr(ord(c) ^ key) for c in ciphertext)
print("plaintext: ", plaintext)
```

Output:

```
ciphertext: ,%%&ei&;%-h
plaintext:  Hello, World!
```

A word of warning about that output. Some of the scrambled characters are control characters, which
have no visible shape. The `H` and the `W`, for example, become characters you can't see. So the
ciphertext looks shorter than the message really is. That's normal. The decryption step brings the
original text back.

---

### Bitwise NOT `~`

Bitwise `~` flips every bit. A `1` becomes a `0`, and a `0` becomes a `1`:

|`~`|b|
|:-:|-|
|0|1|
|1|0|

Using the same 4-bit value, 9:

||8|4|2|1|
|:-:|-|-|-|-|
|9|1|0|0|1|
|`~`|0|1|1|0|

In four bits, that's `0110`, which is 6. You might expect Python to print 6:

```python
my_settings = 9   # 1001 binary
print(~ my_settings)
```

Output:

```
-10
```

Python printed `-10`. So what happened?

---

### Signed Integers Are Weird

To understand `-10`, you need to know how integers are stored.

> Note: Python uses integers of flexible size, so it doesn't store them exactly the way I describe
> below. The principles still hold, though, and they explain the result.

In many languages, an integer uses 32 bits. The binary form of 9 looks like this:
`0000 0000 0000 0000 0000 0000 0000 1001`

Bitwise NOT flips every bit, which gives:
`1111 1111 1111 1111 1111 1111 1111 0110`

The leftmost bit is the sign bit. When it's `1`, the number is negative. In two's complement, a
standard way to store negative numbers, that bit pattern means `-10`. So the NOT of 9 is -10, and
that's the result you saw.

You can see the 32-bit pattern by treating the same value as an unsigned number. Add 2³² to it, and
the bits read as a large positive number:

```python
signed_integer = -10
unsigned_integer = signed_integer + (1 << 32)
print(unsigned_integer)
```

Output:

```
4294967286
```

> **Moral:** Be very careful with bitwise NOT. Unless you understand how negative numbers are stored,
> the results can surprise you.

---

### Bit-Shifts `<<` and `>>`

A bit-shift moves every bit in a value a set number of positions, to the left (`<<`) or to the right
(`>>`).

A shift is an arithmetic operation, not a logical one. Each position in a binary number is a power of
two, so shifting one position left doubles the value. Shifting one position right halves it, and drops
any remainder. (This ignores the sign bit, which is a separate matter.)

```python
x = 2
x <<= 1 # Same as x = x << 1
print(x)
x >>= 1 # Same as x = x >> 1
print(x)
```

Output:

```
4
2
```

The process:

* `x` starts at 2 (`0010`)
* Shifting `0010` one position left gives `0100`, which is 4
* Shifting `0100` one position right gives `0010`, which is 2

> **Beware:** A right shift truncates the value.

```python
x = 3
x >>= 1
print(x)
```

Output:

```
1
```

The process:

* `x` starts at 3 (`0011`)
* Shifting `0011` one position right gives `0001`, which is 1
* The rightmost 1 has nowhere to go, so it's lost

---

You can shift by more than one position:

* `x << y` is the same as `x * 2ʸ`
* `x >> y` is the same as `x // 2ʸ`

```python
x = 5
print(x << 2)
print(x >> 2)
```

Output:

```
20
1
```

* `2² = 4`
* `5 * 4 = 20`
* `5 / 4 = 1.25`, but we drop the decimal part, so
* `5 // 4 = 1`

---

