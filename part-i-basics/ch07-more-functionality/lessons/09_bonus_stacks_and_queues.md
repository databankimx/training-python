## Bonus : Stacks and Queues

When processing items from an ordered collection like a list, we need to think 
about which end gets processed first.

Using while loops, we can simulate the behavior of two different list-like 
data structures: stacks and queues.

---

### Stacks

A stack uses last-in, first-out (LIFO) order.

You can imagine this visually. If you stack several things on top of each 
other, at any time you can only remove the top one (the last one you added).

Note: I am specifying index -1 in the `pop()` call. This is redundant, because
`pop()` removes the last item in the list bu default. I have left this in 
place in order for the code to explicitly show the reader that it is behaving
as a stack.

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

A queue uses first-in, first-out (FIFO) order

This is a lot like when people are waiting in line (first-come, first-served).

Note: Now we are calling `pop(0)` to remove the first item from the list.

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
> This lesson is not a complete exploration of the stack and queue data 
> structures, which require additional functionality not covered here.
>
> This is just a review of how we can control retrieval order in the way that 
> those structures would.

---
