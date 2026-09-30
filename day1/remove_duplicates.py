def remove_dupicates(numbers):
    if not numbers:
        return 

    i = 0
    j = 0
    while j < len(numbers):
        if numbers[i] != numbers[j]:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
        j += 1
    return numbers[:i +1]

print(remove_dupicates([1,1,2,2,3,3,4]))