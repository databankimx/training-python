## Using Bit-Shifts (`<<` and`>>`)

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

A bit-shift operation literally shifts the bit values in a field a
specified number of positions to the left (`<<`) or right (`>>`).

---

### Right Bit-Shift is Division by Two

Right-shifting a value is equivalent to dividing the value by two to the 
power of the number of positions shifted:

$$n~\texttt{>>}~p=n\div2^p$$

So, if we have a value $n=128$, and bit-shift it to the right $3$ 
places, we get the value $128/2^3=16$

```python
x = 128
b = x >> 3
print(f"{x} >> 3 = {b}")
```

Output:

```
128 >> 3 = 16
```

Looking at that in binary, we have:

> |||||
> |-|-:|-:|-|
> ||$1000~0000_2$|($128_{10}$)||
> ||$\uparrow~~~\downarrow~~~~~~~~~~~$||(the $1$ moves three places to the right)|
> |$\texttt{>>}~3$|$0001~0000_2$|($16_{10}$)

---

### Left Bit-Shift is Multiplication by Two

Left-shifting a value is equivalent to multiplying the value by two to the 
power of the number of positions shifted:

$$n~\texttt{<<}~p=n\times2^p$$

With our existing value $n=16_{10}$, if we shift to the left three places, 
we get the value $16\times2^3=128$

```python
x = 16
b = x << 3
print(f"{x} << 3 = {b}")
```

Output:

```
16 << 3 = 128
```

> |||||
> |-|-:|-:|-|
> ||$0001~0000_2$|($16_{10}$)||
> ||$\downarrow~~~\uparrow~~~~~~~~~~~$|(the $1$ moves three places to the left)|
> |$\texttt{<<}~3$|$1000~0000_2$|($128_{10}$)

---

### Overflow and Underflow Can Result in Data Loss

Assuming we're limited to $8$ bits, what happens when we shift so that we
overflow a bit into the ninth (or tenth) bit position?

#### No Overflow In Python

Python integers grow dynamically, so as long as there is memory available,
we will not encounter overflow.

```python
# Overflow doesn't happen in Python
x = 64
b = x << 3
print(f"{x} << 3 = {b}")
```

Output:

```
64 << 3 = 512
```

Binary View:

> |||||
> |-|-:|-:|-|
> ||$0100~0000_2$|($64_{10}$)||
> ||$~\downarrow~~~~~\uparrow~~~~~~~~~~~~~~$|(the $1$ moves three places to the left)|
> |$\texttt{<<}~3$|$10~0000~0000_2$|($512_{10}$)

The Python integer grows to support the extra bits required.

---

#### Overflow in Languages with Static-Size Integer Types

Let's take a look at integer overflow in C. We'll use an `unsigned char` type,
which is the equivalent of an $8$-bit byte in C.

See [bit_shift_overflow.c](./18_bit_shift_overflow.c)

```c
#include <stdio.h>

int main() {
    unsigned char x, b;

    // Overflow
    x = 64;
    b = x << 3;
    printf("%d\n", b);

    return 0;
}
```

Output:

```
64 << 3 = 0
```

Binary View:

> |||||
> |-|-:|-:|-|
> ||$0100~0000_2$|($64_{10}$)||
> ||$~\downarrow~~~~~\uparrow~~~~~~~~~~~~~~$|(the $1$ moves three places to the left)|
> |$\texttt{<<}~3$|$10~0000~0000_2$|($512_{10}$)

This would yield $512$ if we had a tenth bit into which to shift. But, 
since we only have $8$ bits to consider, the bit containing the $1$ is 
lost, and the returned value is $0$.

---

#### Underflow in Python

We can also lose information when we right shift past the ones place 
(underflow).

Unlike overflow, Python *is* vulnerable to underflow.

```python
x = 4
b = x >> 3
print(f"{x} >> 3 = {b}")
```

Output:

```
4 >> 3 = 0
```

Binary View:

> |||||
> |-|:-|-:|-|
> ||$0000~0100_2$|($4_{10}$)||
> ||$~~~~~~~~~~~\uparrow~~~~~\downarrow~$||(the $1$ moves three places to the right)|
> |$\texttt{>>}~3$|$0000~0000~1_2$|(undefined)|(There is no $0$s place)|

---

#### Underflow in Languages with Static-Size Integer Types

For completeness, let's look at our C example for underflow as well

```c
#include <stdio.h>

int main() {
    unsigned char x, b;

    // Underflow
    x = 4;
    b = x >> 3;
    printf("%d >> 3 = %d\n", x, b);

    return 0;
}
```

Output:

```
4 >> 3 = 0
```

Binary View:

> |||||
> |-|:-|-:|-|
> ||$0000~0100_2$|($4_{10}$)||
> ||$~~~~~~~~~~~\uparrow~~~~~\downarrow~$||(the $1$ moves three places to the right)|
> |$\texttt{>>}~3$|$0000~0000~1_2$|(undefined)|(There is no $0$s place)|

---

### A Simple Example: Iterating Over a Bit-Flag

In some scenarios, it's useful to check all the bits in a bit-flag value.

An easy approach to this is to use a bit-shift to cycle through each bit in
the ones place.

Let's imagine that we have a bit-flag enum for our program settings.

```python
from enum import IntFlag

class Settings(IntFlag):
    DebugMode = 1,
    InteractiveMode = 2,
    RememberSettings = 4,
    Optimize = 8
```

In a scenario where we want to check all of the settings, we can do something
like this:

See [iterate_flags.py](./18_iterate_flags.py)

```python
from random import randint

# -- SNIP --

settings = randint(0, 15)
print(f"With Settings: {settings}, the following bits are set:")
currentValue = 1
while settings > 0:
    if settings & 1: print(f"- {Settings(currentValue).name}")
    settings >>= 1
    currentValue <<= 1
```

Output:

```
With Settings: 15, the following bits are set:
- DebugMode
- InteractiveMode
- RememberSettings
- Optimize
```

Run this a few times to see different results when the random `settings`
value changes.

---
