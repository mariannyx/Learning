print("\n===== 1. Strings =====\n")

# Set / assign a value to a variable
language = "Python"

# Number of characters
print(language + " has " + str(len(language)) + " letters")

# Acess to a specific element / character
print("It also has letter: " + language[-1])

# Slice, : - colon
# Default value is 0
print("And we can cut it into: " + language[:2])


print("\n===== 2. Formatted String =====\n")

first_name = "Marian"
last_name = "Moh"

# Concatenation
full = first_name + " " + last_name
print("We can concatenate: " + full)

# Expression, {} - curly braces
full = f"{first_name} {last_name}"
print("Or use formatted: " + full)


print("\n===== 3. String Methods =====\n")

school = " Robocode   "

# Remove extra spaces, we also have - lstrip() and rstrip()
school = school.strip()
print("Clear string: " + school)

# Find index of the character(s), -1 - not found
print(f"An index of 'code': {school.find("code")}")

# Replace all character(s)
print(f"Replace o with F: {school.replace("o", "F")}")

# Check for the existence
print(f"Is 'Robo' part of the word: {"Robo" in school}")

# Does not contain the character(s)
print(f"Is 'Beer' not part of the word: {"Beer" not in school}")
