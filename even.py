def is_even(num):
    """Returns True if the number is even, False otherwise."""
    return num % 2 == 0
print(is_even(4))  # Output: True
#write the edge cases for the above code
print(is_even(0))  # Output: True (0 is considered even)
print(is_even(-2)) # Output: True (negative even number)
print(is_even(3))  # Output: False (odd number)
print(is_even(-1)) # Output: False (negative odd number)

#write teh code using teh exception handling
def is_even(num):
    """Returns True if the number is even, False otherwise."""
    try:
        if not isinstance(num, int):
            raise ValueError("Input must be an integer.")
        return num % 2 == 0
    except ValueError as e:
        print(e)
        return None
print(is_even(4))  # Output: True