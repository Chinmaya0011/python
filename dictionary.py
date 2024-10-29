# Creating a dictionary to store information about a person
person = {
    'name': 'Alice',   # Key 'name' with value 'Alice'
    'age': 25,         # Key 'age' with value 25 (integer)
    'city': 'New York' # Key 'city' with value 'New York'
}

# Printing the entire dictionary
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing the value of a specific key (name)
print(person['name'])  # Output: Alice

# Adding a new key-value pair to the dictionary
person['job'] = 'Engineer'  # Adds 'job': 'Engineer'
print(person)  
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}

# Modifying the value of an existing key (age)
person['age'] = 26  # Updates the value of 'age' to 26
print(person['age'])  # Output: 26

# Deleting a key-value pair (city)
del person['city']  # Removes the 'city' key and its value
print(person)  
# Output: {'name': 'Alice', 'age': 26, 'job': 'Engineer'}

# Looping through the dictionary to print all keys and values
for key, value in person.items():
    print(key + ':', value)  
# Output:
# name: Alice
# age: 26
# job: Engineer
