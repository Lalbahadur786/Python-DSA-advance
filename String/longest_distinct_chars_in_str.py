def longest_unique_sub_str(string):
    """
    """
    seen = {}
    max_len = 0
    start = 0
    for end in range(len(string)):
        if string[end] in seen:
            start = max(start, seen[string[end]]+ 1)
        seen[string[end]] = end
        max_len = max(max_len, end-start + 1)
    return max_len

string = "abbcd"
print(longest_unique_sub_str(string))