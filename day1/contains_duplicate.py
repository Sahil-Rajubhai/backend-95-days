def contains_duplicate(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 3, 2]
print(contains_duplicate(numbers))

# Space = O(n)
# Time = 0(n)