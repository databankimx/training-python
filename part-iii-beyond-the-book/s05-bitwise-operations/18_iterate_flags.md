## Iterating Over Bit-Flags

Often you need to check every setting in a bit-flag value: which features are
switched on, and which are off. You could test each flag by name, but a bit-flag
value can be read one bit at a time, using bit-shifts.

The code for this lesson is in [18_iterate_flags.py](./18_iterate_flags.py).

---

### The Settings

The program defines its settings as a bit-flag enum. Each setting is one bit,
so the values are powers of two:

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

---

### The Algorithm

To check every bit, we look at the ones place, then shift the whole value one
position to the right so the next bit moves into the ones place. We repeat this
until no set bits are left.

At the same time, we track which setting the ones place represents. It starts
at `1` (`DebugMode`), and doubles each time we shift:

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

---

### Walking Through the Example

Take `settings = 10`, which is `0000 1010` in binary:

| Pass | `settings` (binary) | Ones bit | `currentValue` | Action |
|:-:|:-:|:-:|:-:|-|
| 1 | `0000 1010` | 0 | 1 | Nothing |
| 2 | `0000 0101` | 1 | 2 | Print `InteractiveMode` |
| 3 | `0000 0010` | 0 | 4 | Nothing |
| 4 | `0000 0001` | 1 | 8 | Print `Optimize` |
| 5 | `0000 0000` | - | - | Loop ends |

The printed names match the two bits that are set.

---

### Testing

The script chooses a random settings value between `0` and `15`, so each run
shows a different combination. Two example runs:

```
With Settings: 10, the following bits are set:
- InteractiveMode
- Optimize

With Settings: 7, the following bits are set:
- DebugMode
- InteractiveMode
- RememberSettings
```

The value `7` is `0111` in binary, which sets the first three bits, and the
value `10` sets the second and fourth bits.

Run the script a few times to see other combinations. There are sixteen possible
values, from `0` (no settings) to `15` (all settings).

---

### Where This Is Useful

Checking every flag in a value is common when you need to list the settings
that are switched on, for example when logging a configuration or showing it to
a user. The same loop works for any enum whose values are powers of two.

---
