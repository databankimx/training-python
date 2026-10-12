"""Lesson 7.7"""

print("Chapter 7:")
print("Exercise 7 - Using a Loop to Move/Remove List Items")

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop(0)
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")
    print(len(pets))

print(pets)
