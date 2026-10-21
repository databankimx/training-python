"""Lesson 4.7"""

print("Chapter 4:")
print("Exercise 7 - Slicing Lists")

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:3])

print(players[:3])
print(players[:4])

print(players[2:])
print(players[-3:])

print(players[::2])
print(players[::-2])

first_three = players[:3]
first_three.append("tim")
print(first_three)
print(players)

print(players[3:99])

print("Here are the first 3 players on my team")
for player in players[:3]:
    print(player)

name = "Scott"
print(name[::-1])
