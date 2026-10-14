## Lambda Functions

Based on Alonzo Church's "lambda calculus," (a stateless but 
Turing-complete computational system invented in the 1930s), the lambda 
concept allow the abstraction of functions.

Unlike languages like Lisp, Haskell, and F#, Python is not natively a 
*functional* programming language. Instead, it is an object-oriented 
programming language.

However, some concepts from functional languages are implemented in
Python, specifically:

* Functions are First-Class Objects
    * They can be bound to names (like local variables)
    * They can be passed as arguments to (and returned from) functions

Since lambda calculus is a system based solely on functions, the Python
implementation of functions as first-class citizens uses lambda
nomenclature and symbols.

Lambda syntax takes the following forms:

```python
(lambda <parameters>: <return expression>)(arguments)
```

---

### A simple Example: The Identity Function

In any programming language that implements functions, we can create an
identity function (a function that simply returns the argument passed to
it).

#### Identity As a Classic Function

```python
def identity(x: any) -> any:
    """The identity function simply returns its argument"""
    return x
```

If we call that function, we just get back whatever we passed.

```python
n = 42
print(f"identity(n) returns: {identity(n)}")
```

Output:

```
identity(n) returns: 42
```

---

#### Identity As a Lambda

When implementing a lambda, there is no need to declare a function.
Instead, we'll just implement the lambda call.

```python
n = 42
print(f"(lambda x: x)(n) returns: {(lambda x: x)(n)}")
```

Output:

```
(lambda x: x)(n) returns: 42
```

---

#### Breaking Down the Identity Lambda

We used this syntax for the lambda above:

```python
(lambda x: x)(n)
```

Breaking that down, we have:

* A declaration that this is a lambda: `lambda`
* A list of the incoming parameters: `x`
* A colon separating the function part from the return part: `:`
* The return: `x`
* The argument being passed into the parameter: `n`

We can see that this is equivalent to both the declaration of a function 
like we built previously and a call to it, the difference being that the
function isn't named.

```python
def anonymous(x):
    return x
anonymous(n)
```

---

### A Second Example: Add One

Obviously, the identity is a useless example, so keeping it simple, we'll
create a function (and its equivalent lambda) that does something with
the data.

```python
def plus_one(x: int) -> int:
    """Add one to the argument"""
    return x + 1

n = 42
print(f"plus_one(n) returns: {plus_one(n)}")
print(f"(lambda x: x + 1)(n) returns: {(lambda x: x + 1)(n)}")
```

Output:

```
plus_one(n) returns: 43
(lambda x: x + 1)(n) returns: 43
```

Python executes a reduction strategy to evaluate the lambda:

* `(lambda x: x + 1)(n)`
* `(lambda x: x + 1)(42)` -> Sub in the value for `n`
* `lambda 42: 42 + 1` -> Sub in the argument `n` for `x`
* `42 + 1` -> Convert from lambda to plain expression
* `43` -> Resolve the expression

---

### A Lambda as a Variable

We can store a lambda in a variable and then call it like a function.

When used like this, we omit passing the argument when declaring the
lambda.

```python
n = 42
plus_two = lambda x: x + 2
print(f"plus_two(n) = (lambda x: x + 2)(n), returns: {plus_two(n)}")
```

Output:

```
plus_two(n) = (lambda x: x + 2)(n), returns: 44
```

---

### Multiple Parameters

A lambda can have multiple parameters, which are comma-separated just
like in a traditional function.

```python
a, b = 21, 21
sum_args = lambda x, y: x + y
print(f"sum_args(a, b)  returns: {sum_args(a, b)}")
print(f"(lambda x, y: x + y)(a, b) returns: {(lambda x, y: x + y)(a, b)}")
```

Output:

```
sum_args(a, b) returns: 42
(lambda x, y: x + y)(a, b) returns: 42
```

We can see that using the lambda directly is identical to storing it in
a variable and calling it like a function.

---

### Terminology

* A lambda used by itself is called an **anonymous lambda**
* A lambda stored in a variable is called a **named lambda**

The *anonymous lambda* is also what is called an *immediately invoked 
function expression (IIFE)*, and although they work, Python discourages
the use of immediately invoked lambdas.

---
