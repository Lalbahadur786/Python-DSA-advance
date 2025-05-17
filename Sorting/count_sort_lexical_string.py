def count_sort_string(s):
    # Create a count array for 26 lowercase letters
    count = [0] * 26

    # Count each character
    for char in s:
        count[ord(char) - ord('a')] += 1

    # Build the sorted string
    sorted_str = ''
    for i in range(26):
        sorted_str += chr(i + ord('a')) * count[i]

    return sorted_str

# Example usage
input_str = "cbazxy"
sorted_str = count_sort_string(input_str)
print("Sorted string:", sorted_str)

