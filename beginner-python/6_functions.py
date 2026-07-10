print("\n# ===== 1. Functions =====\n")


# 1 - Perform a task
# Parameter it's input that you define for your function
def greet(name):
    print("Hello", name)


# 2 - Return a value
# Optinal parameter has to be at the end
def get_greet(name="John"):
    return f"Hello {name}"


# Argument - actual value for a given parameter
# By default we use positional arguments
greet("Marian")

# With returned value we can do whatever we want
print(get_greet())

# With keyword argument the position doesn't really matter
# Also it improves the readability of our code
greet(name="Oleg")


print("\n# ===== 2. None and xargs =====\n")

# None is an object that represents absence of a value
print(f"All functions by default return : {greet("Ivan")}")


# Collection of arguments works as a tuple
def add(*numbers):
    amount = 0
    for number in numbers:
        amount += number

    return amount


print(f"\nadd(1, 2, 3, 4): {add(1, 2, 3, 4)}")
