print("\n===== 1. Sets =====\n")

# Unordered, mutable, no duplicates
my_set = {1, 2, 3, 2, 1}
print(f"My set: {my_set}")

# Add an element
my_set.add(4)
print(f"After adding an elem: {my_set}")

# Remove an element
# Warning: May raise KeyError
my_set.remove(1)
print(f"After removing an elem: {my_set}")

# Safe alternative
my_set.discard(67)

# Arbitrary remove an element ;)
print(f"\nArbitrary removing: {my_set.pop()}")
print(f"And result of it: {my_set}")

# Remove all elements
my_set.clear()
print(f"After clearing: {my_set}")


print("\n===== 2. Operations =====\n")

# Another way to create a set
apple_set = set("apple")
print(f"Apple set: {apple_set}")

banana_set = set("banana")
print(f"Banana set: {banana_set}")

# Combines elems from borh sets without duplication
fruit_set = apple_set.union(banana_set)
print(f"\nUnion: {fruit_set}")

# Calculate the intersection of sets
inter = apple_set.intersection(banana_set)
print(f"Intersection: {inter}")

# All elems from the first set that are not in the second set
diff = apple_set.difference(banana_set)
print(f"Difference: {diff}")

# Elements found in A or B, but not in both
sym_diff = apple_set.symmetric_difference(banana_set)
print(f"Symmetric diff: {sym_diff}")

# intersection and differences have _update methods
# which allows assigning a result to the first set

# Add elems from the second set
sym_diff.update(apple_set)
print(f"Update: {sym_diff}")

# Immutable version of a normal set
six_seven = frozenset([6, 7])
print(f"\nImmutable legend: {six_seven}")

# AttributeError
# six_seven.add(8)
