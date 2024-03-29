# Check if the first and last number of a list is the same

# Function: check_first_last_same
def check_first_last_same(numbers):

    # Get the first number from the list
    first_number = numbers[0]

    # Get the last number from the list
    last_number = numbers[-1]

    # Check if the first and last numbers are the same
    if first_number == last_number:
        # If same, return True
        return True
    else:
        # If different, return False
        return False
    
# Given 1
numbers_1 = [88, 45, 37, 62, 88, 90]
print(f"Given list: ", numbers_1)
print(f"The result is ", check_first_last_same(numbers_1))

# Given 2
numbers_2 = [75, 38, 24, 12]
print(f"Given list: ", numbers_2)
print(f"The result is ", check_first_last_same(numbers_2))

# Given 3
numbers_3 = [27, 7, 13, 65, 93, 27]
print(f"Given list: ", numbers_3)
print(f"The result is ", check_first_last_same(numbers_3))