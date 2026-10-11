"""Lesson 5.3"""

print("Chapter 5:")
print("Exercise 3 - Handling Multiple Conditions")

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
age_1 = 21
print(age_0 >= 21 and age_1 >= 21)

print(age_0 >= 21 and not age_1 < 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

p = True
q = False

p_xor_q = (p or q) and not (p and q)
print(f"{p} XOR {q} = {p_xor_q}")

p_xor_q = (p and not q) or (q and not p)
print(f"{p} XOR {q} = {p_xor_q}")
