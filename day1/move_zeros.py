def move_zeros(numbers):
    if not numbers:
        return

    i = 0
    j = 0
    while j < len(numbers):
        if numbers[j] != 0:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
        j += 1
    return numbers

print(move_zeros([0, 1, 0, 3, 12]))     

# Space = O(1)
# Time = 0(n)