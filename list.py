# Definition of List:
# A list is a built-in data structure in Python that holds an ordered collection of items. 
# Lists are mutable, which means you can change their contents without changing their identity. 
# They can contain elements of different data types, including integers, floats, strings, and even other lists.

# Creating a list with different data types
arr = [1, "chinu", 2.3]  # A list containing an integer, a string, and a float

# 1. Accessing Elements:
# Accessing the second element in the list (index starts at 0)
print("Second element:", arr[1])  # Output: "chinu"

# 2. Modifying Elements:
# Modifying the first element
arr[0] = 5  # Changing the first element to 5
print("After modifying first element:", arr)  # Output: [5, "chinu", 2.3]

# 3. Adding Elements:
# Adding a new element to the end of the list
arr.append("new element")
print("After adding new element:", arr)  # Output: [5, "chinu", 2.3, "new element"]

# 4. Removing Elements:
# Removing an element from the list
arr.remove("chinu")  # Removing the element "chinu"
print("After removing 'chinu':", arr)  # Output: [5, 2.3, "new element"]

# 5. Slicing Lists:
# Slicing the list to get a sublist
sublist = arr[1:3]  # Getting elements from index 1 to 2
print("Sublist (index 1 to 2):", sublist)  # Output: [2.3, "new element"]

# 6. Finding the Length:
# Finding the length of the list
print("Length of the list:", len(arr))  # Output: 3

# 7. Sorting the List:
# Sorting a list with numeric values
numeric_list = [5, 2, 9, 1]
numeric_list.sort()  # Sorts the list in ascending order
print("Sorted numeric list:", numeric_list)  # Output: [1, 2, 5, 9]

# 8. Reversing the List:
# Reversing the order of elements in the list
arr.reverse()
print("Reversed list:", arr)  # Output will depend on the current state of arr

# 9. Extending the List:
# Extending the list with another list
arr.extend([100, 200])
print("List after extending with [100, 200]:", arr)  # Output: [.., 100, 200]

# 10. Inserting Elements:
# Inserting an element at a specific index
arr.insert(1, "inserted element")  # Inserting at index 1
print("After inserting at index 1:", arr)  # Output will depend on the current state of arr

# 11. Counting Occurrences:
# Counting how many times an element appears in the list
print("Count of 5 in arr:", arr.count(5))  # Output: number of times 5 appears in arr

# 12. Copying the List:
# Creating a shallow copy of the list
copied_list = arr.copy()
print("Copied list:", copied_list)

# 13. Clearing the List:
# Clearing all elements from the list
arr.clear()
print("After clearing the list:", arr)  # Output: []
