def find_max(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
result = find_max(numbers)
print(f"The maximum number in the list is: {result}")
    