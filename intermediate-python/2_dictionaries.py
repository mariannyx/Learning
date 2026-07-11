print("\n===== 1. Dictionaries =====\n")

# Key-value pairs, ordered, mutable
# Each key-value pair maps a key to its associated value
student = {"name": "Vasilko", "school": "Robocode", "age": 12, "is_active": True}
print(f"Student: {student}")

# Delete a key
del student["is_active"]
print(f"\nAfter removing a key: {student}")

# Another way to do it
student.pop("name")
print(f"After removing one more key: {student}")

# Remove the last inserted item
student.popitem()
print(f"After deleting the last inserted item: {student}")

# Remove all item
# student.clear()
# print(student)

# Another way to create a dictionary
# Also we can use numbers and tuples as a key
# Actually, any immutable type is suitable
new_student = dict(name="Vasylko", age=12, is_active=True)
print(f"\nNew student: {new_student}")

# Loop through keys
print("\nIts keys: ")
for key in new_student:
    print(key, end=" ")

# Loop through values
print("\n\nIts values: ")
for value in new_student.values():
    print(value, end=" ")

# Loop through key-value pairs
print("\n\nIts key-value pairs: ")
for key, value in new_student.items():
    print(f"{key}: {value}", end=" ")

# Best ways to create a copy
new_student_copy = new_student.copy()
# new_student_copy = dict(new_student)
print(f"\n\nCopy of new student: {new_student_copy}")

# Merge dictionaries
# Old values will be overwritten and new pairs will be added
student.update(new_student_copy)
print(f"Merged student: {student}")
