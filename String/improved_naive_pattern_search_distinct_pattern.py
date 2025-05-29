def improved_pattern_search(txt, pat):
    """
    This algo is useful when pattern chars are distinct
    """
    n = len(txt)
    m = len(pat)
    i = 0
    while i <= (n-m):
        for j in range(m):
            if pat[j] != txt[i + j]:
                break
        else: j += 1
        if j == m:
            print(i, end=" ")
        if j == 0:
            i += 1
        else:
            i += j

string = "ABCDABCD"
pat = "CD"
improved_pattern_search(string, pat)