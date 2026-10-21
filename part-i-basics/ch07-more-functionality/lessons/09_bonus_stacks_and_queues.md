## Bonus: Stacks and Queues

When you process the items in an ordered collection like a list, you need to decide which end
gets processed first.

Using `while` loops, we can simulate the behavior of two different list-like data structures: stacks
and queues.

---

### Stacks

A stack uses last-in, first-out (LIFO) order.

Picture a pile of plates. You can only take off the top one, which is the last one you added.

Note: I'm passing index `-1` to `pop()`. That's redundant, because `pop()` removes the last item in
the list by default. I've left it in so the code shows the reader that it's behaving as a stack.

```python
my_stack = [1, 2, 3, 4, 5]
print(f"Stack: {my_stack}")
while my_stack:
    print(my_stack.pop(-1))
```

Output:

```
Stack: [1, 2, 3, 4, 5]
5
4
3
2
1
```

---

### Queues

A queue uses first-in, first-out (FIFO) order.

This is like people waiting in line: first come, first served.

Note: Now we call `pop(0)` to remove the first item from the list. Keep in mind that `pop(0)` shifts
every remaining item, which gets slow on long lists. We covered that cost in lesson 3.7.

```python
my_queue = [1, 2, 3, 4, 5]
print(f"\nQueue: {my_queue}")
while my_queue:
    print(my_queue.pop(0))
```

Output:

```
Queue: [1, 2, 3, 4, 5]
1
2
3
4
5
```

---

> Note:
>
> This lesson isn't a complete exploration of stacks and queues. Those structures need more
> functionality than we cover here.
>
> It's just a review of how you can control the order items come out, the way those structures do.

---

