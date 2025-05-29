CHAR = 256

def are_same(ct, cp):
    for i in range(CHAR):
        if ct[i] != cp[i]:
            return False
    return True

def is_anagram_present(text, pat):
    """
    """
    n = len(text)
    m = len(pat)
    ct = [0] * CHAR
    cp = [0] * CHAR
    for i in range(m):
        ct[ord(text[i])] += 1
        cp[ord(pat[i])] += 1
    for i in range(m, n):
        if are_same(ct, cp):
            return True
        ct[ord(text[i])] += 1
        ct[ord(text[i - m])] -= 1
    # Check the last window
    if are_same(ct, cp):
        return True
    return False

text = "hello"
pat = "lo"
print(is_anagram_present(text, pat))
