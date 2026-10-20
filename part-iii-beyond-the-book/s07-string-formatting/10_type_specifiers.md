## Data Type Specifiers

Python supports specifying the following data type formats:

|Symbol|Presentation Type|
|:-:|-|
|`b`|Binary integer|
|`c`|Single character|
|`d`|Decimal integer|
|`e` or `E`|Exponential (scientific) notation (floating point)|
|`f` or `F`|Floating point|
|`g` or `G`|General: integer, sci. notation, or float depending on magnitude|
|`o`|Octal integer|
|`s`|String|
|`x` or `X`|Hexadecimal integer|
|`%`|Percentage|

---

### Examples

Let's consider the number `42` printed with a variety of type specifiers:

```python
answer = 42
print(f"d: {answer:d}")
print(f"b: {answer:b}")
print(f"e: {answer:e}")
print(f"f: {answer:f}")
print(f"g: {answer:g}")
print(f"o: {answer:o}")
print(f"X: {answer:X}")
print(f"%: {answer / 100:.0%}")
print(f"c: {answer:c}")
print(f"s: {str(answer):s}")
```

Output:

```
d: 42
b: 101010
e: 4.200000e+01
f: 42.000000
g: 42
o: 52
X: 2A
%: 42%
c: *
s: 42
```

---

### The `#` Modifier

Adding a `#` character immediately preceding the type specifier has the
following effects:

* For non-decimal integer types, the `#` character adds a label indicating the
  type base.
* For the general type, the `#` character adds a decimal point whether or not 
  it is required for the value

```python
answer = 42
print(f"b: {answer:#b}")
print(f"o: {answer:#o}")
print(f"X: {answer:#X}")
print(f"g: {answer:#g}")
```

Output:

```
b: 0b101010
o: 0o52
X: 0X2A
g: 42.0000
```

---
