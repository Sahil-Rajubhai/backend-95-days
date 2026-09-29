def find_min(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    min_num = numbers[0]
    for num in numbers[1:]:
        if num < min_num:
            min_num = num
    return min_num

# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
result = find_min(numbers)
print(f"The minimum number in the list is: {result}")
           