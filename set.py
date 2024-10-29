# 1. Creating a set with unique elements
fruits = {'apple', 'banana', 'orange'}
print(f"Initial set: {fruits}")  # Output: {'apple', 'banana', 'orange'}

# 2. Adding an element to the set
fruits.add('grape')  # Adds 'grape' to the set
print(f"After adding 'grape': {fruits}")  # Output: {'apple', 'banana', 'orange', 'grape'}

# 3. Trying to add a duplicate element (it will be ignored)
fruits.add('apple')
print(f"After adding duplicate 'apple': {fruits}")  # Output: {'apple', 'banana', 'orange', 'grape'}

# 4. Removing an element
fruits.remove('banana')  # Removes 'banana' from the set
print(f"After removing 'banana': {fruits}")  # Output: {'apple', 'orange', 'grape'}

# 5. Using discard (no error if element is not present)
fruits.discard('pineapple')  # No error, even though 'pineapple' is not in the set

# 6. Checking membership
print(f"Is 'orange' in the set? {'orange' in fruits}")  # Output: True
print(f"Is 'banana' in the set? {'banana' in fruits}")  # Output: False

# 7. Creating two new sets for operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 8. Performing set operations
union_set = set1 | set2  # Union of set1 and set2
print(f"Union: {union_set}")  # Output: {1, 2, 3, 4, 5}

intersection_set = set1 & set2  # Intersection of set1 and set2
print(f"Intersection: {intersection_set}")  # Output: {3}

difference_set = set1 - set2  # Elements in set1 but not in set2
print(f"Difference: {difference_set}")  # Output: {1, 2}

symmetric_difference_set = set1 ^ set2  # Elements in either set, but not both
print(f"Symmetric Difference: {symmetric_difference_set}")  # Output: {1, 2, 4, 5}

# 9. Looping through a set
print("Looping through the 'fruits' set:")
for fruit in fruits:
    print(fruit)
# Output:
# apple
# orange
# grape
