print("\n# ===== 1. For Loops =====\n")

import random

# Type of range is range
print(type(range(5)))
print()

# Iterable objects: range, string and list
# Iteration means repeating steps
for i in range(5):
    print(f"Hi{"!" * i}")


print("\n# ===== 2. While Loops =====\n")

# While works as long as a condition is True
while True:
    command = input("What should I do? ")
    if command.lower() != "stop":
        print("Sorry, I can't " + command)
        print("Actually, all I can do is stop")
    else:
        # terminate loop
        break


print("\n# ===== 3. Nested loops =====\n")

size = 7

# Outer and inner loops
for x in range(size):
    for y in range(size):
        if x <= y and x + y < size:
            print("-", end="")
        elif x >= y and x + y >= size - 1:
            print("-", end="")
        else:
            print(" ", end="")
    print()
