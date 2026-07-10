print("\n===== 1. Modules =====\n")

# Module is basically a file with some pythom code
# We use it to organize our code
import stats

# Import a specific part of a module
# ctrl + space to check all its parts
from stats import avg

from pathlib import Path

# Alias
import random as rnd
from collections import deque

list = [5, 0, -14, 7, -3]
print(f"List: {list}")
print(f"Max: {stats.max(list)}")
print(f"Min: {stats.min(list)}")

# We don't need to prefix it
print(f"Avg: {avg(list)}")
print(f"Avg of empty list: {avg(list.clear())}")

# We can randomly pick an item of a list
dogs = ["Daisy", "Cherry", "Baron"]
print(f"\nDogs: {dogs}")
print(f"It's {rnd.choice(dogs)}'s nameday")

# Package is a container for multiple modules
# To covert directory into package we should add file __init__.py

# PyPI(Python Package Index) has many packages for different tasks
# pip is a tool used to install or unistall packages from pypi.org


print("\n===== 2. Path =====\n")

# We can type out a file or directory as a string
dir = "party"
path = Path(dir)

# Check for existence of path
if not path.exists():
    # Create a new directory
    path.mkdir()
    print(path.exists())

# Remove a directory
path.rmdir()
print(path.exists())

# If you don't pass an argument here
# This will reference the current directory
origin_path = Path()

# Search for files and directories
# * - all files and dirs, *.* - only files
for file in origin_path.glob("*.py"):
    print(file)


print("\n===== 3. Task: create a dice game =====\n")


class Dice:
    def __init__(self):
        self.history = deque(maxlen=5)

    # Method called roll
    def roll(self):
        result = rnd.randint(1, 6)
        self.history.append(result)

        # Finally we need to return the result
        return result

        # Pythom will automatically interpret this as a tuple
        # return result, result

    def get_history(self):
        return list(self.history)


dice = Dice()

while True:
    message = input("\nRoll(r), history(h) or quit(q): ")
    if message.lower() == "r":
        print(f"You got: {dice.roll()}")
    elif message.lower() == "h":
        print(f"Dice history: {dice.get_history()}")
    elif message.lower() == "q":
        print("Smell ya later!")
        break
    else:
        print("Looks like a misclick ;)")
