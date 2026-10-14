## An Intuitive (but Wrong) Implementation of Negative Integers

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

For these illustrations, we'll simplify beyond what the computer uses
and imagine a 4-bit integer type.

Since this is a signed integer, we'll use the rightmost bit (the 8s
place) as our sign bit.

---

That means that for our positive values, we have the following set:

* $0000_2 = 0_{10}$
* $0001_2 = 1_{10}$
* $0010_2 = 2_{10}$
* $0011_2 = 3_{10}$
* $0100_2 = 4_{10}$
* $0101_2 = 5_{10}$
* $0110_2 = 6_{10}$
* $0111_2 = 7_{10}$

---

If we implement negative numbers intuitively, we'd assume that all of the
binary digits would be the same as the positive numbers, with only the sign
bit flipped, like this:

* $1000_2 = -0_{10}$
* $1001_2 = -1_{10}$
* $1010_2 = -2_{10}$
* $1011_2 = -3_{10}$
* $1100_2 = -4_{10}$
* $1101_2 = -5_{10}$
* $1110_2 = -6_{10}$
* $1111_2 = -7_{10}$

---

### What's wrong with that?

This approach introduces two major flaws:

1. There are two different values for zero
    * This is wasteful, since there is no mathematical difference between
      $0$ and $-0$
    * It also results in the possibility that adding zero could flip the
      sign on the number to which it's being added.

2. The way the adder circuit works, we would get incorrect answers, so this
   would necessitate a more complicated circuit, affecting performance.
    * Imagine the scenario where we're adding $1 + -1$ (see below)
        * The result (see table in previous topic) of adding two $1$s is $2$
        * It doesn't matter what we do with the sign bit, because
          $1-1=0$, not $2$ or $-2$

---

### Adding Our Invalid Negatives

Recall that $0-1$ is the same as $0+-1$ so let's look at the
result of that (using our intuitive system) in binary addition

$1_{10}$ (as 4-bit binary) is $0001_2$

$-1_{10}$ (as 4-bit binary) is $1001_2$

> ||
> |-:|
> |$0001_2$|
> |$\underline{+~1001_2}$|
> |$1010_2$|

So according to our system, $1-1=-2$, which is obviously wrong

---

### Overflowing into the Sign Bit

Other numbers can lose a carry bit and flip the sign.

Consider $7-3$ or $7+-3$

$7_{10}=0111_2$

$-3_{10}=1011_2$

> ||
> |-:|
> |$0111_2$|
> |$\underline{+~1011_2}$|
> |$0010_2$|

So according to our system, $7-3=2$ (wrong again!)

---

### What Now?

So, this solution is clearly not going to work. The next idea is...

---
