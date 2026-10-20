## Negative Integers

But that begs the question of how do we handle negative numbers?

---

### Can we use a different value for negatives?

We don't have a separate value to indicate whether a number is 
negative or positive. If we were working in the base $3$, we could
imagine a system in which we used the third possible value as the
negative like this:

|base 3|value|
|:-:|:-:|
|$0$|$0$|
|$1$|$1$|
|$2$|$-1$|

When designing early computation devices, this was given serious
consideration, but the necessity of dealing with three states 
(different voltages) instead of just on and off ($0$ and $1$) made this an
impractical choice.

---

### Can we make the byte itself contain an indicator for negatives?

The next thought was to borrow one of the bits as an indicator for the
sign (positive or negative) of the number.

This is the practice still in use today. For a signed integer, we 
borrow the leftmost (largest value) bit to store the sign (storing a $0$ 
for positive numbers and a $1$ for negative numbers).

In this system, we can see that:

$0000~0001_2=1_{10}$  
The sign bit is zero (positive), and the value of the remaining bits is 1

$1000~0001_2=-1_{10}$  
The sign bit is one (negative), and the value of the remaining bits is 1

... and so on

---

### So we lose half of our (absolute) values

The result of this is that where previously we had $2^8$ (or $256$) values 
using $8$ bits, now we have $2^7$ ($128$) values (since one bit has been 
borrowed), but every value (or *almost* every value) can be either 
positive or negative.

We still need to account for zero, and as we'll see later, it would be
problematic to differentiate between positive and negative zero, so 
there is a built-in imbalance. We have $255$ total non-zero numbers. If
we divide these (such that half are positive and half negative) we wind
up with $127$ for each with one number left over.

In most programming languages, the extra value is a negative, resulting
in a range for an $8$-bit signed integer of $-128$ to $127$.

---

### Why can't the extra value be a positive number?

It would seem like giving the extra value to the negatives is a bit
counter-intuitive, since we probably use positive numbers more 
frequently when we're modeling a counting world.

Believe it or not, there is a logical (and necessary) reason for the
extra value being negative, and the next few topics will explain why 
this is so.

---
