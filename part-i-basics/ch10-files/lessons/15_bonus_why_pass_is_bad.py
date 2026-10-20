"""Lesson 10.15"""

print("Chapter 10:")
print("Exercise 15 - Bonus Lesson - Why `except: pass` is Bad!\n")

# Use CTRL+C to break this loop
i = 0
while True:
    i += 1
    print(f"(iteration {i}) - I'm just gonna run forever...")

# DON'T RUN THIS - You'll have to kill Python.exe from Task Manager
# You're unable to use CTRL+C to break this loop
# i = 0
# while True:
#     try:
#         i += 1
#         print(f"(iteration {i}) I'm just gonna run forever...")
#     except:
#         pass

# Use CTRL+C to break this loop
# i = 0
# while True:
#     try:
#         i += 1
#         print(f"(iteration {i}) - I'm just gonna run forever...")
#     except KeyboardInterrupt:
#         print("OK... I'll stop... :(")
#         break
#     except Exception as ex:
#         print(ex)
#         pass
