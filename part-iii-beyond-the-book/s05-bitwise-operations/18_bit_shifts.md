## Using Bit-Shifts (`<<` and `>>`)

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

This holds for non-negative values. For negative values, `>>` rounds toward
negative infinity, so `-1 >> 1` is `-1`.

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
which is 8 bits on virtually all systems.

See [bit_shift_overflow.c](./18_bit_shift_overflow.c)

```c
#include <stdio.h>

int main() {
    unsigned char x, b;

    // Overflow
    x = 64;
    b = x << 3;
    printf("%d << 3 = %d\n", x, b);

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

Unlike overflow, Python still loses bits when a right shift moves past the ones
place.

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
> |$\texttt{>>}~3$|$0000~0000~1_2$|($0_{10}$)|(the $1$ falls off the end)|

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
> |$\texttt{>>}~3$|$0000~0000~1_2$|($0_{10}$)|(the $1$ falls off the end)|

---

### A Simple Example: Iterating Over Bit-Flags

In some scenarios, it's useful to check every setting in a bit-flag value: which
features are switched on, and which are off. You could test each flag by name,
but a bit-flag value can be read one bit at a time, using bit-shifts.

The program defines its settings as a bit-flag enum. Each setting is one bit, so
the values are powers of two:

```python
from enum import IntFlag

class Settings(IntFlag):
    DebugMode = 1
    InteractiveMode = 2
    RememberSettings = 4
    Optimize = 8
```

A stored settings value is the sum of the settings that are switched on. For
example, a value of `10` (`0000 1010`) has the `InteractiveMode` bit and the
`Optimize` bit set.

#### The Algorithm

To check every bit, we look at the ones place, then shift the whole value one
position to the right so the next bit moves into the ones place. We repeat this
until no set bits are left.

At the same time, we track which setting the ones place represents. It starts at
`1` (`DebugMode`), and doubles each time we shift:

```python
settings = 10
currentValue = 1
while settings > 0:
    if settings & 1:
        print(f"- {Settings(currentValue).name}")
    settings >>= 1
    currentValue <<= 1
```

Each pass does three things:

* `settings & 1` checks the ones-place bit. It is `1` only if that setting is on.
* `settings >>= 1` shifts the value right, so the next bit is in the ones place.
* `currentValue <<= 1` doubles the value, so it matches the next setting's bit.

The loop ends when `settings` reaches `0`, which means no set bits remain.

#### Walking Through the Example

Take `settings = 10`, which is `0000 1010` in binary:

| Pass | `settings` (binary) | Ones bit | `currentValue` | Action |
|:-:|:-:|:-:|:-:|-|
| 1 | `0000 1010` | 0 | 1 | Nothing |
| 2 | `0000 0101` | 1 | 2 | Print `InteractiveMode` |
| 3 | `0000 0010` | 0 | 4 | Nothing |
| 4 | `0000 0001` | 1 | 8 | Print `Optimize` |
| 5 | `0000 0000` | - | - | Loop ends |

The printed names match the two bits that are set.

#### Testing

The code file runs the loop on `settings = 10`, and then on a random value between
`0` and `15`, so you can see different combinations. Example output:

```
With Settings: 10, the following bits are set:
- InteractiveMode
- Optimize

With Settings: 7, the following bits are set:
- DebugMode
- InteractiveMode
- RememberSettings
```

The value `7` is `0111` in binary, which sets the first three bits. Run the script a
few times to see other combinations. There are sixteen possible values, from `0`
(no settings) to `15` (all settings).

Checking every flag in a value is common when you need to list the settings that
are switched on, for example when logging a configuration or showing it to a user.

---
