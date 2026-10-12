"""Lesson 7.4"""

print("Chapter 7:")
print("Exercise 4 - Using 'while' Loops")

count = 1
while count <= 5:
    print(count)
    count += 1

print()

while count:
    count -= 1
    print(count)

print()

prompt = "\nTell me something and I will repeat it back to you:\n> "
message = ""
while message.lower() != "quit":
    message = input(prompt)
    print(message)

print()

numbers = [1, 2, 3, 4, 5]
while numbers:
    n = numbers.pop(0)
    print(n)
print(numbers)
