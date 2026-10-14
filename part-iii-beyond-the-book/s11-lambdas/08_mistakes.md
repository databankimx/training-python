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
prohibited call just so we can use embed it in a lambda doesn't gain us
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

---
