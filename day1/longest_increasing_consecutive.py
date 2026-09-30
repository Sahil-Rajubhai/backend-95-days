def longest_increasing_consecutive_run(numbers):
    if not numbers:
        return

    i = 0
    j = 1
    max_run = 1
    current_run = 1

    while j < len(numbers):
        if numbers[i] + 1 == numbers[j]:
            current_run += 1
            max_run = max(max_run,current_run)
        else:
            current_run = 1
        i += 1
        j += 1
    return max_run

print(longest_increasing_consecutive_run([1, 2, 3, 2, 3, 4, 5, 1]))
print(longest_increasing_consecutive_run([5, 4, 3, 2]))