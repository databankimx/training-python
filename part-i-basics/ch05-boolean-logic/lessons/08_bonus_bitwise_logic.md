## Bonus Lesson: Bitwise Logic

Although the book does not spend time on this topic, understanding bitwise 
operators is very useful for a Python developer.

### Binary Values

First, we need to understand a little about binary
In the binary, or base-2 number system, there are only two digits, `0` and `1`

In our standard base-10 (decimal) system, we have the typical digits, 0 
through 9.

As you traverse a decimal number from right to left, each position represents 
ten times the previous position. That is, the positions represent increasing 
powers of ten, starting from 10⁰.

So, if you have the base-10 number `255`, There are five 1s, five 10s, and two 
100s:

|10² = 100|10¹ = 10|10⁰ = 1|
|:-:|:-:|:-:|
|2|5|5|

In binary, as we traverse a number from left to right, each position 
represents two times the previous position. That is, the positions represent 
increasing powers of two, starting from 2⁰.

So, if you have the same value as a binary number `11111111`, There is one 1, 
one 2, one 4, one 8, one 16, one 32, one 64, and one 128

|2⁷ = 128|2⁶ = 64|2⁵ = 32|2⁴ = 16|2³ = 8|2² = 4|2¹ = 2|2⁰ = 1|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1|1|1|1|1|1|1|

The sum of these is 255 (the max value of a single 8-bit byte)

So, `11111111` binary is equivalent to `255` in decimal  
Likewise, `00000000` binary is equivalent to `0` decimal

And each binary digit in a computer is a *bit*.

---

### Using Bits in Place of Bools

Because there are exactly two possible values in each binary digit (and 
because under the covers all numbers in a computer are stored as binary), it's 
almost inevitable that people would decide to use individual binary digits to 
store boolean values (imagine `1` = `True` and `0` = `False`)

This is useful, because in Python, a boolean value takes up one byte, but by 
using each bit, you can store eight times as many boolean properties in the 
same space. This is the fundamental concept behind a *bit-flag*.

Let's simplify the idea and only use 4 bits in an example.

We use a value of `1001` binary, which is the equivalent of `8 + 0 + 0 + 1 = 9`
in decimal.

---

### Bitwise AND `&`

The bitwise AND operator (`&`) checks a bit across two numbers and sets a 
value of `1` only when both bits are set to `1`

|b₁|`&`|b₂|
|:-:|:-:|:-:|
|`1`|**`1`**|`1`|
|`1`|`0`|`0`|
|`0`|`0`|`1`|
|`0`|`0`|`0`|

The `&` operator operates on every bit position in the two numbers, so if we 
compare decimal 9 (1001 binary) with decimal 8 (1000 binary) ...

||8|4|2|1|
|:-:|-|-|-|-|
|9|1|0|0|1|
|8|1|0|0|0|
|`&`|1|0|0|0|

... we get a result of 8

The principle that when we compare a power of two against any number using
bitwise `&` we get a result containing the same power of two if the bit is set 
(`1`) or zero if the bit is unset (`0`) is how we use *bit-flags* in most
programming languages.

```python
my_settings = 9   # 1001 binary
my_comparison = 8 # 1000 binary
print(my_settings & my_comparison)
```

Output:

```
8
```

This means that the bit we compared (in the 8s place) is set.

One real-world example where we might use this technique is when storing a
license value that identifies whether one of several separate features is
licensed.

We can evaluate this behavior using a loop.

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

Of course, there is a bitwise OR operator (`|`) as well.

Bitwise `|` returns a 1 in each place where at least one of the numbers has a 
1 in that place (inclusive OR)

|b₁|`\|`|b₂|
|:-:|:-:|:-:|
|`1`|**`1`**|`1`|
|`1`|**`1`**|`0`|
|`0`|**`1`**|`1`|
|`0`|`0`|`0`|

The `|` operator operates on every bit position in the two numbers, so if we 
compare the same numbers: decimal 9 (1001 binary) with decimal 8 (1000 
binary) ...

||8|4|2|1|
|:-:|-|-|-|-|
|9|1|0|0|1|
|8|1|0|0|0|
|`\|`|1|0|0|1|

