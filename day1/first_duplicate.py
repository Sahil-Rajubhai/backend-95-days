def first_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return num
        seen.add(num)
    return None  # Return None if there are no duplicates

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 3, 2]
result = first_duplicate(numbers)
if result is not None:
    print(f"The first duplicate number in the list is: {result}")