## Integer Overflow

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

There is a general problem when working with a fixed number of bits.

What happens when we exceed the maximum value? That is to say, what 
happens when we run out of bits when performing an arithmetic 
operation?

This scenario is known as "overflow," and it can have odd (but 
predictable) behavior.

A Note about Python:
* Python implements integers with a dynamic number of bits.
* This means that it is not possible to overflow an integer in Python.
* Python integers have no fixed size, and so no fixed sign bit. The next several
  sections still apply to how integers are represented in binary in general, but
  Python programmers can ignore the effects of overflow for integers.

---

### Overflowing an Unsigned Integer

With an unsigned integer, we can imagine a condition where the value
stored in an integer variable `ub` is already all ones when we try
to add `1` to it:

Since Python is not vulnerable to overflow, let's consider this in C.

The code for this section is in [05_integer_overflow.c](./05_integer_overflow.c).
To run it, compile it with a C compiler, such as `gcc 05_integer_overflow.c -o overflow`,
and then run the program that the compiler creates.

```c
#include <stdio.h>

int main() {
    unsigned char ub = 255; // ub = 1111 1111
    ub++;                   // ub = ?
    printf("\nub = %i\n", ub);

    return 0;
}
```

If we add `1` to our integer `ub`, the value (in real world
numbers) would be $256$

> |||
> |-:|-:|
> |$1111~1111_2$|$255_{10}$|
> |$\underline{+~0000~0001_2}$|$\underline{+~~~~~1_{10}}$|
> |$1~0000~0000_2$|$256_{10}$|

But as you can see, that would require a ninth bit, which we don't 
have available in a fixed-size, $8$-bit value.

In the computer, the binary math is computed the same way as real-world
arithmetic, but when the carry value of 1 moves to the 9th bit, it is 
simply lost, the result of which is that we see  

$$255+1=0$$

> |||
> |-:|-:|
> |$1111~1111_2$|$255_{10}$|
> |$\underline{+~0000~0001_2}$|$\underline{+~~~~~1_{10}}$|
> |${1\mkern-9mu/}~0000~0000_2$|$0_{10}$|

Output:

```
ub = 0
```

---

### Overflowing a Signed Integer

The results of integer overflow can become even more surprising when
we look at what happens with a signed integer.

We can again imagine a condition where the value stored in a signed 
integer variable `sb` is already equal to the maximum value when we 
try to add `1` to it.

```c
#include <stdio.h>

int main() {
                  //     ⌄--- remember, this is the sign bit
    char sb = 127; // sb = 0111 1111
    sb++;          // sb = ?
    printf("\nsb = %i\n\n", sb);

    return 0;
}
```

The arithmetic in the real world looks like this:

> |||
> |-:|-:|
> |$0111~1111_2$|$127_{10}$|
> |$\underline{+~0000~0001_2}$|$\underline{+~~~~~1_{10}}$|
> |$1000~0000_2$|$128_{10}$|

But, what's happened in our integer is that while we haven't 
overflowed outside the $8$-bit size, we ***have*** overflowed our value
into the sign bit.

> ||||
> |-:|-:|-|
> |$0111~1111_2$|$127_{10}$||
> |$\underline{+~0000~0001_2}$|$\underline{+~~~~~1_{10}}$||
> |$1000~0000_2$|$-128_{10}$|(why ?)|

$$127+1=-128~~???$$

Output:

```
sb = -128
```

The `1000 0000` pattern is what we'd expect for 128 if the leftmost bit were just
another bit. But because it's the sign bit, the pattern is read as a negative
number. The exact negative value depends on how the computer stores negatives,
which the next several topics explain.

> Note: In C, overflowing a signed integer is undefined behavior. The C standard
> doesn't say what happens, so a compiler is allowed to do something else. On most
> current systems you'll see `-128`, but that isn't guaranteed. Unsigned overflow,
> as in the first example, is defined: it wraps around to 0.

---
