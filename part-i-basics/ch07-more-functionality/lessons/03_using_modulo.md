## Using the Modulo Operator

Though a new arithmetic operation for non-programmers, the modulo operator `%`
is one of the most useful features in programming.

The scenarios where modulo computation is useful are nearly uncountable.

The function of the modulo operator is to return the remainder left over after
dividing some number by a modulus (some other number) and takes the following
syntax:

```python
var = number % modulus
```

---

### Modulo as Remainder

Let's look at the result (remainder of integer division) of the modulo 
operator on several numbers:

```python
numbers = [4, 5, 6, 7]
for number in numbers:
    print(f"{number} % 3 = {number % 3}")
```

Output:

```
4 % 3 = 1
5 % 3 = 2
6 % 3 = 0
7 % 3 = 1
```

---

### Identifying Multiples

A common use of modulus is when you want to determine if a number is a 
multiple of another number, for which we can define this rule:

```python
# For any integers, m and n
if n % m == 0:
    # then n is a multiple of m
```

Since zero is a *falsy* value, we can also express it like this:

```python
# For any integers, m and n
if not n % m:
    # then n is a multiple of m
```

An example of this use is to identify even versus odd numbers.

We know that any multiple of 2 is an even number, so:

```python
number = int(input("\nEnter an integer:\n> "))
if number % 2 == 0:
    condition = "even"
else:
    condition = "odd"
print(f"The number {number} is {condition}.")
```

User Prompt:

```
Enter an integer:
> _
```

Let's assume the user typed `7` + `<ENTER>`

Output:

```
The number 7 is odd.
```

---

<span style="color:salmon">**Homework Alert!**</span>

### Checking for Prime Numbers

A fun exercise you can try is using modulo to determine if a number is prime

* Definition of a prime number:  
  Any positive integer that has exactly two integer factors: 1 and itself
    * 0 is the additive identity and is neither positive nor negative,  
      so it is not a prime number
    * Since 1 only has one factor (itself), it is the unit number, not a prime
    * 2 is the smallest (and only even) prime number
    * All non-prime positive integers are called composite numbers

Try to resist the urge to look at my examples until you try it yourself:

> Example file [primes.zip](./primes.zip) - password: *igiveup*

Think about efficiency as well as functionality

---
