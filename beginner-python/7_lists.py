print("\n===== 1. Lists =====\n")

# Mutable collection used to store
# multiple items in a single variable
numbers = [3, -4, 0, 7, 1]
print(numbers)

max = numbers[0]
for number in numbers:
    if number > max:
        max = number

print(f"max: {max}")

# 2D (dimensional) - rectangular array
# Each item in this list is another list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using 2 square brackets we can
# access individual items in our matrix
print(f"matrix[1][1]: {matrix[1][1]}")


print("\n===== 2. List Methods =====\n")

team = ["Yura", "Dima"]
print(team)

# Add a new item at the end
team.append("Nastya")
print(team)

# Add a new item anywhere
team.insert(1, "Sofia")
print(team)

# Check for the existence of an item
dima = team.index("Dima")
print(f"Dima is: {dima + 1}th")

# ValueError: item is not in list
# team.index("Ivan")

# Safe version of existence check
print(f"Is Ivan in team: {"Ivan" in team}")

# Get number of a specific item
print(f"How many Marian: {team.count("Marian")}")

# Sorting
team.sort()
print(f"\nSorted: {team}")

# Reverse
team.reverse()
print(f"\nReversed: {team}")

# Copy and create a new independent list
new_team = team.copy()

# Remove the last item
new_team.pop()
print(f"After pop: {new_team}")

# Remove a specific item
new_team.remove("Yura")
print(f"After remove: {new_team}")

# Remove all the items
new_team.clear()
print(f"After clear: {new_team}")

# Check old list
print(f"\nLegends never die: {team}")


print("\n===== 3. Task: remove duplicates in a list =====\n")

list = ["M", 2, "a", 1, True, 4, "M", True, True, "r", 1]
print(f"Origin: {list}")

for item in list:
    if list.count(item) > 1:
        list.remove(item)

print(f"Result: {list}")
