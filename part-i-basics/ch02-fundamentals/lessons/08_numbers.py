"""Lesson 2.8"""

print("Chapter 2:")
print("Exercise 8 - Numerical Operators")

x = 3
y = 2
z = 4

# Operators (Note: PEMDAS precedence order is in effect)
# Oper | Meaning  | Example
#   +    add        3 + 2 -> 5
print(f"{x} + {y} = {x + y}")
#   -    subtract   3 - 2 -> 1
print(f"{x} - {y} = {x - y}")
#   *    multiply   3 * 2 -> 6
print(f"{x} * {y} = {x * y}")
#   /    divide     3 / 2 -> 1.5
print(f"{x} / {y} = {x / y}")
#          	       4 / 2 -> 2.0 (all division returns float, even if result is whole)
print(f"{z} / {y} = {z / y}")
#   **   exponent   3 ** 2 -> 9
print(f"{x} ** {y} = {x ** y}")
#        PEMDAS     3 + 2 * 4 -> 11
print(f"{x} + {y} * {z} = {x + y * z}")
#   ()   grouping   (3 + 2) * 4 -> 20
print(f"({x} + {y}) * {z} = {(x + y) * z}")
