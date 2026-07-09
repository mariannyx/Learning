print("\n# ===== 1. Numbers =====\n")

# Import a module
import math

# Get an integer, // - double slash
print(f"10 // 3 = {10 // 3}")

# Remainder of division, % - percent
print(f"10 % 3 = {10 % 3}")

# Rounding a number
print(f"\nround(2.7): {round(2.7)}")

# Ceiling of a number
print(f"math.ceil(2.2): {math.ceil(2.2)}")

# Absolute value
print(f"abs(-5): {abs(-5)}")


print("\n# ===== 2. Type conversion =====\n")

# Get input from the user
x = input("x: ")

# Built-in function that returns type of an object
print(f"Type of x: {type(x)}")

# Convert to an integer
x = int(x) + 2
print(f"\nx + 2 = {x}")

# Augmented assignment operator
x += 5
print(f"x += 5: {x}")

# Falsey values: "", 0, None
# Anything that is not falsey is considered Truthy
