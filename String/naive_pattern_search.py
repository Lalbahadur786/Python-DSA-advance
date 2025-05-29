def naive_pattern_search(txt, pat):
    """
    """
    n = len(txt)
    m = len(pat)
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if pat[j] != txt[i + j]:
                break
            j += 1
        if j == m:
            print(i, end=" ")

string = "ABCDABCD"
pat = "CD"
naive_pattern_search(string, pat)