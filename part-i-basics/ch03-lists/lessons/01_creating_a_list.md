## Creating a List and Accessing Values

Lists are ordered collections of items.

Items in Python lists do not need to be of the same data type.

---

### Syntax

* Surround a list with square brackets `[]`
* Separate items with commas `,`<br>
  e.g.:<br>
  ```python
  numbers = [1, 2, 3, 4, 5]
  number_names = ["one", "two", "three"]
  ```

---

### Indexing
                 
List indices are zero-based and allow backward-indexing, so:

* First item is always `list_name[0]`
* Last item is always `list_name[-1]`

Regardless of list length.

---

> ### Why Do We Count From Zero, Not One?
> 
> In many programming languages (particularly older languages like C and C++),
> the underlying data structure on which a list is built is called an `array`.
> 
> For an array, the variable doesn't actually contain all of the elements of
> the array; instead it contains a pointer to the place in memory where the
> array starts. Additionally, arrays traditionally contained a single, static
> sized data type.
> 
> Then, the index defines how far we have to move in memory from that starting
> point in units the size of the array type.
> 
> So, in a language like C++, where the `int` data type is four bytes in size,
> the location of any element is the staring location plus the index times
> the size of the element.
> 
> |||||
> |:-:|:-:|:-:|:-:|
> |Type|Size|Index|Location|
> |`int`|4 bytes|`0`|`start + 0 * 4 = start + 0`|
> |\"|\"|`1`|`start + 1 * 4 = start + 4`|
> |\"|\"|`2`|`start + 2 * 4 = start + 8`|
> 
> ... and so on.
> 
> 
> Since the first element is stored at the staring location, its offset is
> zero bytes. Using an index of zero makes the computation of the location > easier.
> 
> Now, in Python, we don't actually use the array as the fundamental type.
> Instead, the `list` itself is the most fundamental type of collection. And
> unlike an array, this is what's called a *linked list*, meaning that each
> element contains not only a value but a link to the next element in the list.
> This is necessary since the list can composed of different data types, many
> of which are not static sized.
> 
> The first element, however, is still located at the start location of the
> list, so it still has an offset of zero and therefore index zero. That way,
> the list variable doesn't need to contain two pointers (one to start 
> location, and a separate one to the first element).

---

### Examples

```python
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[1].title())
print(bicycles[-2].upper())

message = f"My favorite bicycle was a {bicycles[0].title()}."
print(message)
```

Output:

```
['trek', 'cannondale', 'redline', 'specialized']
trek
specialized
Cannondale
REDLINE
My favorite bicycle was a Trek.
```

---

### Avoid Index Errors

If you specify an index value that is not included in the list, you will
receive an IndexError.

Example:

In this list, there are three elements, filling indices 0, 1, and 2.

Requesting index 3 results in an error because the list doesn't contain
an element at that index.

```python
my_list = [1, 2, 3]
print(my_list[3])
```

Output:

```
Traceback (most recent call last):
  File "...\indexes.py", line 2, in <module>
    print(my_list[3])
          ~~~~~~~^^^
IndexError: list index out of range
```

---
