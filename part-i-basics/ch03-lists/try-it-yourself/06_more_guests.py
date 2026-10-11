"""Assignment 3.6"""

# More Guests: You just found a bigger dinner table, so now
#              more space is available. Think of three more guests
#              to invite to dinner.

print("Try-it-Yourself:")
print("Assignment 3.6")

guests = ["Charles Babbage", "Ada Lovelace", "George Boole",
          "Grace Hopper", "Alan Turing", "Tim Berners-Lee"]
print(f"I found a bigger table that can seat {len(guests) + 3} people.")
guests.insert(0, "Barbara Liskov")
guests.insert(3, "Donald Knuth")
guests.append("Margaret Hamilton")
print(guests)

print(f"{guests[0]}, would you like to join me for dinner?")
print(f"{guests[1]}, would you like to join me for dinner?")
print(f"{guests[2]}, would you like to join me for dinner?")
print(f"{guests[3]}, would you like to join me for dinner?")
print(f"{guests[4]}, would you like to join me for dinner?")
print(f"{guests[5]}, would you like to join me for dinner?")
print(f"{guests[6]}, would you like to join me for dinner?")
print(f"{guests[7]}, would you like to join me for dinner?")
print(f"{guests[8]}, would you like to join me for dinner?")
