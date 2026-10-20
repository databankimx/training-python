"""Lesson 4.4"""

print("Chapter 4:")
print("Exercise 4 - Numeric Lists")

for value in range(1, 6):
    print(value)

nums = []
for i in range(1, 6):
    nums.append(i) #NOSONAR
print(nums)

numbers = list(range(1, 6))
print(numbers)

one, two, three = range(1, 4)
print(f"{one} - {two} - {three}\n")

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 6):
    squares.append(value ** 2)
print(squares)
