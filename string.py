# String Example
name = "Chinmaya Kumar Mishra"  # A string stored in the variable 'name'

# 1. len() - Get the length of the string
print("Length of the string:", len(name))  # Output: 22
# len() counts the total number of characters, including spaces.

# 2. find() - Find the index of the first occurrence of a substring
str1 = "chinmaya kumar mishra"
print("First occurrence of 'a':", str1.find("a"))  # Output: 5
print("Finding 'z':", str1.find("z"))  # Output: -1 (not found)

# 3. lower() - Convert all characters to lowercase
print("Lowercase:", name.lower())  # Output: chinmaya kumar mishra

# 4. upper() - Convert all characters to uppercase
print("Uppercase:", name.upper())  # Output: CHINMAYA KUMAR MISHRA

# 5. strip() - Remove leading and trailing whitespace
msg = "   Hello World!   "
print("Without leading/trailing spaces:", msg.strip())  # Output: "Hello World!"

# 6. replace() - Replace a substring with another string
print("Replaced 'Kumar' with 'Prasad':", name.replace("Kumar", "Prasad"))  
# Output: Chinmaya Prasad Mishra

# 7. split() - Split the string into a list based on a delimiter (default is space)
words = name.split()  # Splits by spaces
print("Split string into words:", words)  
# Output: ['Chinmaya', 'Kumar', 'Mishra']

# 8. join() - Join a list of strings into a single string with a specified separator
joined_name = "-".join(words)
print("Joined with '-':", joined_name)  
# Output: Chinmaya-Kumar-Mishra

# 9. startswith() - Check if the string starts with a specific substring
print("Starts with 'Chinmaya':", name.startswith("Chinmaya"))  # Output: True

# 10. endswith() - Check if the string ends with a specific substring
print("Ends with 'Mishra':", name.endswith("Mishra"))  # Output: True

# 11. count() - Count occurrences of a substring in the string
print("Count of 'a':", str1.count("a"))  # Output: 3

# 12. capitalize() - Capitalize the first letter of the string
print("Capitalized:", str1.capitalize())  
# Output: Chinmaya kumar mishra

# 13. isalpha() - Check if the string contains only alphabetic characters (no spaces or digits)
print("Is alphabetic:", name.isalpha())  # Output: False (because it contains spaces)

# 14. isdigit() - Check if the string contains only digits
num_str = "12345"
print("Is digit:", num_str.isdigit())  # Output: True

# 15. title() - Convert the string to title case (first letter of each word capitalized)
print("Title Case:", name.title())  # Output: Chinmaya Kumar Mishra

# 16. index() - Find the index of the first occurrence of a substring (raises an error if not found)
print("Index of 'Kumar':", name.index("Kumar"))  # Output: 9
# print(name.index("xyz"))  # Uncommenting this will raise a ValueError

# 17. rfind() - Find the last occurrence of a substring
print("Last occurrence of 'a':", str1.rfind("a"))  # Output: 17

# 18. swapcase() - Swap uppercase to lowercase and vice versa
print("Swapped case:", name.swapcase())  
# Output: cHINMAYA kUMAR mISHRA

# 19. zfill() - Pad the string on the left with zeros to a specified length
num = "42"
print("Zero-padded to 5 digits:", num.zfill(5))  # Output: 00042

# 20. in and not in - Check membership of a substring
print("'Kumar' in name:", "Kumar" in name)  # Output: True
print("'XYZ' not in name:", "XYZ" not in name)  # Output: True
