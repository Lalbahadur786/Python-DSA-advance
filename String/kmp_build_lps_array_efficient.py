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

string = "abacabad"
print(kmp_lps_array_efficient(string))