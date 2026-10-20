## Be Careful with Loops

### Beware!

It's tempting to modify a list while iterating across it, but that will break 
things...

---

Consider this example where we're trying to `pop()` each item as we iterate:

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

You might be surprised that the output is:

```
1
3
5
[2, 4]
```

</details>
<br>

---

If you predicted that all five numbers would be printed and that the list 
would be empty after the loop, here's why that didn't happen:

* On the first iteration, we pop `numbers[0]`, which re-indexes the remainder 
  of the list `[2, 3, 4, 5]`
* But the Python iterator doesn't know about the change (it was created when 
  we started the loop)
* So it just moves on to `numbers[1]`, which is now the value 3.
  Then it pops `numbers[1]` leaving `[2, 4, 5]`
* Finally the third iteration moves to `numbers[2]`, which is now the value 5
* After the three iterations, the loop encounters the end of the list and
  terminates, but the list still contains the values that got skipped ->
  `[2, 4]`

The process (step-by-step) looks like this:

|Iteration|List Before `pop`|Index|Value|List After `pop`|
|:-:|-|:-:|:-:|-|
|1|`[1, 2, 3, 4, 5]`|0|1|`[2, 3, 4, 5]`|
|2|`[2, 3, 4, 5]`|1|3|`[2, 4, 5]`|
|3|`[2, 4, 5]`|2|5|`[2, 4]`|

No error is thrown, because the iterator halts upon reaching the end of the 
list. We just get an unexpected result

> **Moral**: NEVER modify the collection you are looping over with `for`!

**Foreshadowing**: We'll see a way to empty the list in a loop without 
problems in Lesson 07.04 (but it'll be a different kind of loop).

---
