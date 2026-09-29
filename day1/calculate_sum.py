def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
result = calculate_sum(numbers)
print(f"The sum of the numbers in the list is: {result}")