print("\n===== 1. Strings =====\n")

# Set / assign a value to a variable
language = "Python"

# Number of characters
print(language + " has " + str(len(language)) + " letters")

# Acess to specific element / character
print("It also has letter: " + language[-1])

# Slice, : - colon
# Default value is 0
print("And we can cut it into: " + language[:2])


print("\n===== 2. Formatted String =====\n")

first_name = "Marian"
last_name = "Moh"

# Concatenation
full = first_name + " " + last_name
print("We can cocatenate: " + full)

# Expression, {} - curly braces
full = f"{first_name} {last_name}"
print("Or use formatted: " + full)


print("\n===== 3. String Methods =====\n")

school = " Robocode   "

# Remove extra spaces, we also have - lstrip() and rstrip()
school = school.strip()
print("Clear string: " + school)

# Find index of character(s), -1 - not found
print("An index of 'code': " + str(school.find("code")))

# Replace all character(s)
print("Replace o with F: " + school.replace("o", "F"))

# Check for the existance
print("Is 'Robo' part of the word: " + str("Robo" in school))

# Does not contain character(s)
print("Is 'Beer' not part of the word: " + str("Beer" not in school))
