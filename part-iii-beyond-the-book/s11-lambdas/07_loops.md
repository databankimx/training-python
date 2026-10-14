## Closures in Loops

In some situations involving loops, the behavior of a Python lambda 
function as a closure may be counterintuitive. Predicting this behavior
requires understanding when free variables are bound in the context of a 
lambda.

---

### Using a Traditional Closure

Here is an example of a traditional closure function.

```python
def wrapped_function(n: int) -> callable:
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
1, 2, 3
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

We aren't immediately invoking the lambda, which means that the value of
`n` is evaluated during runtime, not when the lambda is defined. As a
result, we have what's known as a *modified closure*, where the captured
value has been mutated before it can be used.

In effect, each of the closure lambdas in the `for func in funcs:` loop
possesses the last captured value `3` by the time it executers.

So how do we fix this?

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

Now, calling this function...

```python
call_wrapped_lambda_defined()
```

... yields the expected output:

```
1 2 3
```

---
