""" for checking palindrome computation 
if string contains any char occurance odd time (more than 1) then False
"""

from collections import Counter

def is_palindrome_permuation(string):
    """
    """
    # Get the occurance of chars
    cnt_dict = Counter(string)

    odd_occur = 0

    # Traverse through count values and check for odd occur
    for num in cnt_dict.values():
        if num % 2 != 0:
            odd_occur += 1
        if odd_occur > 1:
            return False
    return True

string = "aaaabbbbcd"
print(is_palindrome_permuation(string))