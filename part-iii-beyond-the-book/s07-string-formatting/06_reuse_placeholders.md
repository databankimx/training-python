## Reusing Placeholder Values

You can use the same placeholder multiple times in the string template, and
it will be replaced with the same value from the values tuple.

---

### A Simple Example

In the following example, we have the `squared` value only once in the values
tuple, but it appears twice in the template and therefore in the resulting 
string:

```python
x, y = 2, 3
squared = "²"
print("{0}{1} = {2}\n{3}{1} = {4}\n".format(x, squared, x ** 2, y, y ** 2))
```

Output:

```
2² = 4
3² = 9
```

---

### Accessing Properties

You can access the properties of an object in the placeholder.

Here is an example using an imaginary number. We can access the real and
imaginary parts of the number directly from the placeholder.

This allows us to pass only one argument `x` to the `format()` function.

```python
x = 3 + 5j
print("Real = {0.real}\nImag = {0.imag}\n".format(x))
```

Output:

```
Real = 3.0
Imag = 5.0
```

---
