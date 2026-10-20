"""Assignment 3.7"""

# Shrinking Guest List: You just found out that your new dinner table
#                       won't arrive in time for the dinner, and you
#                       have space for only two guests.

print("Try-it-Yourself:")
print("Assignment 3.7")

guests = [
    "Barbara Liskov",
    "Charles Babbage",
    "Ada Lovelace",
    "Donald Knuth",
    "George Boole",
    "Grace Hopper",
    "Alan Turing",
    "Tim Berners-Lee",
    "Margaret Hamilton"
]

print("Oh no! I can only invite two people to dinner!")
print(f"I'm sorry, {guests.pop(-1)}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop(0)}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"I'm sorry, {guests.pop()}. I can't invite you to dinner.")
print(f"{guests[0]}, you are still invited.")
print(f"{guests[1]}, you are still invited.")
del guests[-1]
del guests[0]
print(guests)
