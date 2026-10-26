"""Assignment 3.10"""

# Every Function: Write a program that creates a list and uses each
#                 function introduced in this chapter at least once.

print("Try-it-Yourself:")
print("Assignment 3.10")

# Part 1: a list of snacks
snacks = ["popcorn", "pretzels", "apple"]
print(f"We start with {len(snacks)} snacks: {snacks}")   # len()
print(snacks[0])                                          # indexing
snacks[1] = "trail mix"                                   # modifying a value
snacks.append("cheese")                                   # append()
snacks.insert(0, "chips")                                 # insert()
snacks.remove("apple")                                    # remove()
print(snacks)
last = snacks.pop()                                       # pop()
first = snacks.pop(0)                                     # pop() with an index
print(f"Popped {last} and {first}: {snacks}")
del snacks[0]                                             # del
print(snacks)

# Part 2: sorting and reversing a list of numbers
scores = [13, 7, 28, 3]
scores.sort()                                             # sort()
print(scores)
print(sorted(scores, reverse=True))                       # sorted()
scores.reverse()                                          # reverse()
print(scores)
print(list(reversed(scores)))                             # reversed()
scores.clear()                                            # clear()
print(scores)
