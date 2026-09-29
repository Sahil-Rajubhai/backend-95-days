def contains(numbers, target):
    for num in numbers:
        if num == target:
            return True
    return False    

# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
target = 4
result = contains(numbers, target)
if result:
    print(f"The target number {target} is present in the list.")
else:
    print(f"The target number {target} is not present in the list.")