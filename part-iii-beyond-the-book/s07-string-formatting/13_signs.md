## Positive/Negative Signs on Numbers

Often with numbers, it's important to determine whether or not the sign 
(indicating positive or negative) should be shown.

Sometimes we want to display numbers the way we do in arithmetic class (show
a minus `-` for negative numbers). Other times we may wish to explicitly show 
a `+` for positive numbers.

This table illustrates the format specifiers for signs on numerical data:

|Symbol|Effect|
|:-:|-|
|`+`|Show signs on both positive and negative numbers|
|`-`|Show sign only on negative numbers|
|(space) ` `|Show sign on negative or a single space on positive numbers|
|`=`|Preceding one of the above, moves the sign to the left of the full width|

> Note: Even though we don't review this until the next lesson, I am 
> including a 5-character width specification in all of these examples to 
> make it clear what behavior is occurring.

---

### Showing Positive and Negative Signs

The `+` symbol indicates that signs should be shown on both positive and 
negative numbers.

Here, `+5d` indicates a 5-character width along with the +/- signs on an 
integer:

```python
nums = [1, -7, 42]
for n in nums:
    print(f"[+5d]  '{n:+5d}'")
```

Output:

```
[+5d]  '   +1'
[+5d]  '   -7'
[+5d]  '  +42'
```

---

#### Left-Justify Signs

Preceding the `+` with an `=` symbol moves the sign to the left of the total
width allocated:

```python
nums = [1, -7, 42]
for n in nums:
    print(f"[=+5d]  '{n:=+5d}'")
```

Output:

```
[=+5d] '+   1'
[=+5d] '-   7'
[=+5d] '+  42'
```

---

### Only Showing Negative Signs

The `-` symbol indicates that signs should be shown on negative numbers only.

Here, `-5d` indicates a 5-character width along with the `-` sign (if needed) 
on an integer:

```python
nums = [1, -7, 42]
for n in nums:
    print(f"[-5d]  '{n:-5d}'")
```

Output:

```
[-5d]  '    1'
[-5d]  '   -7'
[-5d]  '   42'
```

---

#### Left-Justify Signs

Preceding the `-` with an `=` symbol moves the sign to the left of the total
width allocated:

```python
nums = [1, -7, 42]
for n in nums:
    print(f"[=-5d]  '{n:=-5d}'")
```

Output:

```
[=-5d]  '    1'
[=-5d]  '-   7'
[=-5d]  '   42'
```

---

### Maintaining Alignment

Using a single space instead of either the `+` or `-` symbol indicates that
only negative values show a sign, but positive values are preceded by a 
single space character (to maintain alignment).

Here, ` 5d` indicates a 5-character width along with the `-` sign (if needed) 
or a space on an integer:

```python
nums = [1, -7, 42]
for n in nums:
    print(f"[ 5d]  '{n: 5d}'")
```

Output:

```
[ 5d]  '    1'
[ 5d]  '   -7'
[ 5d]  '   42'
```

---

#### Left-Justify Signs

Preceding the blank space with an `=` symbol moves the sign to the left of 
the total width allocated:

```python
nums = [1, -7, 42]
for n in nums:
    print(f"[= 5d]  '{n:= 5d}'")
```

Output:

```
[= 5d]  '    1'
[= 5d]  '-   7'
[= 5d]  '   42'
```

---
