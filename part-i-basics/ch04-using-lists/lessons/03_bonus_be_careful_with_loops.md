## Be Careful with Loops

### Never Modify a Collection You Are Iterating Over

It's tempting to modify a list while iterating across it, but it will break
things in ways that don't always produce an error - just a wrong result.

---

Consider this example where we try to `pop()` each item as we iterate:

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    n = numbers.index(number)
    print(numbers.pop(n))
print(numbers)
```

Try to predict what will happen before reading the output.

<details>
<summary>Output</summary>

```
1
3
5
[2, 4]
```

</details>
<br>

---

If you predicted all five numbers would print and the list would be empty,
here is why that didn't happen:

- On the first iteration, `numbers[0]` (value `1`) is popped. The list becomes `[2, 3, 4, 5]`.
- The Python iterator doesn't know about the change - it was created at the start of the loop.
- So it moves to `numbers[1]`, which is now `3`. That gets popped, leaving `[2, 4, 5]`.
- Third iteration moves to `numbers[2]`, which is now `5`. That gets popped, leaving `[2, 4]`.
- The iterator reaches the end of the list and stops. No error is raised.

| Iteration | List before `pop` | Index | Value | List after `pop` |
|:-:|-|:-:|:-:|-|
| 1 | `[1, 2, 3, 4, 5]` | 0 | 1 | `[2, 3, 4, 5]` |
| 2 | `[2, 3, 4, 5]` | 1 | 3 | `[2, 4, 5]` |
| 3 | `[2, 4, 5]` | 2 | 5 | `[2, 4]` |

No error is thrown - you just get an unexpected result.

> **Moral: NEVER modify the collection you are looping over with `for`.**

**Foreshadowing:** We will see a correct way to empty a list in a loop in
lesson 07.04, using a `while` loop instead.

---
