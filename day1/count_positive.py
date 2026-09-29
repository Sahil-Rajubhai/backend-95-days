def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

# Example usage:
result = count_positive([-2, 5, 7, -1, 0, 4])
print(f"The count of positive numbers in the list is: {result}")