## Two's Complement

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

Enter the solution that is implemented for numbers in modern computing: **two's complement**

Two's complement is just one's complement *plus one*.

---

### A Four-Bit Example

So with our known positive values (in our imaginary 4-bit integer):

* $0000_2=0_{10}$
* $0001_2=1_{10}$
* $0010_2=2_{10}$
* $0011_2=3_{10}$
* $0100_2=4_{10}$
* $0101_2=5_{10}$
* $0110_2=6_{10}$
* $0111_2=7_{10}$

---

The two's complement implementation for negatives would look like this:

* $0000_2= ~~~0_{10}$
* $1111_2=-1_{10}$
* $1110_2=-2_{10}$
* $1101_2=-3_{10}$
* $1100_2=-4_{10}$
* $1011_2=-5_{10}$
* $1010_2=-6_{10}$
* $1001_2=-7_{10}$  
  ... which would leave a wasted bit, so ...
* $1000_2=-8_{10}$

... and this is why we have an extra negative value in integer data types

---

### Does This Really Work?

We can check ourselves by looking at the same examples we've been using:

---

### $1-1$

> ||
> |-:|
> |$0001_2$|
> |$\underline{+~1111_2}$|
> |$1\Larr0000_2$|

We don't care about the lost carry bit (adding one accounted for it),
but now we get the correct answer: $1-1=0$

---

### $7-3$

> ||
> |-:|
> |$0111_2$|
> |$\underline{+~1101_2}$|
> |$1\Larr0100_2$|

Again, although we lose a carry bit, we end up with the right answer:
$7-3=4$

---

### Problem Solved!

Implementation of a two's complement negatives system ensures that we
always get the correct answer when performing binary addition with our
adder circuits, even if the signs don't match.

---

### Wait a minute! Now integer overflow makes sense too!

Now that we understand that the number system uses two's complement for
negatives, the overflow behavior we saw earlier makes sense.

If we go back to using an 8-bit integer, and look at our 127 + 1 problem:

```c
#include <stdio.h>

int main() {
                  //     ⌄--- remember, this is the sign bit
    char b = 127; // b = 0111 1111 =  127
    b++;          // b = 1000 0000 = -128
    printf("b = %i", b);

    return 0;
}
```

We can predict that this is the expected overflow behavior by doing the
binary addition:

> ||
> |-:|
> |$0111~1111_2$|
> |$\underline{+~0000~0001_2}$|
> |$1000~0000_2$|

And we see the previously inexplicable behavior of $127+1=-128$ for
an 8-bit signed integer emerge as a result of overflowing into the sign 
bit.

---

### Verification

Just to verify that this is the expected behavior:

* $128_{10}$ in binary is $1000~0000_2$
* One's complement of that is $0111~1111_2$
* Two's complement (one's complement plus one) then is $1000~0000_2$

So, $-128$ is the expected result of the overflow

---
