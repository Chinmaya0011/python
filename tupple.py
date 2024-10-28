# Definition of Tuple:
# A tuple is a built-in data structure in Python that holds an ordered collection of items, similar to a list.
# The key difference is that tuples are immutable, meaning once they are created, their contents cannot be changed.
# Tuples can contain elements of different data types, including integers, floats, strings, and even other tuples.

# Creating a tuple with different data types
my_tuple = (1, "chinu", 2.3)  # A tuple containing an integer, a string, and a float

# 1. Accessing Elements:
# Accessing the second element in the tuple (index starts at 0)
print("Second element:", my_tuple[1])  # Output: "chinu"

# 2. Length of the Tuple:
# Finding the length of the tuple
print("Length of the tuple:", len(my_tuple))  # Output: 3

# 3. Slicing Tuples:
# Slicing the tuple to get a sub-tuple
sub_tuple = my_tuple[1:3]  # Getting elements from index 1 to 2
print("Sub-tuple (index 1 to 2):", sub_tuple)  # Output: ("chinu", 2.3)

# 4. Concatenating Tuples:
# Concatenating two tuples
another_tuple = (4, 5)
combined_tuple = my_tuple + another_tuple
print("Combined tuple:", combined_tuple)  # Output: (1, "chinu", 2.3, 4, 5)

# 5. Repeating Tuples:
# Repeating elements in a tuple
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)  # Output: (1, "chinu", 2.3, 1, "chinu", 2.3)

# 6. Checking Membership:
# Checking if an element exists in the tuple
print("Is 'chinu' in my_tuple?", "chinu" in my_tuple)  # Output: True
print("Is 4 in my_tuple?", 4 in my_tuple)  # Output: False

# 7. Counting Occurrences:
# Counting how many times an element appears in the tuple
count_1 = my_tuple.count(1)  # Count occurrences of 1
print("Count of 1 in my_tuple:", count_1)  # Output: 1

# 8. Finding Index:
# Finding the index of the first occurrence of an element
index_of_chinu = my_tuple.index("chinu")
print("Index of 'chinu':", index_of_chinu)  # Output: 1

# 9. Nested Tuples:
# Creating a tuple that contains another tuple
nested_tuple = (my_tuple, another_tuple)
print("Nested tuple:", nested_tuple)  # Output: ((1, "chinu", 2.3), (4, 5))

# 10. Converting a List to a Tuple:
# Converting a list to a tuple
my_list = [10, 20, 30]
tuple_from_list = tuple(my_list)
print("Tuple from list:", tuple_from_list)  # Output: (10, 20, 30)

# 11. Unpacking Tuples:
# Unpacking tuple elements into variables
x, y, z = my_tuple
print("Unpacked values:", x, y, z)  # Output: 1 "chinu" 2.3

# 12. Tuples are Immutable:
# Trying to modify an element in the tuple will raise an error
try:
    my_tuple[0] = 100  # Attempting to change the first element
except TypeError as e:
    print("Error:", e)  # Output: 'tuple' object does not support item assignment
