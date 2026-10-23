## Mistakes and Bad Choices

There are some common mistakes you can make when working with lambda 
expressions.

You should not do any of these things!

> Note: Right now, I don't have much in this section, but I will add more
> in the future.

---

### Cheating the Limitation on Raising Exceptions

We know that we cannot raise exceptions from lambda functions because of
the prohibition of statements (remember, a lambda contains one expression 
and zero statements).

But what would happen if we create a function that raises an exception and
then call that function from the lambda?

```python
def throw(ex: Exception) -> None:
    """Raise an exception"""
    raise ex

def throw_from_lambda() -> None:
    """Raise an exception"""
    try:
        (lambda: throw(Exception("Caught an error!")))()
    except Exception as ex:
        print(ex)

throw_from_lambda()
```

Output:

```
Caught an error!
```

It worked. We cheated the system. But this is bad practice. Abstracting a
prohibited call just so we can embed it in a lambda doesn't gain us
anything functionally. It just proves we can do a "*clever*" thing.

It would be better to refactor the lambda as a function and just raise the
exception instead.

---

### Creating Lambdas that are Difficult to Read

Like list comprehensions, programmers who are just discovering lambdas
often want to see how far they can go in pushing the complexity of the
expression defining one.

The result can be a lambda that is just difficult to read (and difficult
to read is difficult to maintain).

Here's an example:

```python
def cryptic_lambda() -> None:
    """Execute a lambda that is hard to read"""
    print((lambda _: list(map(lambda _: _ // 2, _)))([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

cryptic_lambda()
```

Output:

```
[0, 1, 1, 2, 2, 3, 3, 4, 4, 5]

```

Now, you may or may not have figured out that you're using the `map()`
function to generate a list of the values when you integer divide the
provided list's members by two.

If you did figure it out, I'm betting it took longer than it should have.

---

What if we refactored that as a function?

```python
def readable_function() -> None:
    """Execute the same code in a more readable format"""
    div_by_two = lambda n: n // 2
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(map(div_by_two, lst)), "\n")

readable_function()
```

Output:

```
[0, 1, 1, 2, 2, 3, 3, 4, 4, 5]

```

Heck, we can even still use a lambda for the integer division, but I'll
wager you figured out the function much faster than the cryptic lambda.

> Note: the code file turns off several Pylint warnings (`line-too-long`,
> `broad-except`, `unnecessary-direct-lambda-call`, and `unnecessary-lambda-assignment`),
> and it has `# NOSONAR` comments on two lines. Those comments stay in the code file.

---

### Using `map()` for Side Effects

`map()` is for transforming values. Using it only to run a side effect, such as
printing, builds a list that nobody uses:

```python
print(list(map(lambda x: print(x), [1, 2, 3])))
```

Output:

```
1
2
3
[None, None, None]
```

Each `print()` returns `None`, so the list is full of `None` values. A plain `for`
loop does the same job more clearly:

```python
for x in [1, 2, 3]:
    print(x)
```

---

### Mutable Default Arguments in a Lambda

This one is easy to miss, because the lambda looks harmless. This version creates
a new list each time, so it appears to work:

```python
add_to = lambda x, lst=[]: lst + [x]
print(add_to(1))
print(add_to(2))
```

Output:

```
[1]
[2]
```

This version changes the default list in place:

```python
add_and_show = lambda x, lst=[]: (lst.append(x), lst)[1]
print(add_and_show(1))
print(add_and_show(2))
```

Output:

```
[1]
[1, 2]
```

The default list is created once, when the lambda is defined, so every call shares
it. This is the same trap as the mutable default in the dataclasses lessons, where a
`field(default_factory=list)` avoids it.

> Note: the code file turns off several Pylint warnings on these lines, and it has
> `# NOSONAR` comments on them. Those comments stay in the code file.

---

### Forgetting the Parentheses in a Key Function

A key function that returns a method instead of calling it looks reasonable, but
it doesn't do what you want:

```python
words = ["banana", "Apple", "cherry"]
print(sorted(words, key=lambda s: s.lower))
```

The lambda returns the `lower` method itself, not the lowercased string. `sorted()`
tries to compare method objects, which isn't allowed, so it raises a `TypeError`. In
the code file, the `try` block catches this and prints `TypeError raised`.

The fix is to call the method:

```python
print(sorted(words, key=lambda s: s.lower()))
```

Output:

```
['Apple', 'banana', 'cherry']
```

---

### Lambdas Have No Name of Their Own

A lambda's `__name__` is always `<lambda>`:

```python
f = lambda x: 1 / x
print(f.__name__)
```

Output:

```
<lambda>
```

A traceback from inside a lambda shows the same `<lambda>` name, which makes errors
harder to track down in a large codebase. A named function keeps its own name, and it
can have a docstring, which a lambda can't.

---
