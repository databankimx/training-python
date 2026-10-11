"""Lesson 4.1"""

print("Chapter 4:")
print("Exercise 1 - Looping in lists")

magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician)

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}\n")
print("Thank you everyone. That was a great magic show!\n")