... we get a result of 9

We might imagine an OR scenario where we're checking user permissions when a 
user is in two groups, where permissions available in each group.

In a least-restrictive system, the user would receive the combination of both 
permission sets.

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

For bitwise operations, Python provides an XOR (`^`) or "Exclusive OR"
operator that only sets a place to 1 if exactly one number has a 1 in
that place.

|b₁|`^`|b₂|
|:-:|:-:|:-:|
|`1`|`0`|`1`|
|`1`|**`1`**|`0`|
|`0`|**`1`**|`1`|
|`0`|`0`|`0`|

The `^` operator operates on every bit position in the two numbers, so if we 
compare the same numbers: decimal 9 (1001 binary) with decimal 8 (1000 
binary) ...

||8|4|2|1|
|:-:|-|-|-|-|
|9|1|0|0|1|
|8|1|0|0|0|
|`^`|0|0|0|1|

... we get a result of 1

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

### Reversible Property of XOR `^`

One neat feature of XOR operator is that it is reversible, so if you have
three values such that `c = a ^ b` then `c ^ b == a`

Using `a = 9` and `b = 8`

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

Because of its property of being reversible, bitwise XOR can be used in 
cryptographic systems.

We can create a non-very-secure system using this property alone.

Each character takes up one byte, so we can use any key from 0 to 255 for the
encryption/decryption algorithm.

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

---

### Bitwise NOT `~`

Bitwise `~` swaps each bit in a value so a `1` becomes a `0` and vice versa.

|`~`|b|
|:-:|-|
|0|1|
|1|0|

So, using the same value (9) that we have used in the previous examples:

||8|4|2|1|
|:-:|-|-|-|-|
|9|1|0|0|1|
|`~`|0|1|1|0|

We should get back a value of `0110` binary or 6 decimal.

```python
my_settings = 9   # 1001 binary
print(~ my_settings)
```

Output:

```
-10
```

But instead we got back `-10`!

What gives?!

---

### Signed Integers are Weird

To understand why we got `-10` as the result of our previous computation, we
need to understand how integers are stored in the computer.

There's actually a lot going on here...

> Note: Python actually uses dynamically sized integers, so they are not
> stored exactly like I describe below, but all of the principles except for
> the strict bit-length hold for Python integers as well.

In many programming languages, an integer is stored using 32 bits, so the
binary representation of 9 would be:  
`0000 0000 0000 0000 0000 0000 0000 1001`

Bitwise negation (NOT) is a 1's complement of the number (reverses every
bit), which generates an intermediate result of:  
`1111 1111 1111 1111 1111 1111 1111 0110`

But the leftmost bit of an integer is a sign bit, and when it gets is set
(`1`), that makes the number negative.

Negative integers are represented as 2's complement, which is the same as 1's
complement plus 1, so because the leftmost bit is set, that value is actually
`-10` in decimal.

> Moral: Be super careful using bitwise NOT unless you have a deep 
> understanding of 1's and 2's complements and how they relate to integers in 
> the computer.

---

### Bit-Shifts `<<` and `>>`

Bit-shifting is exactly what it sounds like. When we use these operators, we
shift all of the bits in a value a specified number of positions to the left
`<<` or right `>>`.

This isn't a logical transformation, but an arithmetic one.

Since the positions in a binary number represent powers of two, that means
that bit-shifting one position to the left is the same as multiplying by
two (assuming you don't collide with the sign bit), and bit-shifting one
position to the right is the same as dividing by two (if you ignore the
decimal part of the result).

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

*  `x` begins equal to 2 (`0010`)
*  Bit-shifting `0010` one position left gives `0100` -> `4`
*  Bit-shifting `0100` one position right gives `0010` -> `2`

---

> Beware: Bit-shifting to the right will truncate the value.

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

* `x` begins equal to 3 (`0011`)
*  Bit-shifting `0011` one position right gives `0001` -> `1`
    * The rightmost one has no position to shift into, so it is lost

---

Of course, you can bit-shift more than one place, such that:

* `x << y` is the same as `x * 2ʸ`  
  and
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
* `5 / 4 = 1.25`  
  but we drop the decimal part, so...
* `5 // 4 = 1`

---
