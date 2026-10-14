## Bitwise AND - Real-World Example: Bit-Flags

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

One example where we commonly use a bitwise AND is when checking a 
bit-flag.

### Scenario

You are employed by a large company called MacroWare. One of the company's
flagship software products is an office product suite that contains 
several different programs.

For a number of reasons, including simplifying delivery by packaging only 
one installer and providing an easy path to post-purchase upsells, the 
installation package installs all of the programs, regardless which have 
been purchased by the user.

You are tasked with creating a mechanism that allows the software to check 
the licensed state of each of the programs before allowing each program to 
run.

---

### An Obvious Approach

You might intuitively default to using boolean values to enable/disable 
each feature:

```python
class ProductLicenses:
    def __init__(self):
        self.word_processing: bool = False
        self.spreadsheets: bool  = False
        self.presentations: bool  = False
        self.email_client: bool  = False
        self.notebook: bool  = False
        self.collaboration: bool  = False
        self.project_management: bool  = False
        self.publishing: bool  = False
```

---

#### Usage

Then when accessing a feature, you could check the feature's boolean value 
to determine whether it launches.

```python
licenses = ProductLicenses()

# -- SNIP --

if not licenses.word_processing:
    raise Exception("Not licensed for Word Processing!")

# -- SNIP --
```

---

### What's Wrong with This Approach

This approach works, but it's not very mindful of memory usage, since each 
of those boolean values consumes one byte in memory.

This might not matter given the large amount of memory in current 
computers, but if you're storing active license information in a database, 
it's using eight columns (at a minimum of one byte apiece) for this 
information.

Supposing MacroWare sells a billion copies, that's consuming about $8$GB 
of disk space.

---

### An Alternative Approach : Bit-Flags

Suppose, instead of using one byte per product, instead, you used one bit. 
That would reduce the size of the licensing data eightfold, and the 
database licensing data would be only $1$GB.

The idea sounds great, but how would we do it.

One approach would be to define each product as a binary bit position 
value in an integer enum.

```python
from enum import IntFlag

class ProductLicenses(IntFlag):
    unlicensed         = 0,
    word_processing    = 1,
    spreadsheets       = 2,
    presentations      = 4,
    email_client       = 8,
    notebook           = 16,
    collaboration      = 32,
    project_management = 64,
    publishing         = 128
```

---

You can even use binary literals to make the bit position based choice 
more obvious.

```python
from enum import IntFlag

class ProductLicenses(IntFlag):
    unlicensed         = 0b0000_0000,
    word_processing    = 0b0000_0001,
    spreadsheets       = 0b0000_0010,
    presentations      = 0b0000_0100,
    email_client       = 0b0000_1000,
    notebook           = 0b0001_0000,
    collaboration      = 0b0010_0000,
    project_management = 0b0100_0000,
    publishing         = 0b1000_0000
```

---

#### Usage

Then, when you need to check if a product is licensed, you can use bitwise 
AND (`&`) to validate the value of a specific bit position.

```python
# -- SNIP --

licenses = some_integer_value
wp = ProductLicenses.word_processing

if licenses & wp != wp
    raise Exception("Not licensed for Word Processing!")

# -- SNIP --
```

---

### Explanation

How does that work?

Well, you already know that each value in your enum only has a single bit 
set to $1$.

Because of that, you can be certain that regardless of the value you 
compare to it, that bit is the only one for which a $1$ could possibly be 
returned by a bitwise AND operation.

So, if the compared value does not have that bit set to $1$, the AND 
operation will return $0$, and if it does, it will return the value of 
that bit position.

Let's imagine an example where the stored value for licenses is $11$, and 
we're checking for the bit that represents word processing ($1$).

The bitwise comparison looks like this:

> |||
> |-:|:-|
> |$0000~1011$|(licenses)|
> |$\underline{\&~0000~0001}$|(word processing enum value)|
> |$0000~0001$||

Only the rightmost bit (value 1) has ones in both values, so the returned 
value is $1$ (which is the same as the value we compared from the enum), 
so we know that word processing is licensed.

If the value in licenses is $10$ instead, we'd get a result of $0$:

> |||
> |-:|:-|
> |$0000~1010$|(licenses)|
> |$\underline{\&~0000~0001}$|(word processing enum value)|
> |$0000~0000$||

So we know that word processing is not licensed.

---

### The Full Example

See [bit_flags.py](./12_bit_flags.py)

```python
from enum import IntFlag

class ProductLicenses(IntFlag):
    unlicensed         = 0b0000_0000,
    word_processing    = 0b0000_0001,
    spreadsheets       = 0b0000_0010,
    presentations      = 0b0000_0100,
    email_client       = 0b0000_1000,
    notebook           = 0b0001_0000,
    collaboration      = 0b0010_0000,
    project_management = 0b0100_0000,
    publishing         = 0b1000_0000

def main() -> None:
    licenses = 11
    for l in ProductLicenses:
        if not licenses & l: continue
        print(l.name)

if __name__ == "__main__":
    main()
```

Output:

```
word_processing
spreadsheets
email_client
```

Try varying the value of `licenses` and see what results you get.

---

### Putting it to Use

This technique can work with any collection of settings where the values 
are enumerated as powers of two, and the bit-size of the integer in which 
you store the values determines the number of values you can store.

---
