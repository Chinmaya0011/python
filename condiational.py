# conditional_statements.py
# This file demonstrates various conditional statements in Python with comments and examples.

# 1. Grading System Based on Marks
mark = int(input("Enter your marks: "))  # Input: Marks as integer

if mark > 90:
    print("Grade A")  # Marks > 90
elif mark > 80 and mark <= 90:
    print("Grade B")  # Marks between 81 and 90
elif mark > 70 and mark <= 80:
    print("Grade C")  # Marks between 71 and 80
elif mark > 60 and mark <= 70:
    print("Grade D")  # Marks between 61 and 70
elif mark > 50 and mark <= 60:
    print("Grade E")  # Marks between 51 and 60
else:
    print("Failed")  # Marks <= 50

# 2. Driving Eligibility Based on Age
userAge = int(input("Enter your age: "))  # Input: Age as integer

if userAge < 18:
    print("You can't drive and cry in the corner!")  # Not eligible to drive
elif userAge >= 18:
    print("You can drive!")  # Eligible to drive
else:
    print("Enter a valid age.")  # Invalid input

# 3. Check if a Number is Even or Odd
num = int(input("Enter a number: "))  # Input: Number as integer

if num % 2 == 0:
    print(f"{num} is even.")  # If divisible by 2, it's even
else:
    print(f"{num} is odd.")  # Otherwise, it's odd

# 4. Simple Login System
username = "admin"  # Predefined username
password = "1234"  # Predefined password

input_username = input("Enter username: ")  # Input: Username
input_password = input("Enter password: ")  # Input: Password

if input_username == username and input_password == password:
    print("Login successful!")  # Both username and password match
elif input_username != username:
    print("Incorrect username!")  # Username mismatch
elif input_password != password:
    print("Incorrect password!")  # Password mismatch
else:
    print("Login failed!")  # Both credentials are wrong

# 5. Check Membership in String
name = "Chinmaya Kumar Mishra"  # Example name

if "Kumar" in name:
    print("'Kumar' is present in the name.")  # Substring found
else:
    print("'Kumar' is not in the name.")  # Substring not found

# 6. Using Logical Operators
a, b, c = 5, 10, 15  # Example variables

if a < b and b < c:
    print("a < b and b < c is True")  # Both conditions are True
if a < b or b > c:
    print("At least one condition is True")  # One condition is True
if not a > b:
    print("a is not greater than b")  # Negated condition

# 7. Identity Operator Example
x = [1, 2, 3]
y = [1, 2, 3]
z = x  # z refers to the same object as x

print("x is y:", x is y)  # Output: False (Different objects with same content)
print("x is z:", x is z)  # Output: True (Same object)

# 8. Assignment Operators
num = 10  # Assign value 10 to num
print("Initial value:", num)

num += 5  # Add 5 to num (num = num + 5)
print("After += 5:", num)

num -= 3  # Subtract 3 from num (num = num - 3)
print("After -= 3:", num)

num *= 2  # Multiply num by 2 (num = num * 2)
print("After *= 2:", num)

num /= 4  # Divide num by 4 (num = num / 4)
print("After /= 4:", num)

# 9. Bitwise Operators
a = 5  # Binary: 101
b = 3  # Binary: 011

print("a & b:", a & b)  # Output: 1 (Binary: 001)
print("a | b:", a | b)  # Output: 7 (Binary: 111)
print("a ^ b:", a ^ b)  # Output: 6 (Binary: 110)
print("~a:", ~a)  # Output: -6 (Bitwise NOT)
print("a << 1:", a << 1)  # Output: 10 (Left shift)
print("a >> 1:", a >> 1)  # Output: 2 (Right shift)

# 10. Membership Operators in Lists
fruits = ["apple", "banana", "mango"]

if "apple" in fruits:
    print("Apple is in the list.")  # Checks if 'apple' is in the list

if "orange" not in fruits:
    print("Orange is not in the list.")  # Checks if 'orange' is not in the list
 