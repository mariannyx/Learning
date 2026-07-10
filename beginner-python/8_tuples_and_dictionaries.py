print("\n===== 1. Tuples =====\n")

# Immutable list
coordinates = (5, 0, -2)

# Unpacking - assign tuple / list to the variables
x, y, z = coordinates
print(f"Coordinates: {x}, {y}, {z}")


print("\n===== 2. Dictionaries =====\n")

# Key value pairs
# Each key should be unique
student = {"name": "Vasylko", "age": 12, "is_active": True}

# Return a value associated with this key
print(f"Name: {student["name"]}")

# KeyError
# print(student["brawl_trophies"])

# Check for key existence
print(f"Brawl trophies: {student.get("brawl_trophies")}")

# Supply a default value
print(f"After checking: {student.get("brawl_trophies", 10_000)}")

# Add or change a key value pair
student["brawl_trophies"] = 40_000
print(f"And again: {student.get("brawl_trophies")}")


print("\n===== 3. Task: convert numbers into words =====\n")

names_of_digits = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

number = input("Enter a number: ")
number_words = ""

for digit in number:
    number_words += names_of_digits.get(digit, "!") + " "

print(number_words)
