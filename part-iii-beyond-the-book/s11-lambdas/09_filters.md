## Key Functions and Filters

Functions like sort(), sorted(), min(), and max() accept keys, for which 
a lambda is often an optimal choice.

---

### List Sorting Key

Let's imagine that we have a list containing mixed letters and numbers
like this:

```python
ids = ["id1", "id2", "id30", "id3", "id22", "id100"]
```

---

#### Sorting without a Key

If we try to sort the list ...

```python
print(sorted(ids))
```

... the items are sorted lexically (because they contain letters) ...

Output:

```
['id1', 'id100', 'id2', 'id22', 'id3', 'id30']
```

Given that every item starts with `id` and then a numerical value, this is
almost certainly not what we want. We'd prefer the items be sorted by the 
numeric part.

---

#### Improving the Sort with a Lambda as a Key

However, we can create a lambda function that strips off the `id` part of 
each term and converts it to an integer for sorting.

```python
print(sorted(ids, key=lambda x: int(x[2:])))
```

The result is that the elements are sorted numerically ...

Output:

```
['id1', 'id2', 'id3', 'id22', 'id30', 'id100']
```

Which seems like a much more appropriate result.

---

### Formatting Items Using `map()`

When mapping items to a list, it's often advantageous to perform some 
formatting while creating the list.

Say we have this tuple, and we want to create a list where the first
letter of each element is capitalized.

```python
tup = ("cat", "dog", "turtle")
```

We could, of course, use a list comprehension.

```python
print([x.capitalize() for x in tup])
```

Alternately, we could use the `map()` function and apply the 
capitalization using a lambda.

```python
print(list(map(lambda x: x.capitalize(), tup)))
```

In either case we would get this...

Output:

```
['Cat', 'Dog', 'Turtle']
```

Because this is a very simple example, the lambda method is arguably more
complicated than the comprehension, but there will be cases where passing
a lambda to `map()` will be preferable.

---

### Filtering with a Lambda

Frequently, we will want to filter a list or range and only include parts
of the collection in a result.

Let's imagine we want a list containing the even numbers from 1 to 10.

There are a few approaches to this.

We could invoke the step value in the `range()` function:

```python
print(list(range(2, 11, 2)))
```

But that assumes that we know the start and end values. Specifically, it
requires that we know whether the first number in the range is even.

Or we could use a list comprehension:

```python
print([x for x in range(1, 11) if not x % 2])
```

Or, we could use a lambda with the `filter()` function.

```python
print(list(filter(lambda x: not x % 2, range(1, 11))))
```

Or better yet, we could stash the lambda in a variable so that we could
use it for later filtering of even numbers

```python
even = lambda x: not x % 2
print(list(filter(even, range(1, 11))))
```

All of these have the same results...

Output:

```
[2, 4, 6, 8, 10]
```

But it's reasonable to conclude that the second lambda method provides
the greatest flexibility.

Will that always be the case?

No. As a developer, you should decide in a given situation which approach
is best suited.

But now, you have the lambda option in your tool belt.

---
