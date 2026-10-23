## Be Careful with Loops

### Beware!

It's tempting to change a list while you loop over it. Don't. It looks harmless, but it will quietly break your program.

---

Here's an example. The goal is to `pop()` every item as we go:

```python
numbers = [1, 2, 3, 4, 5]

# Try to predict what will happen in this loop
for number in numbers:
    n = numbers.index(number)
    print(numbers.pop(n))
print(numbers)
```

### Surprise!

<details>
<summary>Open after you make your prediction...</summary>
<br>

The output is:

```
1
3
5
[2, 4]
```

</details>
<br>

---

If you predicted that all five numbers would print and the list would end up empty,
you're not alone. That's what most people expect. Here's what really happens:

* On the first iteration, we pop `numbers[0]`, which leaves `[2, 3, 4, 5]`. The
  remaining items shift left to fill the gap.
* The loop doesn't know the list changed. Its internal position moves on to the next
  index, `1`, which now holds `3`. We pop that, leaving `[2, 4, 5]`.
* The third iteration moves to index `2`, which now holds `5`. We pop that too.
* After three iterations, the loop reaches the end of the list and stops. But the
  list still holds the items that got skipped, so it ends as `[2, 4]`.

Here it is, step by step:

|Iteration|List Before `pop`|Index|Value|List After `pop`|
|:-:|-|:-:|:-:|-|
|1|`[1, 2, 3, 4, 5]`|0|1|`[2, 3, 4, 5]`|
|2|`[2, 3, 4, 5]`|1|3|`[2, 4, 5]`|
|3|`[2, 4, 5]`|2|5|`[2, 4]`|

No error appears, because the loop stops cleanly at the end. The result is just wrong.

> **A note on `index()`:** the code finds each position with `numbers.index(number)`,
> which returns the *first* place a value appears. That's fine here, because every
> number is unique. If the list had duplicates, `index()` would point at the wrong
> item. Keep that in mind before you copy this pattern.

> **Moral:** Never change the collection you're looping over with `for`.

**Foreshadowing:** Chapter 7 covers `while` loops, which give you a safe way to keep
removing items until a list is empty. They work differently, and they don't have this
problem.

---
