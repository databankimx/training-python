## Float Rounding Error

We saw before that we can encounter unexpected rounding errors when
working with floating point numbers.

Why?

---

### Binary can only represent approximations for floating point numbers

Any number that can be represented in binary in a computer can always be 
expressed as an integer multiplied by an integer power of two thus:

$$i=n(2^m)|(m,n)\in\Z$$

This means that:

1.	There are no real floating-point decimals inside the computer.
2.	The majority of floating-point value approximations are inexact.  
    We just select the nearest value that the computer can express.  
    For example:  
    $\small 0.1 \approx 7205759403792794 \times 2^{-56} \approx 0.10000000000000000555$  
    $\small 0.2 \approx 7205759403792794 \times 2^{-55} \approx 0.2000000000000000111$

Because the values above do not show a discrepancy until the 18th decimal 
place, you often will not see the rounding error visually in your results. 
Nevertheless, it is there.

``` python
print(.1)
print(.2)
```

Output:

```
0.1
0.2
```

---

At 0.3, the discrepancy is a bit below the real value instead of above, 
but still does not show as part of our output

$$\small0.3 \approx 5404319552844595 \times 2^{-54} \approx 0.29999999999999998889776975$$

```python
print(.3)
```

Output:

```
0.3
```

---

### The sum of two approximations is not an approximation of the real value

However, the sum of the approximations of 0.1 and 0.2 is not an 
approximation of 0.3  

$$\small 0.10000000000000000555 + 0.2000000000000000111 \approx 0.000000000000004440$$

Here, the rounding error has changed, because the computer doesn't know 
anything about us expecting an approximation of 0.3, just about the 
request to find the sum of the approximations of 0.1 and 0.2

Additionally, in Python we get to see 17 decimal places in our output, and 
since the decimal rounding error has moved into the 17th instead of 18th 
position, we now actually see the rounding error in our code results.

```python
print(0.1 + 0.2)
```

Output:

```
0.30000000000000004
```

---

### OK - What do I do now?

There are many strategies that we can implement to mitigate the effect of
rounding error when working with floating point numbers, but the main
thing is to be aware that this can (and *will*) happen and to write your 
code in such a fashion as to avoid allowing it to impact your final 
results.

---
