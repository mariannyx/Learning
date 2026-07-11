print("\n===== 1. Strings =====\n")

# Ordered, immutable, text representation, avoid errors
language = "Python"

# Number of characters
print(language + " has " + str(len(language)) + " letters")

# Acess to a specific element / character
print("It also has letter: " + language[-1])

# Slice text
# Default value is 0
print("And this is part of it: " + language[:2])


print("\n===== 2. Formatted String =====\n")

# Set / assign a value to a variable
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


print("\n===== 4. Conversion =====\n")

text = "I am a teacher"
print(f"Example: {text}")

# Convert a string to a list
my_list = text.split(" ")
print(f"List: {my_list}")

# Convert a list to a string
my_string = " ".join(my_list)
print(f"String: {my_string}")

# Convert a word to a list of letters
letters = list(text)
print(f"Letters: {letters}")
