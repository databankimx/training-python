"""Lesson 6.15"""

print("Chapter 6:")
print("Exercise 15 - Dictionary Comprehensions")

keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]

dictionary = {}
for i, key in enumerate(keys):
    dictionary[key] = values[i]
print(dictionary)

dictionary = {keys[i]: values[i] for i in range(len(keys))}
print(dictionary)

dictionary = {key: value for (key, value) in zip(keys, values)}
print(dictionary)

odd_dictionary = {key: value for (key, value) in zip(keys, values) if value % 2 == 1}
print(odd_dictionary)
