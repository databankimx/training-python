"""Assignment 5.5"""

# Alien Colors #3: if-elif-else chain.
#                  Green: 5 pts. Yellow: 10 pts. Red: 15 pts.
#                  Write three versions, one per color.

print("Try-it-Yourself:")
print("Assignment 5.5")

alien_colors = ["green", "yellow", "red"]
for alien_color in alien_colors:
    if alien_color == "green":
        points = 5
    elif alien_color == "yellow":
        points = 10
    elif alien_color == "red":
        points = 15
    else:
        points = 0
    print(f"You earned {points} points!")
