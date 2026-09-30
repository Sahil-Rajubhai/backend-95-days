def max_consecutive_1_s(numbers):
    if not numbers:
        return

    max_1_s = 0
    current_1_s = 0
    for  num in numbers:
        if num == 1:
            current_1_s += 1
        else:
            max_1_s = max(max_1_s,current_1_s)
            current_1_s = 0
    return max_1_s

print(max_consecutive_1_s([1, 1, 0, 1, 1, 1, 0, 1]))

# Space = O(1)
# Time = 0(n)