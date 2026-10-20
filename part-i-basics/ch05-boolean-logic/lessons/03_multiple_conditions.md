## Combining Multiple Conditionals

Often, it will be necessary to check multiple conditions simultaneously. For
example, if we need to know if something is between a minimum and maximum
value, we have to check both conditions.

---

### A Less-Than-Optimal Solution

We could do this by nesting two if blocks, like this:

```python
min = 10
max = 20
n = 15
if n > min:
    if n < max:
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

---

But that's kind of an ugly pattern, and it's unnecessarily verbose. What we
need is a way to logically group conditions and check them at the same time.

Python provides this for us in the form of logical operators.

---

### Logical Operators

We'll review three logical operators: `and`, `or`, and `not`, as well as a
logical concept that doesn't provide an operator: `xor`.

For each of the operators, I will include a truth table (a matrix indicating
when the operator is `True` or `False`) as well as a code example.

It is a convention to call the operands of a logical operator `p` and `q`, so I
will use that nomenclature below. In the truth tables, I will also abbreviate 
`True` and `False` as `T` and `F` respectively.

I have provided a separate file
[Boolean Logic Test Page](./boolean_logic_tester.html)
to allow you to play around with combinations of values and how the logical
operators evaluate them.

---

#### Logical `and`

The `and` operator will return `True` only if the conditions on both sides are
`True`.

|p|`and`|q|
|:-:|:-:|:-:|
|T|<span style="color:green">**T**</span>|T|
|T|F|F|
|F|F|T|
|F|F|F|

---

Using this, we can simplify the example from above

```python
min = 10
max = 20
n = 15
if n > min and n < max:
    print("OK")
else:
    print("ERROR")
```

Output:

```
OK
```

In a complex conditional, the logical operator should always be evaluated last.

So, when we evaluate the complex conditional (`n > min and n < max`), we do the
following:

1. Evaluate `n > min` which returns `True` for the left condition
2. Evaluate `n < max` which returns `True` for the right condition
3. Evaluate `True and True` which returns `True` based on the truth table

So, the `and` is `True`, which routes us to the "OK" path in the `if`-`else`

---

#### Logical `or`

The `or` operator will return `True` any time at least one of the operands is
`True`. This is known as the *inclusive or*, since it includes the condition
where both operands are `True`

We can think of this as the inverse of `and` in that `or` will only return
`False` when both operands are `False`

|p|`or`|q|
|:-:|:-:|:-:|
|T|<span style="color:green">**T**</span>|T|
|T|<span style="color:green">**T**</span>|F|
|F|<span style="color:green">**T**</span>|T|
|F|F|F|

---

Looking at the previous example, we could achieve the same results using `or`
as we did with `and`.

```python
min = 10
max = 20
n = 15
if n < min or n > max:
    print("ERROR")
else:
    print("OK")
```

Output:

```
OK
```

Here is the breakdown of the conditional evaluation for `n < min or n > max`

1. `15 < 10` -> `False` (left operand)
2. `15 > 20` -> `False` (right operand)
3. `False or False` -> `False` (or)

Since the `or` evaluates to `False`, we follow the `else` branch.

---

#### Logical `not`

Sometimes, the code flow is easier to follow if we invert the condition
being checked. For example it may more intuitive to have the `True` path
contain the code that executes when a condition isn't detected (if the
condition is an error or anomalous data, e.g.).

The `not` operator takes only one operand and returns the opposite value
(negation) of the condition.

|`not`|p|
|:-:|:-:|
|F|T|
|T|F|

---

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

When you have a complex conditional that uses more than one logical
operator, `and` has higher precedence than `or`.

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

---

#### `and` supersedes `or`

When we evaluate the expression, we resolve the `and` first, so...

1. From `len(lst) > 3 or lst[0] == 1 and lst[-1] == 2` we just look at
   `lst[0] == 1 and lst[-1] == 2`
2. `lst[0] == 1` resolves `True`
3. `lst[-1] == 2` resolves `False`
4. `True and False` resolves `False`

... then we resolve the `or`...

5. `len(lst) > 3` resolves `True`
   We already know that `lst[0] == 1 and lst[-1] == 2` resolved `False`
6. `True or False` resolves `True`

And so we end up on the true `if` path.

---

If we had ignored precedence and just evaluated from the left, we would
have gotten the opposite result

1. Starting with the `or` we evaluate `len(lst) > 3 or lst[0] == 1`
2. `len(lst) > 3` resolves `True`
3. `lst[0] == 1` resolves `True`
4. `True or True` resolves `True`
5. Now we have `True and lst[-1] == 2`
6. `lst[-1] == 2` resolves `False`
7. `True and False` resolves `False` (**WRONG!**)

... which would have diverted us to the `else` path.

---

#### `not` has the highest precedence

You should always evaluate `not` as soon as its immediate right operand is
resolved.



---

#### Grouping

To allow us to override precedence, Python permits the use of parentheses
for grouping.

Looking at our previous example, if we had grouped the conditions around
the `or`, it would have properly been evaluated first.

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

1. Starting with the `or` in parentheses, we evaluate
   `len(lst) > 3 or lst[0] == 1`
2. `len(lst) > 3` resolves `True`
3. `lst[0] == 1` resolves `True`
4. `True or True` resolves `True`
5. Now we have `True and lst[-1] == 2`
6. `lst[-1] == 2` resolves `False`
7. `True and False` resolves `False`

... which diverts us to the `else` path.

---

### Bonus - Simulating XOR

There is no logical operator for the *exclusive or* (XOR) condition.

However, if we compare their truth tables, we'll see that an XOR is the
same as `or` if we make sure that we set the condition `False` when 
`and` is `True`. So a truth table for XOR would look like this:

|p|XOR|q|
|:-:|:-:|:-:|
|T|F|T|
|T|<span style="color:green">**T**</span>|F|
|F|<span style="color:green">**T**</span>|T|
|F|F|F|

That reflects more closely what human language means when we say "either
this or that".

Another way to say this is to say that XOR means `or` but `not and`.

```python
s = 1
m = 5
l = 10
m_is_least = m < s and m < l
m_is_between = (m < s or m < l) and not m_is_least # XOR
print(m_is_between)
```

Output:

```
True
```

---

### Bonus - Chaining

If we want to compare three numbers using inequalities, we can do what we've
done thus far and use `and` like this:

```python
s = 1
m = 5
l = 10
m_between = s < m and m < l
```

---

However, Python permits us to us a shorthand for `and` where we can chain 
multiple instances of an inequality, like this:

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

Obviously, the order matters, as chaining should only be used with the same
directionality.

* You can chain `<` and `<=`
* You can chain `>` and `>=`
* But you should not chain `<` and `>`
    * Keep to one direction (greater or less but not both)

---
