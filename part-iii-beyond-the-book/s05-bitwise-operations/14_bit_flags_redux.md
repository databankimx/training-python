## Bitwise OR - Real-World Example: Bit-Flags (Redux)

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

Sometimes it's useful to have a particular value represented by more than 
one bit in a bit-flag. Bitwise OR can be used to simplify this.

---

### Scenario

Back at MacroWare, your boss is pleased with how you chose to implement
license checks for the component software.

You're now asked to handle checks for packages that contain several of the
separate programs as a single license type.

Specifically:

* Personal:
    * WordProcessing
    * EmailClient
* Work:
    * WordProcessing
    * EmailClient
    * Spreadsheets
    * Presentations
    * Notebook
    * Collaboration
* Ultra Deluxe:
    * All Programs

---

### An Obvious Approach

Intuition might suggest that the easy approach is to switch to using a 
larger integer type and add values for each package

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
    publishing         = 128,
    personal           = 256,
    work               = 512,
    ultra_deluxe       = 1024
```

Then, when checking whether a specific program should run, you could check for multiple conditions.

```python
# -- SNIP --

licenses = 512

wp = (licenses & Products.word_processing == Products.word_processing
   or licenses & Products.personal == Products.personal
   or licenses & Products.work == Products.work
   or licenses & Products.ultra_deluxe == Products.ultra_deluxe)

if not wp:
    raise Exception("Not licensed for word processing!")

print("Ready for word processing...")
```

Output:

```
Ready for word processing...
```

---

### Obvious Is Not Necessarily Good

This implementation has a number of inefficiencies.

* The values for the packages are not coupled to the products they include
* The logic is unnecessarily overcomplicated
* Future changes in the included products in a given package require 
  tracking down the locations where a given product is checked
    * So updates have to be made in multiple locations in your code

---

### An Alternative Approach : Combined Bit-Flags

Using a bitwise OR permits combining multiple bit values, since it returns 
the union of the bit values rather than the intersection.

For example, you know that the Personal license includes Word Processing 
and an Email Client. In your existing bit-flag enumeration, you have 
values for those.

|||
|-|-:|
|`word_processing`|$=1_{10}=0000~0001_2$|
|`email_client`|$=8_{10}=0000~1000_2$|

If you perform a bitwise OR on those values...

> |||
> |-:|-:|
> |$0000~0001_2$|$(1_{10})$|
> |$\underline{~\|~~0000~1000_2}$|$(8_{10})$|
> |$0000~1001_2$|$(9_{10})$|

... you end up with the value 9, where both bits are set.

This is sometimes called a bit-mask.

---

You might just take that knowledge and set the following:

```python
from enum import IntFlag

class ProductLicenses(IntFlag):    
    # -- SNIP --

    personal = 9,
```

---

Or, you can use the bitwise OR in the enumeration to make it clear what 
we're doing and easy to modify in the future:

```python
from enum import IntFlag

class ProductLicenses(IntFlag):    
    # -- SNIP --

    # Note: The enum values are stored as tuples, so we have to
    #       get the `value[0]` element for the integer value
    #       when accessing them inside the enum
    personal = word_processing[0] | email_client[0],
```

---

### Getting More from What You Already Have

And you can leverage the work already done when setting the values for the
other packages.

Since the Work package includes Word Processing and the Email Client in
addition to other programs, and the Ultra Deluxe package contains 
everything, you can implement them like this:

```python
from enum import IntFlag

class ProductLicenses(IntFlag):    
    # -- SNIP --

    personal = word_processing[0] | email_client[0],
    work = personal[0] | spreadsheets[0] | presentations[0] \
         | notebook[0] | collaboration[0],
    ultra_deluxe = work[0] | project_management[0] | publishing[0]
```

---

### Putting it Together

So your final enumeration looks like this:

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
    publishing         = 0b1000_0000,
    personal = word_processing[0] | email_client[0],
    work = personal[0] | spreadsheets[0] | presentations[0] \
         | notebook[0] | collaboration[0],
    ultra_deluxe = work[0] | project_management[0] | publishing[0]
```

And now, you can continue using your original, simple licensing check,
regardless which (if any) package the user owns.

```python
# -- SNIP --

licenses = ProductLicenses.work
wp = licenses & ProductLicenses.word_processing
if not wp:
    raise Exception("Not licensed for word processing!")
print("Ready for word processing...")
```

Output:

```
Ready for word processing...
```

---

### We Compared a Bit_mask Against a Bit-Flag

This works because now, you have the Word Processing bit set in each 
package that includes it.

If we consider the Work package, its value is 0011 1111. Even though it has
several bits set, if you perform a bitwise AND against Word Processing...

> ||
> |-:|
> |$0011~1111_2$|
> |$\underline{\&~~0000~0001_2}$|
> |$0000~0001_2$|

It still results in the same value ($1$) as when you didn't define 
packages, so you don't need to make changes in your license checks if the 
packages are modified. You only need to change the enum.

---

### The Full Example

See [bit_flags_redux.py](./14_bit_flags_redux.py)

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
    publishing         = 0b1000_0000,
    personal = word_processing[0] | email_client[0],
    work = personal[0] | spreadsheets[0] | presentations[0] | \
           notebook[0] | collaboration[0],
    ultra_deluxe = work[0] | project_management[0] | publishing[0]

def main() -> None:
    licenses = ProductLicenses.work
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
presentations
email_client
notebook
collaboration
```

Try varying which package you use in `licenses` and see what results you 
get.

---
