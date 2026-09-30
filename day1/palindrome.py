def palindrome(text):
    if not text: 
        return

    text = text.strip().lower()
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

tests = ["Madam", "RaceCar", "Python"]
for test in tests:
    print(palindrome(test))

# Space = O(1)
# Time = 0(n)