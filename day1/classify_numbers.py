def classify_numbers(numbers):
    positive = negative = zero = even = odd = 0
    for num in numbers:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
        
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return positive, negative, zero, even, odd  

# Example usage:
numbers = [1, -2, 0, 3, -4, 5, 6]
positive, negative, zero, even, odd = classify_numbers(numbers)
print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Zeroes: {zero}")        
print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")