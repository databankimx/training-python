## Conditional Tests (Comparisons)

A conditional test compares two values, and it evaluates to `True` or `False`. Python
has a handful of comparison operators:

|Operator|Comparison|Result|
|:-:|-|-|
|`==`|equal|`True` when both operands have the same value|
|`!=`|not equal|`True` when the operands have different values|
|`<`|less than|`True` when the left value is less than the right value|
|`<=`|less than or equal|`True` when the left value is less than or equal to the right value|
|`>`|greater than|`True` when the left value is greater than the right value|
|`>=`|greater than or equal|`True` when the left value is greater than or equal to the right value|
|`is`|same object|`True` when both operands point to the same object in memory|
|`is not`|different object|`True` when the operands point to different objects in memory|

We'll cover `not` and the other logical operators in the next lesson.

---

### Equivalency (`==`)

The most common test is equivalency, `==`. It checks whether two values hold the same data.

Python compares the values, not the types. Two numbers of different types can still be equal,
as the example below shows. Comparing a number to a string is always `False`, because they
don't hold the same data.

To check the opposite, use `!=`, which means "not equal."

#### Equivalency with Numbers

Note: an integer can be equal to a float if the float's decimal part is zero. For example,
`2 == 2.0` returns `True`.

```python
num = 1
print(num == 1)
print(num == 1.0)
print(num == 2)
print(num != 2)
```

Output:

```
True
True
False
True
```

---

#### Equivalency with Strings

String comparisons are case-sensitive, so `'A'` is not the same as `'a'`.

You can work around this by using `upper()` or `lower()` to normalize both values, so they
share a single case.

```python
car = "bmw"
print(car == "bmw")
print(car == "BMW")
print(car.upper() == "BMW") # Work around case sensitivity
```

Output:

```
True
False
True
```

---

### Object Equivalency (`is`)

The `is` keyword checks something different. Instead of asking whether two values are the
same, it asks whether two names point to the same object in memory.

This builds on the list assignment and copying ideas from lesson 4.8. To check the opposite,
use `is not`.

```python
lst = [1, 2, 3]
ref = lst
print(ref == lst)
print(ref is lst)
cpy = lst[:]
print(cpy == lst)
print(cpy is lst)
print(cpy is not lst)
```

Output:

```
True
True
True
False
True
```

The copy has the same values as the original, so `==` returns `True`. It's a different object,
so `is` returns `False`.

---

### Inequalities (`>`, `>=`, `<`, `<=`)

Often, we care more about where one item falls relative to another than whether they're equal.
For that, we use the familiar comparison operators.

#### Inequalities with Numbers

```python
age = 21
print(age > 18)
print(age < 18)
print(age >= 25)
print(age <= 25)
```

Output:

```
True
False
False
True
```

---

#### Inequalities with Strings

Strings complicate inequalities, because Python compares them by the character codes behind
each letter, not by alphabetical order.

That means any lowercase letter is greater than any uppercase letter. A quick look at the
ASCII table explains why:

|Character|ASCII||Character|ASCII|
|:-:|:-:|-|:-:|:-:|
|A|65||a|97|
|B|66||b|98|
|C|67||c|99|
|D|68||d|100|
|E|69||e|101|
|F|70||f|102|
|G|71||g|103|
|H|72||h|104|
|I|73||i|105|
|J|74||j|106|
|K|75||k|107|
|L|76||l|108|
|M|77||m|109|
|N|78||n|110|
|O|79||o|111|
|P|80||p|112|
|Q|81||q|113|
|R|82||r|114|
|S|83||s|115|
|T|84||t|116|
|U|85||u|117|
|V|86||v|118|
|W|87||w|119|
|X|88||x|120|
|Y|89||y|121|
|Z|90||z|122|

Each lowercase letter's code is exactly 32 higher than its uppercase counterpart. Since
inequalities compare those codes, the comparison is case-sensitive. As before, `upper()` and
`lower()` get you around that.

```python
left = "apple"
right = "Zebra"
print(right > left)
print(right.upper() > left.upper())
```

Output:

```
False
True
```

---
