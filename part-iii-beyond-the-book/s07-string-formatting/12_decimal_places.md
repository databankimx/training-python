## Controlling Decimal Precision

One of the most ubiquitous requirements developers encounter is that floating 
point numbers need to be displayed to a specific degree of precision (that 
is, with a specific number of decimal places).

Importantly, we frequently want to avoid rounding the numbers as that might
introduce errors in our calculations.

Python supports specifying decimal precision in the form `.nf` where `n` is
the number of decimal places to display. This does not affect the value in the
stored variable, just the displayed number.

---

### Ignoring Unnecessary Precision

If we consider a number like the mathematical constant `π`, we know that as
an irrational number, it will always include greater precision than we want.

Consider this code:

```python
print(f"π = {math.pi}")
print(f"π = {math.pi:.5f}")
```

Output:

```
π = 3.141592653589793
π = 3.14159
```

---

Interestingly unlike many numerical manipulations in Python, this will
automatically round the decimal to the specified precision as opposed to truncating.

```python
print(f"π = {math.pi}")
print(f"π = {math.pi:.6f}")
```

Output:

```
π = 3.141592653589793
π = 3.141593
```

---

### Including Extra Precision

Limiting a long decimal to a specified precision is certainly important, but
equally important is enduring we include decimal places that might not 
ordinarily be necessary.

For example, when displaying currency values, we want to show exactly two
decimal places, even if they contain zeros.

```python
price = 1.75
qty = 2
total = price * qty
print(f"${total}")
print(f"${total:.2f}")
```

Output:

```
$3.5
$3.50
```

Notice how without the decimal precision specifier, the zero is dropped.

---
