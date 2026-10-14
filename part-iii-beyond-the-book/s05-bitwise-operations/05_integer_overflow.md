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
* The next several sections still apply to how Python represents integers
  in binary, but since the bit size (and therefore the position of the
  sign bit) can change dynamically, Python coders can ignore the effects of
  overflow (for integers).

---

### Overflowing an Unsigned Integer

With an unsigned integer, we can imagine a condition where the value
stored in an integer variable `b` is already all ones when we try
to add `1` to it:

Since Python is not vulnerable to overflow, let's consider this in C

```c

#include <stdio.h>

int main() {
    unsigned char b = 255; // b = 1111 1111
    b++;                   // b = ?
    printf("b = %i", b);

    return 0;
}
```

If we add ```1``` to our integer ```b```, the value (in real world
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
b = 0
```

---

### Overflowing a Signed Integer

The results of integer overflow can become even more surprising when
we look at what happens with a signed integer.

We can again imagine a condition where the value stored in a signed 
integer variable ```s``` is already equal to the maximum value when we 
try to add ```1``` to it.

```c
#include <stdio.h>

int main() {
                  //     ⌄--- remember, this is the sign bit
    char b = 127; // b = 0111 1111
    b++;          // b = ?
    printf("b = %i", b);

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
b = -128
```

As expected, the result is a negative number. But the negative value
isn't what we'd likely expect. It seems like the rest of the value
after the sign bit should be zero. This is also explained over the next
several topics.

---
