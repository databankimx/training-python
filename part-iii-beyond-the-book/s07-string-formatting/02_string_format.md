## The String `.format()` Function

In v2.6, as an improvement on the somewhat cumbersome string-modulo operator,
Python introduced the `.format()` method for the `str` type.

With the `.format()` method, we use curly brace pairs `{}` as the 
placeholders (removing the requirement to specify type, which was never 
enforced in the first place). The arguments to the function are expressions,
and each one replaces a pair of curly braces in the resulting string.

---

### The Basic Idea

Here is a template with one placeholder, and a single argument that fills it:

```python
template = "Hello, {}!"
print(template.format("World"))
```

Output:

```
Hello, World!
```

The `.format()` method is called on the template string. It returns a new
string and leaves the template unchanged.

---

### Several Placeholders

Each pair of braces takes the next argument, in order:

```python
print("{} {}".format("Hello", "World"))
```

Output:

```
Hello World
```

Because the arguments are expressions, they can be any values, including the
results of calculations:

```python
print("{} + {} = {}".format(2, 3, 2 + 3))
```

Output:

```
2 + 3 = 5
```

---

### Choosing Where Each Argument Goes

The braces can also say which argument to use. There are three ways to do this,
each covered in its own lesson:

* [The index indicated in the braces](./03_format_indices.md) - `{0}` and `{1}`
  refer to arguments by their position.
* [The keyword indicated in the braces](./04_format_keywords.md) - `{name}`
  refers to an argument by its keyword.
* [The order of appearance if the braces are left empty](./05_format_auto.md) - `{}`
  takes the next argument, in order.

For example, an index chooses the arguments in any order:

```python
print("{1} {0}".format("world", "hello"))
```

Output:

```
hello world
```

And a keyword makes the template easier to read:

```python
print("Name: {name}, Age: {age}".format(name="Scott", age=54))
```

Output:

```
Name: Scott, Age: 54
```

---

### Mixing the Styles

Automatic numbering (`{}`) and numbered placeholders (`{0}`, `{1}`) cannot be
mixed in the same template. Python raises an error if you try:

```python
print("{} {0}".format("Hello", "World"))
```

Output:

```
ValueError: cannot switch from automatic field numbering to manual field specification
```

Keyword placeholders (`{name}`) can be mixed with `{}`, because a keyword is
not a position. Choose one style for each position in the template.

---

### Comparing with the String-Modulo Operator

The same message can be written with either method. The `.format()` version
uses `{}` where the modulo version uses `%s`, and it doesn't need the values in
a tuple:

```python
print("Hello, %s!" % ("World",))
print("Hello, {}!".format("World"))
```

Output:

```
Hello, World!
Hello, World!
```

The format specifiers that control how values are displayed (such as the number
of decimal places) are covered later in this section.

---

### Where to Go Next

Start with the [string-modulo operator](./01_string_modulo.md) if you haven't
read it yet. Then continue with the three ways of choosing arguments above, and
the [reusing placeholders](./06_reuse_placeholders.md) and
[conversion](./07_conversion.md) lessons.

---
