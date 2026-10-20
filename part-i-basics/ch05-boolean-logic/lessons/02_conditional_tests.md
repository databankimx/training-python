## Conditional Tests (Comparisons)

A conditional test is a comparison between two values. These tests come in
several types:

|Operator|Comparison|Result|
|:-:|-|-|
|`==`|equal|`True` when both operands contain the same value|
|`!=`|not equal|`True` when the operands contain different values|
|`<`|less than|`True` when the left value is less than the right value|
|`<=`|less than or equal|`True` when the left value is less than or equal to the right value|
|`>`|greater than|`True` when the left value is more than the right value|
|`>=`|greater than or equal|`True` when the left value is more than or equal to the right value|
|`is`|same object|`True` when both operands point to the same object in memory|
|`is not`|different object|`True` when the operands point to different objects in memory|
|`not` or `!`|inverse/negation|`True` when the right (and only) operand is `False`|

---

### Equivalency (`==`)

The most commonly used test is equivalency `==`, which tests to see whether
two items contain identical data.

Since the data must be identical, the data types must be the same (e.g.:
compare a number to a number or a string to a string).

To negate `==` we use the `!=` (not equal) operator

#### Equivalency with Numbers

Note: An integer can return `True` when compared with a float it the
float's decimal part is zero (e.g.: `2 == 2.0` returns `True`)

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

String comparisons are case-sensitive (that is, 'A' is not the same as 'a')

We can work around this by using the `upper()` or `lower()` functions to
normalize the data so that both operands share a single case.

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

Another form of equivalency checking uses the `is` keyword. Instead of 
checking that the values are the same, this checks that the two operands
point to the same object in memory.

Consider this example, using the lesson we learned about list assignment
versus copying.

To negate `is`, we use the `not` keyword

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

---

### Inequalities (`>`, `>=`, `<`, `<=`)

Often, we're more interested in where an item falls in relation to another as
opposed to actual equivalency between the items.

For these, we have the typical arithmetic comparisons.

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

Strings complicate the inequality relationships, because they are evaluated
based on the ASCII value of the characters, not by alphabetical order.

Any lower case letter will always evaluate as greater than any upper case 
letter because of this.

A quick look at the ASCII table will explain why:

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

As you can see, the ASCII value of any lower case character is 32 higher than
its upper case counterpart.

And since inequalities compare the ASCII values, that makes them
case-sensitive. But as mentioned before, we can work around this limitation
using the `upper()` or `lower()` functions.

---

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
