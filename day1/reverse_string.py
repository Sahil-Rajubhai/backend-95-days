def reverse_srting(text):
    reverse_text = ""
    for char in text:
        reverse_text = char + reverse_text
    return reverse_text

# Example usage:
text = "Hello, World!"
result = reverse_srting(text)
print(f"The reversed string is: {result}")