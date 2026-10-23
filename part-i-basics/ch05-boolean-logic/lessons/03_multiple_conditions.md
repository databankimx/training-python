## Combining Multiple Conditions

Often you need to check more than one condition at the same time. Say you want to know
whether a number falls between a minimum and a maximum. You have to check both
conditions.

---

### A Less-Than-Optimal Solution

You could nest two `if` blocks:

```python
low = 10
high = 20
n = 15
if n > low:
    if n < high:
        print("OK")
    else:
        print("ERROR")
else:
    print("ERROR")
```

Output:

```
OK
```

It works, but it's clumsy, and it repeats the `else` branch. What we need is a way to group
conditions and check them together. Python gives us logical operators for exactly that.

---

### Logical Operators

We'll review three logical operators, `and`, `or`, and `not`, and one logical idea that
doesn't have its own operator, `xor`.

For each operator, I include a truth table, which lists when the operator is `True` or
`False`, along with a code example.

By convention, the operands of a logical operator are called `p` and `q`, and I'll use those
names below. In the truth tables, `True` and `False` are shortened to `T` and `F`.

To play with combinations of values and see how the operators evaluate them, open the
[Boolean Logic Test Page](./boolean_logic_tester.html).

---

#### Logical `and`

The `and` operator returns `True` only when the conditions on both sides are `True`.

|p|`and`|q|
|:-:|:-:|:-:|
|T|<span style="color:green">**T**</span>|T|
|T|F|F|
|F|F|T|
|F|F|F|

---

With `and`, the earlier example becomes a single condition:

```python
low = 10
high = 20
n = 15
if n > low and n < high:
    print("OK")
else:
    print("ERROR")
```

Output:

```
OK
```

Python resolves each comparison first, and then `and` combines the results. For
`n > low and n < high`:

1. `n > low` is `True`, because 15 is greater than 10.
2. `n < high` is `True`, because 15 is less than 20.
3. `True and True` is `True`, according to the truth table.

Since `and` is `True`, the code takes the `"OK"` path.

---

#### Logical `or`

The `or` operator returns `True` whenever at least one operand is `True`. This is called the
*inclusive or*, because it also counts the case where both operands are `True`.

It returns `False` only when both operands are `False`.

|p|`or`|q|
|:-:|:-:|:-:|
|T|<span style="color:green">**T**</span>|T|
|T|<span style="color:green">**T**</span>|F|
|F|<span style="color:green">**T**</span>|T|
|F|F|F|

---

The same check works with `or`, written the other way around:

```python
low = 10
high = 20
n = 15
if n < low or n > high:
    print("ERROR")
else:
    print("OK")
```

Output:

```
OK
```

Here's how `n < low or n > high` resolves:

1. `15 < 10` is `False` (left operand).
2. `15 > 20` is `False` (right operand).
3. `False or False` is `False`.

Since the `or` is `False`, the code takes the `else` branch.

---

#### Logical `not`

Sometimes the code is easier to follow if you invert a condition. For example, it can read
more naturally to put the normal path in the `if` and the error path in the `else`, when the
condition describes an error.

The `not` operator takes one operand and returns the opposite value.

|`not`|p|
|:-:|:-:|
|F|T|
|T|F|

```python
print(not True)
print(not False)
```

Output:

```
False
True
```

---

### Logical Operator Precedence

When a condition uses more than one logical operator, Python applies them in a set order.
Here's the order, from highest to lowest:

1. `not`
2. `and`
3. `or`

So `and` is applied before `or`:

```python
lst = [1, 2, 3, 4, 5]
if len(lst) > 3 or lst[0] == 1 and lst[-1] == 2:
    print("OK")
else:
    print("ERROR")
```

Output:

```
OK
```

Here's how Python reads that condition:

1. Python resolves the `and` first, so we look at `lst[0] == 1 and lst[-1] == 2`.
2. `lst[0] == 1` is `True`.
3. `lst[-1] == 2` is `False`.
4. `True and False` is `False`.

Now the `or` is left with `len(lst) > 3 or False`:

5. `len(lst) > 3` is `True`.
6. `True or False` is `True`.

So the condition is `True`, and the code takes the `"OK"` path.

If Python had read the condition strictly from left to right, the answer would flip:

1. `len(lst) > 3 or lst[0] == 1` is `True or True`, which is `True`.
2. `True and lst[-1] == 2` is `True and False`, which is `False`.

That would take the `else` path, which is wrong for this condition. Precedence matters.

---

#### Grouping

You can override precedence with parentheses. Grouping the `or` makes Python evaluate it first:

```python
lst = [1, 2, 3, 4, 5]
if (len(lst) > 3 or lst[0] == 1) and lst[-1] == 2:
    print("OK")
else:
    print("ERROR")
```

Output:

```
ERROR
```

1. The `or` inside the parentheses resolves first: `len(lst) > 3` is `True`, so `True or True`
   is `True`.
2. `True and lst[-1] == 2` becomes `True and False`, which is `False`.

Now the condition is `False`, so the code takes the `else` path.

---

### Bonus: Simulating XOR

Python has no operator for *exclusive or* (XOR), which is `True` when exactly one operand is
`True`. You can build it from the operators you already have.

|p|XOR|q|
|:-:|:-:|:-:|
|T|F|T|
|T|<span style="color:green">**T**</span>|F|
|F|<span style="color:green">**T**</span>|T|
|F|F|F|

That matches what people usually mean by "either this or that, but not both." The idea is
`or`, with the case where both are `True` removed. In code, that's `p or q`, and not both,
which is `not (p and q)`:

```python
p = True
q = False
p_xor_q = (p or q) and not (p and q)
print(f"{p} XOR {q} = {p_xor_q}")
```

Output:

```
True XOR False = True
```

The same truth table can be written another way, as one side or the other, but not both:

```python
p_xor_q = (p and not q) or (q and not p)
print(f"{p} XOR {q} = {p_xor_q}")
```

Output:

```
True XOR False = True
```

Both forms give the same answer for every combination of `p` and `q`, so you can pick whichever
reads better to you.

---

### Bonus: Chaining

To check that a number sits between two others, you can combine two comparisons with `and`:

```python
s = 1
m = 5
l = 10
m_between = s < m and m < l
```

Python also lets you chain comparisons, which reads more like the math:

```python
s = 1
m = 5
l = 10
m_between = s < m < l
print(m_between)
```

Output:

```
True
```

The chained form means the same thing as `s < m and m < l`, with `m` checked only once.

The direction matters. Chain comparisons that point the same way:

* You can chain `<` and `<=`
* You can chain `>` and `>=`
* Avoid chaining `<` and `>` together, even though Python allows it. The result is hard to
  read, and you'll probably have to think about it twice.

---
