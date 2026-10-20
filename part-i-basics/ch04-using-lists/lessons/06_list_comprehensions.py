"""Lesson 4.6"""

print("Chapter 4:")
print("Exercise 6 - List Comprehensions")

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

squares = [value ** 2 for value in range(1, 11)]
print(squares)

even_squares = [value ** 2 for value in range(1, 11) if value % 2 == 0]
print(even_squares)
