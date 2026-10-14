## An Iterative Solution for Counting Nested Lists

I'd be remiss if I didn't demonstrate an iterative version for counting 
leaves in nested lists.

Here, we follow the same process we would have in a recursive algorithm, but
instead of pushing calls onto the recursion stack, we create a stack of lists
and place each list there so that we can come back and iterate through it.

```python
def count_leaves(items: list[str | list]) -> int:
    """Iteratively count the number of leaves in a (possibly) nested list"""
    count = 0
    stack = []
    current_list = items
    i = 0
    while True:
        if i == len(current_list):
            if current_list == items:
                return count
            else:
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

names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
num = count_leaves(names)
print(f"The list contains {num} {'leaf' if num == 1 else 'leaves'}")
```

Output:

```
The list contains 10 leaves
```

We got the same answer, but our code is more complicated and consequently 
harder to maintain.

We do still have to worry about the recursion stack maximum, but unlike the
prior examples, that depth doesn't relate to the number of leaves we have to
count but rather to the maximum depth of nesting that occurs in the list.

It's very unlikely that a list would have a thousand levels of nesting, so in
this case, the advantage goes to the easy to maintain recursive algorithm, not
its iterative alternative (at least in my opinion).

Try setting up some performance testing with these two algorithms, and see 
which one performs better.

---
