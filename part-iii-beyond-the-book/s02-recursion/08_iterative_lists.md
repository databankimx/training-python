## An Iterative Solution for Counting Nested Lists

I'd be remiss if I didn't demonstrate an iterative version for counting 
leaves in nested lists.

Here, we follow the same process we would have in a recursive algorithm, but
instead of pushing calls onto the recursion stack, we create a stack of lists
(along with the position we were at in each one) and place them there so that
we can come back and iterate through them.

```python
def count_leaves(items: list[str | list]) -> int:
    """Iteratively count the number of leaves in a (possibly) nested list"""
    count = 0
    stack = []
    current_list = items
    i = 0
    while True:
        if i == len(current_list):
            if current_list is items:
                return count
            current_list, i = stack.pop()
            i += 1
            continue
        if isinstance(current_list[i], list):
            stack.append([current_list, i])
            current_list = current_list[i]
            i = 0
        else:
            count += 1
            i += 1

names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat"
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]
num = count_leaves(names)
print(f"The list contains {num} {'leaf' if num == 1 else 'leaves'}")
```

Output:

```
The list contains 10 leaves
```

We got the same answer, but our code is more complicated and consequently 
harder to maintain.

The `is` check is worth a closer look. It asks whether `current_list` is the
same object as the top-level `items` list. Asking whether they're equal would
compare their contents, and that's both slower and less precise.

The iterative version doesn't use recursion at all, so the recursion limit
doesn't apply to it. Its stack is a normal Python list, which grows with the
depth of the nesting, not with the number of leaves.

For the recursive version, the depth limit is the real constraint. It's very
unlikely that a list would have a thousand levels of nesting, so in this case,
the advantage goes to the easy to maintain recursive algorithm, not its
iterative alternative (at least in my opinion).

Try setting up some performance testing with these two algorithms, and see 
which one performs better.

---
