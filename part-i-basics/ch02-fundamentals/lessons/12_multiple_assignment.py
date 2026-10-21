"""Lesson 2.12"""

print("Chapter 2:")
print("Exercise 12 - Multiple Assignment")

# You can assign multiple variables simultaneously
x, y, z = 1, 2, 3
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

# Swapping values without a temporary variable
a = 1
b = 2
a, b = b, a
print(a, b)

# --- Unpacking collections (upcoming concepts) ---

# From a range
a, b, c = range(1, 4)
print(a, b, c)

# From a tuple
d, e, f = (1, 2, 3)
print(d, e, f)

# From a list
g, h, i = [1, 2, 3]
print(g, h, i)

# From a set. Sets have no guaranteed order, so this output isn't promised.
j, k, l = {1, 2, 3}
print(j, k, l)
