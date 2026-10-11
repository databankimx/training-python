## Bonus Lesson: Bitwise Logic

### Binary Values

In binary (base-2), there are only two digits: `0` and `1`. Each binary digit
is a *bit*. Positions represent increasing powers of two from right to left.

The value `11111111` binary equals `128+64+32+16+8+4+2+1 = 255` decimal - the
maximum value of a single 8-bit byte.

---

### Using Bits in Place of Booleans

Because each bit has exactly two possible values, bits naturally represent
boolean values (`1` = `True`, `0` = `False`). Storing eight booleans in a
single byte (instead of one per byte) is the fundamental concept behind a
*bit-flag*.

---

### Bitwise AND `&`

Sets a bit to `1` only when both input bits are `1`.

| b₁ | `&` | b₂ |
|:-:|:-:|:-:|
| `1` | **`1`** | `1` |
| `1` | `0` | `0` |
| `0` | `0` | `1` |
| `0` | `0` | `0` |

Example: comparing decimal 9 (`1001`) with decimal 8 (`1000`):

| | 8 | 4 | 2 | 1 |
|:-:|-|-|-|-|
| 9 | 1 | 0 | 0 | 1 |
| 8 | 1 | 0 | 0 | 0 |
| `&` | 1 | 0 | 0 | 0 |

Result: 8. This means the bit in the 8s position is set.

```python
my_settings = 9   # 1001 binary
my_comparison = 8 # 1000 binary
print(my_settings & my_comparison)
```

Output:

```
8
```

Evaluating all bit-flags in a value using a loop:

```python
license = 9  # 1001 binary
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

Sets a bit to `1` when at least one input bit is `1` (inclusive OR).

| b₁ | `\|` | b₂ |
|:-:|:-:|:-:|
| `1` | **`1`** | `1` |
| `1` | **`1`** | `0` |
| `0` | **`1`** | `1` |
| `0` | `0` | `0` |

```python
group_a = 9  # 1001 binary
group_b = 3  # 0011 binary
permissions = group_a | group_b  # 1011 binary = 11 decimal
print(permissions)
```

Output:

```
11
```

---

### Bitwise XOR `^`

Sets a bit to `1` only when exactly one input bit is `1`.

| b₁ | `^` | b₂ |
|:-:|:-:|:-:|
| `1` | `0` | `1` |
| `1` | **`1`** | `0` |
| `0` | **`1`** | `1` |
| `0` | `0` | `0` |

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

### Reversible Property of XOR

If `c = a ^ b`, then `c ^ b == a`. XOR is its own inverse.

---

### Using XOR Reversibility for Encryption

```python
plaintext = "Hello, World!"
key = 73
# XOR each character in plaintext with the key
ciphertext = "".join(chr(ord(c) ^ key) for c in plaintext)
print("ciphertext:", ciphertext)
# XOR each character in ciphertext with the same key to recover plaintext
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

Swaps every bit: `1` becomes `0` and vice versa.

```python
my_settings = 9   # 1001 binary
print(~my_settings)
```

Output:

```
-10
```

The result is `-10` rather than `6` because Python integers are signed. The
leftmost bit is a sign bit; when it is set after negation, the value is
interpreted as negative via 2's complement arithmetic.

> Avoid bitwise NOT unless you have a solid understanding of signed integer
> representation and 2's complement.

---

### Bit-Shifts `<<` and `>>`

Shifts all bits left (`<<`) or right (`>>`). Each left-shift by one position
multiplies by 2; each right-shift divides by 2 (truncating).

```python
x = 2
x <<= 1  # same as x = x << 1 -> 4
print(x)
x >>= 1  # same as x = x >> 1 -> 2
print(x)
```

Output:

```
4
2
```

More than one position at a time: `x << y` is `x * 2ʸ`, and `x >> y` is
`x // 2ʸ`.

```python
x = 5
print(x << 2)  # 5 * 4 = 20
print(x >> 2)  # 5 // 4 = 1
```

Output:

```
20
1
```

> **Beware:** right-shifting truncates - the bits that fall off the right end
> are lost.

---
