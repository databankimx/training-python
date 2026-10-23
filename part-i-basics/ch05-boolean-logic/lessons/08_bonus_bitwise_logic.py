"""Lesson 5.8"""

print("Chapter 5:")
print("Exercise 8 - Bitwise Operations")

my_settings = 9

my_comparison = 8
if (my_settings & my_comparison) == my_comparison:
    print("\nThe 8s setting is enabled\n")
else:
    print("\nThe 8s setting is NOT enabled\n")

my_permissions = my_settings | my_comparison

for i in [2 ** x for x in range(4)]:
    if my_permissions & i == i:
        print(f"The user has permission {i}")

my_xor = my_settings ^ my_comparison
print(f"\n{my_settings} XOR {my_comparison} = {my_xor}")

print(f"{my_xor} XOR {my_comparison} = {my_xor ^ my_comparison}")

print(f"\n{~my_settings}\n")

# Negative numbers in 32 bits: the bit pattern of -10 read as an unsigned value
signed_integer = -10
unsigned_integer = signed_integer + (1 << 32)
print(unsigned_integer)

x = 2
x = x << 1
print(x)
x = x >> 1
print(x, "\n")

x = 3
x = x >> 1
print(x, "\n")

x = 5
print(x << 2)
print(x >> 2)
