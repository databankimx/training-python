## String `.format()` Using Indices

Let's look at how index numbers work:

### Single Index

Here is an example where only one index is used:

```python
template = "Hello, {0}!"
values = ("World",)
print(template.format(*values))
```

Output:

```
Hello, World!
```

Of course, there is no reason (other than showing what the items are for the
purpose of this lesson) that either the template or value needs to be stored
as a variable. This would work identically:

```python
print("Hello, {0}!".format("World"))
```

Output:

```
Hello, World!
```

---

### Out of Range Indices

The indices expect a tuple of values (expressions) from which the index in any
placeholder obtains its matching value.

This means that you must be careful with both the order and number of the
arguments. In the previous example, if we coded index `1` instead of `0`, we
would receive an `IndexError`.

```python
template = "Hello, {1}!"
values = ("World",)
print(template.format(*values))
```

Output:

```
Traceback (most recent call last):
  File "...\02_string_format.py", line 11, in <module>
    main()
  File "...\02_string_format.py", line 8, in main
    hello_index()
  File "...\02_string_format.py", line 5, in hello_index
    print(template.format("World"))
          ^^^^^^^^^^^^^^^^^^^^^^^^
IndexError: Replacement index 1 out of range for positional args tuple
```

---

### Multiple Indices

You may have noticed above that when I passed the values tuple to the
`.format()` method, I used the syntax `template.format(*values)`. We use the
asterisk `*` to indicate that the tuple should be split into its individual
values to fill the arbitrary positional arguments of the function.

This starts to matter when we have multiple values, like this:

```python
qty, item, price = 5, "bananas", 0.39
total = qty * price
template = "{0} {1} cost ${2}"
values = (qty, item, total)
print(template.format(*values))
```

Output:

```
5 bananas cost $1.95
```

Again, there is no reason we could not have skipped creating the `template`
and `values` variables and just done this:

```python
qty, item, price = 5, "bananas", 0.39
total = qty * price
print("{0} {1} cost ${2}".format(qty, item, total))
```

---

### Index Order Doesn't Matter

As long as there are arguments for each index specified, the order in which they appear doesn't matter.

```python
qty, item, price = 5, "bananas", 0.39
total = qty * price
template = "{2} {0} cost ${1}"
values = (item, total, qty)
print(template.format(*values))
```

Output:

```
5 bananas cost $1.95
```

---
