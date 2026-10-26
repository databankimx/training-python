## Sorting and Reversing Lists

Python gives you several ways to sort and reverse a list. Most of them come in pairs:
one changes the list you have, and the other makes a copy and leaves the original
alone. So the first thing to decide is whether you want the original changed.

|Function|Effect|
|-|-|
|`list.sort()`|Sorts the list in place (permanent)|
|`sorted(list)`|Sorts and returns a copy of the list|
|`list.reverse()`|Reverses the list in place (permanent)|
|`reversed(list)`|Reverses and returns an iterator over the list|

---

### Sorting a List In Place

The `list.sort()` method sorts the list itself. The change is permanent.

#### Sorting numbers

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

#### Sorting words

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

#### Mixed types won't sort

Python can sort numbers, and it can sort strings. It can't compare a string with a
number, so a list that holds both can't be sorted:

```python
my_list = [5, "banana", "fig", 1, "date"]
my_list.sort() # TypeError occurs here
print(my_list)
```

Output:

```
TypeError: '<' not supported between instances of 'str' and 'int'
```

The error comes from the sort, not the list. Keep the types consistent if you plan
to sort the list later.

---

### Sorting a Copy of a List

Sometimes you need the items in order, but you want to keep the original order too.
The `sorted()` function makes a sorted copy and leaves the list alone:

```python
my_list = [13, 7, 28, 3, 2, 17]
my_sorted_list = sorted(my_list)
print(my_sorted_list) # The copy is sorted
print(my_list)        # The original list is unchanged
```

Output:

```
[2, 3, 7, 13, 17, 28]
[13, 7, 28, 3, 2, 17]
```

---

### Optional Parameters

`list.sort()` and `sorted()` both accept two optional arguments:

|Argument|Effect|
|-|-|
|`reverse`|If `True`, sort in descending order|
|`key`|A function that decides how items are compared when sorting|

---

#### Sorting in descending order with `reverse=True`

```python
my_list = [13, 7, 28, 3, 2, 17]
my_sorted_list = sorted(my_list, reverse=True)
print(my_sorted_list)
print(my_list)             # The original list is unchanged at this point
my_list.sort(reverse=True) # Now the original list is sorted too
print(my_list)
```

Output:

```
[28, 17, 13, 7, 3, 2]
[13, 7, 28, 3, 2, 17]
[28, 17, 13, 7, 3, 2]
```

#### The `key` argument

The `key` argument takes a function, and Python uses that function's result to decide
the order. Functions get their own chapter, so we'll come back to `key` in Chapter 8.

---

### Reversing a List In Place

The `list.reverse()` method flips the order of the items without sorting them. It
changes the list itself, so the change is permanent.

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

`reversed()` works like `sorted()`. It leaves the original list alone and gives you a
reversed version.

It doesn't hand you a list, though. It returns an iterator, which is an object that
produces the items one at a time. Wrap it in `list()` before you print it:

```python
my_list = [13, 7, 28, 3, 2, 17]
my_reversed_list = reversed(my_list)
print(list(my_reversed_list)) # The copy is reversed
print(my_list)                # The original list is unchanged
```

Output:

```
[17, 2, 3, 28, 7, 13]
[13, 7, 28, 3, 2, 17]
```

---

### Remembering Which Is Which

> To remember which functions make a copy instead of changing the original list, I use
> a mnemonic.
>
> I remind myself that '**d**' stands for **duplicate**.
>
> So the functions that end in the letter 'd' (`sorted()` and `reversed()`) are the
> ones that make a duplicate of the list, instead of changing the original.

---
