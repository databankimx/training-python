"""Lesson 5.3"""

print("Chapter 5:")
print("Exercise 3 - Handling Multiple Conditions")

# Nested if blocks
low = 10
high = 20
n = 15
if n > low:
    if n < high:
        print("OK")
    else:
        print("ERROR")
else:
    print("ERROR")

# and
if n > low and n < high:
    print("OK")
else:
    print("ERROR")

# or
if n < low or n > high:
    print("ERROR")
else:
    print("OK")

# not
print(not True)
print(not False)

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 21
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 and not age_1 < 21) #pylint: disable=unnecessary-negation #NOSONAR

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

# Precedence: and is applied before or
lst = [1, 2, 3, 4, 5]
if len(lst) > 3 or lst[0] == 1 and lst[-1] == 2:
    print("OK")
else:
    print("ERROR")

# Grouping with parentheses overrides precedence
if (len(lst) > 3 or lst[0] == 1) and lst[-1] == 2:
    print("OK")
else:
    print("ERROR")

# XOR, built from and, or, and not
p = True
q = False

p_xor_q = (p or q) and not (p and q)
print(f"{p} XOR {q} = {p_xor_q}")

p_xor_q = (p and not q) or (q and not p)
print(f"{p} XOR {q} = {p_xor_q}")

# Chaining
s = 1
m = 5
l = 10
m_between = s < m and m < l
print(m_between)

m_between = s < m < l
print(m_between)
