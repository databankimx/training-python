"""Lesson 6.12"""

print("Chapter 6:")
print("Exercise 12 - Nesting Dictionaries in a List")

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print()

num_aliens = 30
aliens = []
for _ in range(num_aliens):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
print(len(aliens), aliens[0])

print()

aliens = [{"color": "green", "points": 5}] * 3
aliens[0]["color"] = "red"
print(aliens)

print()

aliens = []
for _ in range(num_aliens):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens[:5]:
    print(alien)
