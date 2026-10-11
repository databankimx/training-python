"""Assignment 3.5"""

# Changing Guest List: You just heard that one of your guests
#                      can't make the dinner, so you need to send out
#                      a new set of invitations. You'll have to
#                      think of someone else to invite.

print("Try-it-Yourself:")
print("Assignment 3.5")

guests = ["Charles Babbage", "Ada Lovelace", "George Boole",
          "Grace Hopper", "Alan Turing", "Tim Berners-Lee"]
print(f"{guests[5]} can't join us for dinner.")
guests[5] = "Linus Torvalds"
print(f"{guests[0]}, would you like to join me for dinner?")
print(f"{guests[1]}, would you like to join me for dinner?")
print(f"{guests[2]}, would you like to join me for dinner?")
print(f"{guests[3]}, would you like to join me for dinner?")
print(f"{guests[4]}, would you like to join me for dinner?")
print(f"{guests[5]}, would you like to join me for dinner?")
