# Definition of Loops
# A loop in programming is a control structure that allows code to be executed repeatedly based on a condition or a range of values.
# Loops are fundamental in programming for tasks that require repeated execution of code blocks, such as iterating through collections,
# performing repetitive calculations, or automating repetitive tasks.

# Types of Loops in Python
# Python primarily has two types of loops:
# 1. for loop: Iterates over a sequence (like a list, tuple, dictionary, set, or string) or a range of numbers.
# 2. while loop: Repeats a block of code as long as a specified condition is true.

# Usages of Loops

# 1. for Loop
# Usage: Used when you know the number of iterations in advance or need to iterate over a collection.
for i in range(11):  # Iterates from 0 to 10
    if(i == 0):      # Skips the number 0
        continue
    print(i)        # Prints numbers from 1 to 10

# 2. while Loop
# Usage: Used when the number of iterations is not known beforehand and depends on a condition.
i = 0
while(i <= 20):      # Continues until i is greater than 20
    print(i)        # Prints numbers from 0 to 20
    i += 1          # Increments i by 1

# 3. Breaking Out of a Loop
# Usage: The break statement is used to exit a loop prematurely when a condition is met.
for i in range(10):
    if(i == 5):      # Stops the loop when i equals 5
        break
    print(i)        # Prints numbers from 0 to 4

# 4. Skipping an Iteration
# Usage: The continue statement skips the current iteration and moves to the next iteration.
for i in range(1, 10):
    if(i % 2 != 0):  # Skips odd numbers
        continue
    print(i)        # Prints even numbers from 1 to 9

# 5. Using range()
# Usage: The range() function generates a sequence of numbers, often used in for loops to specify iterations.
for i in range(5, 16):  # Prints numbers from 5 to 15
    print(i)

# 6. Nested Loops
# Usage: Allows you to loop through a set of items within another loop.
for i in range(1, 6):
    for j in range(1, 11):  # Prints multiplication table from 1 to 5
        print(i * j)

# 7. Counting Down with a While Loop
# Usage: A while loop can also count down by decreasing the loop variable.
i = 10
while(i >= 1):      # Counts down from 10 to 1
    print(i)
    i -= 1

# 8. Calculating a Sum
# Usage: Loops can be used to accumulate values, such as calculating the sum of a range of numbers.
sum = 0
for i in range(1, 100):  # Calculates the sum of numbers from 1 to 99
    sum += i

print(sum)              # Prints the total sum
