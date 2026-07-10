print("\n# ===== 1. Comparison operators =====\n")

# > - greater, < - less
# != - not equal, == - equality operator
print(f"meat > apple: {"meat" > "apple"}")

# Numeric representation
print(f"'m' is: {ord("m")} \n'a' is: {ord("a")}")


print("\n# ===== 2. Conditional statements =====\n")

# Set / assign a number to a variable
temperature = 19
print(f"temperature: {temperature}")

if temperature >= 25:
    print("It's pretty hot")
elif temperature >= 20:
    print("It's OK")
else:
    print("Where is the sun?")

# Ternary operator
message = "Warm" if temperature >= 20 else "Cold"
print("It's really " + message)


print("\n# ===== 3. Logical operators =====\n")

tall = True
rich = False

# and - both, or - at least one, not - inverse value
if tall and rich:
    print("Looks like you are tall and rich")
    print("So... Will you marry me?")
elif tall or rich:
    print("We will talk after you...")
    if not rich:
        print("find a better job")
    else:
        print("actually never")

# Chaining comparison operators
if 5 < 10 < 15:
    print("\nActually, 5 < 10 and 10 < 15")


# Short circuit - evaluation stops as soon as...
# we get False in "and" or True in "or"
