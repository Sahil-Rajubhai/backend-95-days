def second_largest(numbers):
    if not numbers:
        return
    
    f_largest = None
    s_largest = None

    for num in numbers:
        if f_largest is None or num > f_largest:
            s_largest = f_largest
            f_largest = num
        elif num != f_largest and (s_largest is None or num > s_largest):
            s_largest = num
    return s_largest

print(second_largest([5,5,5]))