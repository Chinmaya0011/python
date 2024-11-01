# a=41
# b=5
# c=6
# if(a>b and a>c):
#     print("A is greater")
# elif(b>a and b>c):
#     print("B is Greater")
# else:
#     print("C is Greater")
# num=77
# if(num%7==0):
#     print("Divisible")
# else:
#     print("No Divisible")
# arr=[1,"chinu",2]
# arr.insert(2,"c")
# print(arr)

# Dictionary Example
# A dictionary to store student information
students = {
    "Name": "Chinmaya Kumar Mishra",
    "RollNo": 1234,
    "College": "PMEC",
    "Class": "B.tech",
    "Branch": "Civil",
}

# 1. Printing the dictionary
print("Student Information:", students)

# 2. Clearing the dictionary
students.clear()  # Removes all entries from the dictionary
print("After clearing, students dictionary:", students)  # Output: {}

# Set Example
# Creating two sets of fruits and vegetables
fruits = {"apple", "orange", "banana", "grapes"}
veg = {"potato", "tomato", "onion"}

# 3. Performing symmetric difference operation
symmetric_difference = fruits ^ veg  # Elements in either set but not both
print("Symmetric Difference between fruits and veg:", symmetric_difference)

# Q&A
# Q1: What is the purpose of a dictionary in Python?
# A1: A dictionary stores data in key-value pairs. Each key is unique, allowing for efficient data retrieval.

# Q2: What type of data can be stored as values in a dictionary?
# A2: Values can be strings, integers, lists, or any other data type.

# Q3: What does the `students.clear()` method do?
# A3: It removes all key-value pairs from the dictionary.

# Q4: What is a set in Python?
# A4: A set is an unordered collection of unique elements and does not allow duplicates.

# Q5: What does `print(fruits ^ veg)` do?
# A5: It calculates the symmetric difference, returning a set of elements in either set but not both.

# Q6: What will the output of `print(fruits ^ veg)` be?
# A6: It will output a set of distinct elements from both fruits and vegetables.

# Q7: Can a set contain mutable elements?
# A7: No, sets cannot contain mutable elements like lists or dictionaries.

# Q8: What happens if you add a duplicate fruit to the set?
# A8: The set remains unchanged because it ignores duplicate values.

# Q9: How to convert a list with duplicates into a set?
my_list = ['apple', 'banana', 'apple', 'orange']
my_set = set(my_list)  # Converts the list to a set, removing duplicates
print("Converted set from list:", my_set)  # Output: {'apple', 'banana', 'orange'}

# Q10: Common operations on sets include:
# - Union: Combining two sets
# - Intersection: Finding common elements
# - Difference: Elements in one set but not the other
# - Symmetric Difference: Elements in either set but not both
