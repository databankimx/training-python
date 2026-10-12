## Collection Types in Python

Python includes several collection types, each with different rules defining
how they behave.

The rules are:

* **Ordered** collections' members can be accessed by index (address).
* **Mutable** collections' members can be modified after they are initialized.
* Collections with the **Add/Remove** behavior permit items to be added to or 
  removed from the collection.
* Collections with the **Duplicates** behavior can have multiple instances of
  the same collection value.<br>
  Note: Dictionaries technically *can* have duplicate values, but they *cannot*
  contain duplicate keys.

---

The table below lists how the  behaviors of collection types apply to the main 
Python collection types.

|Type|Syntax|Ordered|Mutable|Add/Remove|Duplicates|
|-|-|:-:|:-:|:-:|:-:|
|List|`[1, 2, 3]`|X|X|X|X|
|Tuple|`(1, 2, 3)`|X|||X|
|Set|`{1, 2, 3}`|||X||
|Dictionary|`{'a': 1, 'b': 2, 'c': 3}`|X|X|X||
|||||||

This brief code sample illustrates each of these behaviors using a list:

```python
my_list = [1, 2, 3]

print(my_list)
print(my_list[1]) # Ordered members accessed by index
my_list[1] = 4    # Mutable collections' members can be modified
print(my_list)
my_list.append(3) # Add an item to a collection
print(my_list)    # Note: We added a duplicate value
```

Output:

```
[1, 2, 3]
2
[1, 4, 3]
[1, 4, 3, 3]
```

---
