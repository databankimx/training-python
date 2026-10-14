## Lambdas with `timeit`

Sometimes using a lambda has real advantages. One such example is the
`timeit.timeit()` function.

The `timeit` library provides a number of high-resolution timing 
utilities.

However, not all of them are straightforward to use.

Let's imagine that we want to calculate the factorial of `999` ten times
and determine how long it takes.

---

### `timeit()` with Non-Lambda Code

The `timeit()` function takes as its arguments:

* The code to execute (as a string)
* Any imports necessary (as another string)
* The number of repetitions

So executing achieving our goal with non-lambda code looks like this:

```python
from timeit import timeit

print(timeit("factorial(999)", "from math import factorial", number=10))
```

Output (will vary):

```
0.00025099999038502574
```

But passing in code as strings is awkward and frankly ugly.

---

### `timeit()` with a Lambda

Alternately, we can pass a lambda, which allows us two advantages:

1. We don't need to conceal the code in a string, so if we have to edit
   it, we can take advantage of the editor's syntax highlighting to avoid
   errors.
2. We can simply execute the include and avoid passing it as a string at
   all.

```python
from timeit import timeit
from math import factorial

print(timeit(lambda: factorial(999), number=10))
```

Output (will vary):

```
0.00026409997371956706
```

Personally, I think that's a lot cleaner. It's not always an option, since
some code will not render down to a lambda easily, but when it's available
it's definitely the best choice.

---
