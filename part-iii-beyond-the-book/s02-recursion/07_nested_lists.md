## Traversing a Nested List

The fact that Python provides robust and easy list functionality is one of the reasons for its popularity.

We're not burdened by the need to stick to a single data type or pre-define
dimensions and lengths, and we can drop in a nested list as an element
wherever we want to.

But all that freedom comes at a cost, which is that it can be harder to 
implement some functionality on lists that don't have strict rules defining
their structures.

One example (for which recursion can provide a good solution) is obtaining the
number of leaves in a tree-like structure of nested lists.

---

### Example Problem

Imagine that we have a list that looks like this:

```python
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
```

We want to count the number of names in the list. In tree terminology, these 
are the leaves (elements containing a value, not another list). Elements that
contain another list are the branches.

We can easily see that there are ten leaves:

* Adam, Alex, Ann, Bob, Barb, Bert, Bea, Bill, Chet, and Cat

However, if we just use the `len()` function, we may be surprised by the
result.

```python
num = len(names)
print(f"The list contains {num} {'leaf' if num == 1 else 'leaves'}")
```

Output:

```
The list contains 5 leaves
```

What's going on?

The `len()` function counts only the top-level elements of the list. It doesn't
look inside the elements that are lists. We can see the top-level elements
themselves by looping over the list:

```python
for index, name in enumerate(names):
    print(index, name)
```

Output:

```
0 Adam
1 ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert']
2 Alex
3 ['Bea', 'Bill']
4 Ann
```

Two of those five elements are lists themselves. `len()` counts them as single
elements, the same as the names, which is why the total is five and not ten.

---

### Using Recursion to Fix the Problem

We can pretty easily create an algorithm to traverse the lists and count only
the leaves at every list level.

```python
def count_leaves(items: list[str | list]) -> int:
    """Recursively count the number of leaves in a (possibly) nested list"""
    print(f"Counting list: {items}")
    count = 0
    for item in items:
        if isinstance(item, list):
            count += count_leaves(item)
        else:
            print(f"Found leaf: {item}")
            count += 1
    return count
```

Here, we have two possible cases for an element when we encounter it

* The element is a leaf (it contains a string value)  
  or
* The element is a branch (it contains a list)

We can think of the leaf as the base case. If we encounter one, we just
increment our count.

For a branch however, we can treat it as though it was a top level list and
process it the same way we're processing the current one. This can recurse to
any number of levels.

I've also included a bit of trace logging so we can see the process through
its recursive calls. That logging is for learning. Real code wouldn't print on
every call.

---

### Running It

We can run our code like this:

```python
num = count_leaves(names)
print(f"The list contains {num} {'leaf' if num == 1 else 'leaves'}")
```

Output:

```
Counting list: ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
Found leaf: Adam
Counting list: ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert']
Found leaf: Bob
Counting list: ['Chet', 'Cat']
Found leaf: Chet
Found leaf: Cat
Found leaf: Barb
Found leaf: Bert
Found leaf: Alex
Counting list: ['Bea', 'Bill']
Found leaf: Bea
Found leaf: Bill
Found leaf: Ann
The list contains 10 leaves
```

---

### What's the Point?

You may be asking why I am showing such an esoteric example and thinking, 
"What's the point? I don't care about leaf-counting on tree structures."

But you're wrong. There is a real-world analog to this that you use every day,
and figuring out a way to traverse its contents is a super-common programming
task that you'll eventually have to solve.

#### Folders!

Your file system is a tree. Files are leaves and directories are branches.
And a solution to crawl a directory as opposed to nested lists differs from
this one only in that you'll add in some OS code to access the file system.

You're welcome. I accept tokens of gratitude in the form of whisky and cheese.

---
