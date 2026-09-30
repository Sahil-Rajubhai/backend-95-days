def most_frequent_number(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1

    max_frequency = 0
    most_frequent = None
    for key, value in freq.items():
        if value > max_frequency:
            max_frequency = value
            most_frequent = key
    return most_frequent

print(most_frequent_number([4,1,7,4,9,1,4]))
    
# Space = O(n)
# Time = 0(n)
