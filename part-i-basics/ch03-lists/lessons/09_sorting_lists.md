## Sorting and Reversing Lists

Python provides several functions for sorting and reversing lists.

The main decision for choosing between options that perform the same task
(sort or reverse) is whether or not to affect the original list.

|Function|Effect|
|-|-|
|`list.sort()`|Sorts the list in place (permanent)|
|`sorted(list)`|Sorts and returns a copy of the list|
|`list.reverse()`|Reverses the list in place (permanent)|
|`reversed(list)`|Reverses and returns an iterator for of the list|

---

### Sorting a List In-Place

The `list.sort()` method sorts the list itself. The modification is permanent.

#### You can sort a list numerically

```python
my_list = [13, 7, 28, 3, 2, 17]
print(my_list)
my_list.sort()
print(my_list)
```

Output:

```
[13, 7, 28, 3, 2, 17]
[2, 3, 7, 13, 17, 28]
```

---

#### Or you can sort a list alphabetically

```python
my_list = ["grape", "banana", "fig", "apple", "date"]
print(my_list)
my_list.sort()
print(my_list)
```

Output:

```
['grape', 'banana', 'fig', 'apple', 'date']
['apple', 'banana', 'date', 'fig', 'grape']
```

---

#### You **cannot** sort a mixed-type list, because types can only compare against themselves

```python
my_list = [5, "banana", "fig", 1, "date"]
my_list.sort() # TypeError occurs here
print(my_list)
```

Output:

```
TypeError: '<' not supported between instances of 'str' and 'int'
```

---

### Sorting a Copy of a List

Sometimes you need the list data sorted, but you don't want to modify the
original list. The `sorted(list)` function accomplishes this by creating a copy
of the list and sorting that.

```python
my_list = [13, 7, 28, 3, 2, 17]
my_sorted_list = sorted(my_list)
print(my_sorted_list) # This copy is sorted
print(my_list)        # The original list is unchanged
```

Output:

```
[2, 3, 7, 13, 17, 28]
[13, 7, 28, 3, 2, 17]
```

---

### Optional Parameters

Both the `list.sort()` and `sorted(list)` functions accept two optional
arguments:

|Argument|Effect|
|-|-|
|`reverse`|If `True`, sort in descending order|
|`key`|Accepts a function to define how list items are compared for sorting|

---

#### Using `reverse=True` sorts in descending order

```python
my_list = [13, 7, 28, 3, 2, 17]
my_sorted_list = sorted(my_list, reverse=True)
print(my_sorted_list)
print(my_list)             # The original list is unchanged at this point
my_list.sort(reverse=True) # After this, the original list is sorted
print(my_list)
```

Output:

```
[28, 17, 13, 7, 3, 2]
[13, 7, 28, 3, 2, 17]
[28, 17, 13, 7, 3, 2]
```

#### We'll cover the use of the `key` argument in a later lesson

---

### Reversing a List In-Place

The `list.reverse()` function reverses the order of a list without sorting
the values. This modifies the  list in-place, so the effect is permanent.

```python
my_list = [13, 7, 28, 3, 2, 17]
print(my_list)
my_list.reverse()
print(my_list)
```

Output:

```
[13, 7, 28, 3, 2, 17]
[17, 2, 3, 28, 7, 13]
```

---

### Reversing a Copy of a List

Just like sorting, Python provides the `reversed(list)` function to reverse a
copy of the list rather than modifying the original.

Note: You have to convert the iterator returned by the `reversed()` function
to a list before printing.

```python
my_list = [13, 7, 28, 3, 2, 17]
my_reversed_list = reversed(my_list)
print(list(my_reversed_list)) # This copy is reversed
print(my_list)                # The original list is unchanged
```

Output:

```
[17, 2, 3, 28, 7, 13]
[13, 7, 28, 3, 2, 17]
```

---

### Remembering Which is Which

> To remember which functions make a copy instead of modifying the original
> list, I use a mnemonic.
>
> I remind myself that '**d**' stands for **duplicate** ...
> 
> So the functions that  end in the letter 'd' [`sorted()` and `reversed()`] 
> are the ones that create a duplicate copy of the list instead of modifying 
> the original.

---
