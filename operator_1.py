# Arithmetic Operators
num1 = 12
num2 = 5
print("Arithmetic Operators:")
print("Addition:", num1 + num2)  # 17
print("Subtraction:", num1 - num2)  # 7
print("Multiplication:", num1 * num2)  # 60
print("Division:", num1 / num2)  # 2.4
print("Modulus:", num1 % num2)  # 2
print("Floor Division:", num1 // num2)  # 2
print("Exponentiation:", num1 ** num2)  # 248832

print("\nComparison Operators:")
print("Equal:", num1 == num2)  # False
print("Not Equal:", num1 != num2)  # True
print("Greater Than:", num1 > num2)  # True
print("Less Than:", num1 < num2)  # False
print("Greater or Equal:", num1 >= num2)  # True
print("Less or Equal:", num1 <= num2)  # False

print("\nLogical Operators:")
a = True
b = False
print("AND:", a and b)  # False
print("OR:", a or b)  # True
print("NOT a:", not a)  # False

print("\nBitwise Operators:")
x = 5  # 0101 in binary
y = 3  # 0011 in binary
print("Bitwise AND:", x & y)  # 1 (0001)
print("Bitwise OR:", x | y)  # 7 (0111)
print("Bitwise XOR:", x ^ y)  # 6 (0110)
print("Bitwise NOT (~x):", ~x)  # -6 (inverts all bits)
print("Left Shift:", x << 1)  # 10 (1010)
print("Right Shift:", x >> 1)  # 2 (0010)

print("\nAssignment Operators:")
z = 10
print("Initial Value:", z)  # 10
z += 5
print("After += 5:", z)  # 15
z -= 3
print("After -= 3:", z)  # 12
z *= 2
print("After *= 2:", z)  # 24
z /= 4
print("After /= 4:", z)  # 6.0
z //= 2
print("After //= 2:", z)  # 3.0
z **= 3
print("After **= 3:", z)  # 27.0

print("\nIdentity Operators:")
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("a is b:", a is b)  # True (same object)
print("a is not c:", a is not c)  # True (different objects)

print("\nMembership Operators:")
print("2 in a:", 2 in a)  # True
print("4 not in a:", 4 not in a)  # True
