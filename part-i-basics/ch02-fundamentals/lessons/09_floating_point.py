"""Lesson 2.9"""

print("Chapter 2:")
print("Exercise 9 - Floating-Point Decimals")

print(f"0.1 + 0.1 = {0.1 + 0.1}")
print(f"0.2 + 0.2 = {0.2 + 0.2}")
print(f"2 * 0.1 = {2 * 0.1}")
print(f"2 * 0.2 = {2 * 0.2}")

# Be careful: you will sometimes see an arbitrary number of decimal digits
print(f"0.2 + 0.1 = {0.2 + 0.1}")
print(f"3 * 0.1 = {3 * 0.1}")
# ... but not always
print(f"0.3 = {0.3}")

# If any operand is a float, the result is a float
x = 3
y = 2.0
z = 4
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y}")
print(f"({x} + {y}) * {z} = {(x + y) * z}")
