def kmp_lps_array_efficient(string):
    """
    """
    lps = [0 for _ in range(len(string))]
    i = 1
    l = 0
    while i < len(string):
        if string[i] == string[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l == 0:
                lps[i] = 0
                i += 1
            else:
                l = lps[l - 1]
    return lps

def kmp_search(text, pattern):
    lps = kmp_lps_array_efficient(text)
    i = 0 # for text
    j = 0 # for pattern
    res = []
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            res.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] !=  text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return res

text = "ABCDABCD"
pattern = "CD"
print(kmp_search(text, pattern))