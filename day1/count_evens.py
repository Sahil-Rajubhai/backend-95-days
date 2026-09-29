def count_evens(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
result = count_evens(numbers)
print(f"The count of even numbers in the list is: {result}")