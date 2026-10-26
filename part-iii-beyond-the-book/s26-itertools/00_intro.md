## The `itertools` Module

The `itertools` module is a collection of tools for working with iterators:
values that are produced one at a time, as they are needed. Most of its functions
return an iterator rather than a list, so they use very little memory, even when
the sequence they describe is very long or infinite.

Each lesson in this chapter covers one group of functions:

* [Infinite Iterators](./01_infinite_iterators.md): `count()`, `cycle()`, and `repeat()`
* [Joining and Slicing](./02_chain_and_islice.md): `chain()` and `islice()`
* [Running Totals](./03_accumulate.md): `accumulate()`
* [Combinations and Permutations](./04_combinatorics.md): `combinations()`, `permutations()`, and `product()`
* [Grouping](./05_groupby.md): `groupby()`, and why the data must be sorted first
* [Filtering](./06_filtering.md): `takewhile()`, `dropwhile()`, `filterfalse()`, and `compress()`
* [Pairing and Mapping](./07_zip_longest_and_starmap.md): `zip_longest()` and `starmap()`

Each function returns an iterator, so the examples wrap it in `list()` to see the
values. When you loop over the iterator directly, you don't need the `list()`.

---

### Importing the Module

Import the functions you need by name:

```python
from itertools import count, islice
```

Many of these functions can run forever. They are usually paired with `islice()`
or `takewhile()` so that they stop. Each lesson shows how.

---
