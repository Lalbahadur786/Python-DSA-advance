""" LPS = longest proper prefix and suffix"""

def longest_proper_prefix_suffix(string, n):
    """
    """
    for len in range(n-1, -1, -1):
        for j in range(len):
            if string[j] != string[n-len+j]:
                break
        else:
            return len
    return 0

def kmp_lps_naive(string):
    """
    """
    lps = [0 for _ in range(len(string))]
    lps[0] = 0
    for i in range(1, len(string)):
        lps[i] = longest_proper_prefix_suffix(string, i+1)
    return lps

string = "abacabad"
print(kmp_lps_naive(string))