print("\n===== 1. Exceptions =====\n")

# Handle errors in python programs with try block
# 0 always means success and anything but 0 means crash
try:
    hours = int(input("Enter your working hours per week: "))
    ratio = 40 / hours
    print(f"Your free time is {ratio} times longer than normal")

# Type of the error that our program may encounter
except ValueError:

    # What should happen if our program encounters this error
    print("Invalid value!")

except ZeroDivisionError:
    print("Looks like you should find it ;)")

# Comments are good, but too much a good thing is a bad thing
