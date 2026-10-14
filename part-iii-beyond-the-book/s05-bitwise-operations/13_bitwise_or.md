## Using Bitwise OR (`|`)

<style>
    td, th {
        border: 0!important;
        padding: 0!important;
        margin: 0!important;
        padding-left: 25px!important;
    }
</style>

The bitwise OR operator (`|`) is used to compare two values and return
the union of their set ($1$) bits.

This operation is an *inclusive* OR, meaning that the result bit will be 
set to $1$ any time a $1$ is found in either value, irrespective of the 
other value.

This can be seen by observing the truth table we previously laid out for 
the bitwise OR operation.

|$b_1$|\||$b_2$|
|:-|:-:|-:|
|$1$|$1$|$1$|
|$1$|$1$|$0$|
|$0$|$1$|$1$|
|$0$|$0$|$0$|

---

Consider this scenario:

> ||
> |-:|
> |$a=1001~1100_2=156_{10}$|
> |$b=0011~0100_2=~~52_{10}$|
> |$a~\|~b=1011~1100_2=188_{10}$|

Any position where either value's bit is $1$ (including when both are set) 
will return a $1$.

As long as we understand that what's being compared are the individual
bits, we can express the values in any base with the same results

```python
a = 0b10011100 # 156
b = 0b00110100 # 52
print(f"{(a | b):>08b}") # --> 1011 1100 (188)

x = 156
y = 52
print(x | y) # --> 188
```

Output:

```
10111100
188
```

---

### A Simple Example: Adding a Permission

In many languages, when accessing a file, you sometimes need to specify the
permissions with which you're opening the file. Can you read, write, or 
both?

In Python, this isn't the case. Instead, we use one or more of a set of
strings representing the permissions we want to use.

But let's imagine a scenario where we did have file permission values as
integers.

```python
read = 1
write = 2
read_write = 3
```

Your first thought upon seeing this example is that $3$ ($0011$) is not 
a power of two, so it cannot be represented by setting a single bit.

Worse, it uses both of the bits already in use by read ($0001$) and write 
($0010$).

We can use the bitwise OR operator (in this case, the combined assignment
operator) to apply the permissions we need.

```python
# -- SNIP --

file_path = "C:\\Temp\\test.txt"
need_to_write = True

# Start with just read permission 0000_0001 (1 = read)
permissions = read

# Add the write permission only if needed 0000_0010 (2 = write)
if need_to_write:
    permissions |= write

print(f"{permissions:04b} = {permissions}")
```

Output:

```
0011 = 3
```

Using a bitwise OR added on the `write` permission while retaining the 
`read` permission, resulting in the `read_write` permission.

---
