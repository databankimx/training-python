## Underscores as Number Grouping Symbols

Long numbers are hard to read. Try to tell whether `1000000000` is a billion or a
hundred million at a glance. Nobody can, and that's the problem.

Python 3.6 and later let you add underscores (`_`) to a number. The interpreter
ignores them, so they're purely for the human reading the code.

Underscores go between two digits, one at a time. You can't start or end a number
with one, and you can't put two in a row. Here are a few valid ways to write
`1000`:

```
1_000
10_00
1_0_0_0
```

Python rejects the invalid ones, such as `1__000` (two underscores in a row) or
`_1000` (a leading underscore). Those give you a `SyntaxError`.

In practice, you'll almost always group by thousands, the same way a comma would
in ordinary writing. Since Python integers have no maximum size, grouping like
this is a big help when the numbers get long.

---

Here's the difference in practice. This code:

```python
thousand = 1_000
million  = 1_000_000
billion  = 1_000_000_000
trillion = 1_000_000_000_000
# ...
```

is much easier to read than this:

```python
thousand = 1000
million  = 1000000
billion  = 1000000000
trillion = 1000000000000
# ...
```

Same values, far less squinting.

---

