## Aliases and Uniqueness

Sometimes, you'll have a scenario where you want to support multiple
names for a specific variant.

Consider TIFF compression types. People use the names `CCITT T.6` and 
`Group IV` interchangeably when describing the same compression type.

If you were creating an enum for TIFF compressions, you would want to
support both name conventions, but you would not want to have the same
compression type have two different values.

---

### Aliases

In a scenario like that, you can specify multiple names for a single
value.

Let's create a `TiffCompression` enum class:

```python
class TiffCompression(Enum):
    """Defines names for days of the week as bit-flags"""
    NONE = auto()
    LZW = auto()
    ZIP = auto()
    PACKBITS = auto()
    CCITT_T4 = auto()
    CCITT_T6 = auto()
    GROUP_III = CCITT_T4
    GROUP_IV = CCITT_T6
```

We have two aliases added: `GROUP_III` and `GROUP_IV`.

Let's take a look at the effect of that.

```python
print(TiffCompression.CCITT_T6.name, TiffCompression.CCITT_T6.value)
print(TiffCompression.GROUP_IV.name, TiffCompression.GROUP_IV.value)
```

Output:

```
CCITT_T6 6
CCITT_T6 6
```

Notice how the alias is only used to access the variant. But under the
covers, the first item assigned that value is what is returned.

---

### The `__members__` Attribute

When you create an enum, it exposes a special attribute `__members__`
that contains all of the variants (including aliases) and their values.

```python
print(TiffCompression.__members__)
```

Output:

```
{
    'NONE': <TiffCompression.NONE: 1>,
    'LZW': <TiffCompression.LZW: 2>,
    'ZIP': <TiffCompression.ZIP: 3>,
    'PACKBITS': <TiffCompression.PACKBITS: 4>,
    'CCITT_T4': <TiffCompression.CCITT_T4: 5>,
    'CCITT_T6': <TiffCompression.CCITT_T6: 6>,
    'GROUP_III': <TiffCompression.CCITT_T4: 5>,
    'GROUP_IV': <TiffCompression.CCITT_T6: 6>
}
```

> Note: It doesn't pretty-print like the output above. I added 
> formatting for ease of reading.

---

### Enforcing Uniqueness

Other times, you may want the opposite. You need to be sure that there
will never be two variant names pointing to the same value.

For this, we can implement the `@unique` decorator.

If an enum is defined with the `@unique` decorator, it will raise a
`ValueError` if more than one variant is declared with the same value

```python
from enum import Enum, unique

@unique
class NoRepeats(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    TRES = 3
```

Output:

```
Traceback (most recent call last):
  File "...\05_alias_unique.py", line 14, in <module>
    @unique
     ^^^^^^
  File "...\enum.py", line 1586, in unique
    raise ValueError('duplicate values found in %r: %s' %)
ValueError: duplicate values found in <enum 'NoRepeats'>: TRES -> THREE
```

---
