# Define a function to add all elements in a list
def add_all_numbers(numbers):
    """
    This function adds all the numbers in a list using different methods.
    :param numbers: list of numbers to add
    :return: sum of all numbers in the list
    """

    # Method 1: Using a loop
    sum_with_loop = 0  # Initialize sum
    for num in numbers:
        sum_with_loop += num  # Add each number to the sum
    print("Sum using loop:", sum_with_loop)

    # Method 2: Using the built-in sum() function
    sum_with_sum_function = sum(numbers)  # Sums up all elements in the list
    print("Sum using sum() function:", sum_with_sum_function)

    # Method 3: Using reduce() function from functools module (without lambda)
    from functools import reduce
    
    # Define a function to add two numbers
    def add(x, y):
        return x + y
    
    # Use the add function with reduce
    sum_with_reduce = reduce(add, numbers)  # Reduces the list by adding each pair of numbers
    print("Sum using reduce() function:", sum_with_reduce)

    # Method 4: Using list comprehension and sum()
    sum_with_comprehension = sum([num for num in numbers])  # List comprehension to iterate over numbers
    print("Sum using list comprehension:", sum_with_comprehension)

    return sum_with_sum_function  # Return one of the results


# Example usage
numbers_list = [1, 2, 3, 4, 5]
total_sum = add_all_numbers(numbers_list)
print("Total sum:", total_sum)
