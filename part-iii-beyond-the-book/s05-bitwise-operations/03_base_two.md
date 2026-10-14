## Base 2 (Binary)

Remember our rule:

Starting from the rightmost position and traversing right-to-left, the 
place values are $b^p$ where $b$ is the base and $p$ is the position 
relative to the rightmost number (how many digits away).

---

### Position Values

Following the same logic we saw in base $10$, in base $2$, the position 
values are just powers of two instead of ten (although I will express 
their values as base $10$ here for convenience):

* $2^0=1$
* $2^1=2$
* $2^2=4$
* $2^3=8$
* $2^4=16$
* $2^5=32$
* $2^6=64$
* $2^7=128$
* and so on

This means in our binary byte we have the following places:

||||||||||
|-|-|-|-|-|-|-|-|-|
|...|$128$s|$64$s|$32$s|$16$s|$8$s|$4$s|$2$s|$1$s|

---

### Computed Values

Reading binary numbers is similar to decimal: the sum of the non-zero 
position values.

So:

* $0000~0000_2 = 0_{10}$
* $0000~0001_2 = 1_{10}=(1\times1)$
* $0000~0010_2 = 2_{10}=(1\times2)+(0\times1)$
* $0000~0011_2 = 3_{10}=(1\times2)+(1\times1)$
* ...
* $1111~1111_2 = 255_{10}=(128+64+32+16+8+4+2+1)$

That means that there are $256$ possible values available in an $8$-bit 
byte, which makes perfect sense, since $2^8=256$.

And for an unsigned $8$-bit integer, these values range from $0$ to $255$

---
