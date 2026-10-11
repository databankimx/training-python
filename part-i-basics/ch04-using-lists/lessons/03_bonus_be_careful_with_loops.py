"""Lesson 4.3"""

print("Chapter 4:")
print("Exercise 3 - Be Careful with Loops")

numbers = [1, 2, 3, 4, 5]

print("\nTry to predict the results of the loop.")
input("Press enter to continue after your prediction...\n")

for number in numbers:
    n = numbers.index(number)
    print(numbers.pop(n))
print(numbers)
