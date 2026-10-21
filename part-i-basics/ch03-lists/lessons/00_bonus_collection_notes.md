## Collection Types in Python

Python has several collection types. Each one holds a group of values, but they
don't all behave the same way. Some keep things in order, some let you change
them, and some won't let you store the same value twice.

This lesson is a preview. You'll get full coverage of lists in this chapter, and
tuples, sets, and dictionaries come later in the book. For now, the goal is to
see how they differ.

The behaviors that matter are:

* **Ordered** collections let you reach a member by its position (its index).
* **Mutable** collections let you change their members after they're created.
* Collections with **Add/Remove** let you add or remove items.
* Collections with **Duplicates** can hold the same value more than once.

---

Here's how the main collection types stack up:

|Type|Syntax|Ordered|Mutable|Add/Remove|Duplicates|
|-|-|:-:|:-:|:-:|:-:|
|List|`[1, 2, 3]`|X|X|X|X|
|Tuple|`(1, 2, 3)`|X|||X|
|Set|`{1, 2, 3}`|||X||
|Dictionary|`{'a': 1, 'b': 2, 'c': 3}`|X|X|X||

> Notes:
>
> * Dictionaries can have duplicate values, but they can't have duplicate keys.
> * Dictionaries before Python 3.7 didn't guarantee insertion order, so older
>   versions don't have the **Ordered** behavior.

---

Here's a short sample that shows these behaviors, using a list:

```python
my_list = [1, 2, 3]

print(my_list)
print(my_list[1]) # Ordered members can be reached by position
my_list[1] = 4    # Mutable collections let you change their members
print(my_list)
my_list.append(3) # Add an item to a collection
print(my_list)    # Note: we added a duplicate value
```

Output:

```
[1, 2, 3]
2
[1, 4, 3]
[1, 4, 3, 3]
```

---

The `.py` file shows the other types as well. One thing to watch: a set doesn't
have an order. The sample prints its items in order, but that's luck, not a rule,
so don't count on a set printing the same way twice.

