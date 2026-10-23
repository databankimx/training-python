## Closures in Loops

In some situations involving loops, the behavior of a Python lambda 
function as a closure may be counterintuitive. Predicting this behavior
requires understanding when free variables are bound in the context of a 
lambda.

---

### Using a Traditional Closure

Here is an example of a traditional closure function.

```python
from collections.abc import Callable

def wrapped_function(n: int) -> Callable:
    """Simple wrapper for a closure"""
    def func() -> None:
        """The inner function captures n as a closure"""
        print(n, end=" ")
    return func
```

When we consume this function, `n` will be evaluated at the time that each
closure is defined.

```python
def call_wrapped_function() -> None:
    """Consume the wrapped function"""
    numbers = 1, 2, 3
    funcs = []
    for n in numbers:
        # n is evaluated at definition time
        funcs.append(wrapped_function(n))
    for func in funcs:
        func()
    print()

call_wrapped_function()
```

As a result, we see this...

Output:

```
1 2 3

```

... which is exactly what we expect.

---

### Using a Lambda (Incorrectly)

Here, instead of calling the closure function, we'll use a lambda:

```python
def call_wrapped_lambda() -> None:
    """Consume a wrapped lambda"""
    numbers = 1, 2, 3
    funcs = []
    for n in numbers:
        funcs.append(lambda: print(n, end=" "))
    for func in funcs:
        func()
    print()
```

We would expect this to yield the same output as the closure functions
above. However, when we call it...

```python
call_wrapped_lambda()
```

... we see this

Output:

```
3 3 3

```

And that's definitely *not* what we expected.

What gives?!

---

### How Lambdas Work

We aren't immediately invoking the lambda, so every lambda in `funcs` refers to
the same variable `n` from the loop's scope, not to its own copy. This is called
*late binding*: `n` is looked up when the lambda runs, not when it's defined.

By the time the `for func in funcs:` loop runs, the first loop has finished, and
`n` holds its last value, `3`. So each lambda prints `3`.

The traditional closure avoids this, because each call to `wrapped_function(n)`
creates a new scope with its own `n`.

So how do we fix this?

> Note: the code file has a Pylint disable (`cell-var-from-loop`) and a `# NOSONAR`
> comment on the plain-lambda loop, which demonstrate the problem. Those comments
> stay in the code file.

---

### Ensuring a Defined Value in a Closure Lambda

All we need to do is to ensure that `n` is defined along with the lambda.
This locks the existing value to the closure so that when it is evaluated,
it will not have been modified.

Since we don't have the ability to pass an argument for `n` (the numerical
loop is done when we call the closures), we'll set a default value for the
`n` parameter, using the current value at definition time:

```python
def call_wrapped_lambda_defined() -> None:
    """Consume a wrapped lambda with the free variable defined"""
    numbers = 1, 2, 3
    funcs = []
    for n in numbers:
        funcs.append(lambda n=n: print(n, end=" "))
    for func in funcs:
        func()
    print()
```

The `n=n` in `lambda n=n:` has two different `n` names, and they do different jobs:

* **The `n` on the left of `=`** is the lambda's own parameter. It's local to the lambda,
  and it's the name the lambda's body uses.
* **The `n` on the right of `=`** is the loop variable in `call_wrapped_lambda_defined()`.
  Python evaluates it once, when the lambda is defined, so it takes the value the loop
  has at that moment: `1` for the first lambda, `2` for the second, and `3` for the third.

That value becomes the parameter's default. Each lambda now has its own `n`, stored
as its default, so later changes to the loop variable don't affect it.

When `func()` is called with no arguments, the lambda uses its default value for `n`,
which is the value it was given when it was defined.

Now, calling this function...

```python
call_wrapped_lambda_defined()
```

... yields the expected output:

```
1 2 3
```

---
