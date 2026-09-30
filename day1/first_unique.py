def first_unique(text):
    if not text:
        return 
    
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    for char in text:
        if freq[char] == 1:
            return char
    return None

tests = ["leetcode", "aabbcc", "aabbcddee"]
for test in tests:
    print(first_unique(test))

# Space = O(n)
# Time = 0(n)