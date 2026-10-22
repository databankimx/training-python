## A Bit about Integers

> *"I see what you did there..."*  
> &nbsp;&nbsp;~Literally Everyone

A byte is comprised of 8 bits, each of which can be a one or a zero. 
Binary (base 2) is the basis of bitwise computation.

In many languages, such as C and Java, the default integer type is typically 
32 bits (four bytes) long, but for simplicity, we'll work with 8-bit integers in 
this lesson.

---

### Position Values

In all of our numbering systems, the position values (1's place, e.g.) 
are computable. Starting from the rightmost position and traversing 
right-to-left, the place values are $b^p$ where $b$ is the base and $p$ is 
the position relative to the rightmost number (how many digits away).

---

So, for any numbering system, the place values look like this.

||||||
|-|-|-|-|-|
|...|$b^3$|$b^2$|$b^1$|$b^0$|

---

And reading the value of a number, where $d$ is the digit in a given 
place, looks like this (sum of each digit times its position value):

||||||
|-|-|-|-|-|
|...|$+d(b^3)$|$+d(b^2)$|$+d(b^1)$|$+d(b^0)$|

---

As an example, the base-two number `1011` has a 1 in the $2^3$, $2^1$, and $2^0$
places, and a 0 in the $2^2$ place:

$$1011_2 = 1(2^3) + 0(2^2) + 1(2^1) + 1(2^0) = 8 + 0 + 2 + 1 = 11_{10}$$

---
