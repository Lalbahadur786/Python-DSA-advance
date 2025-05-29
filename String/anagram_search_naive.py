"""A substring matching with permutation with the text and chars has to be
contnuous"""

CHAR = 256

def are_anagram(pat, text, i):
    count = [0] * CHAR
    for j in range(len(pat)):
        count[ord(pat[j])] += 1
        count[ord(text[i+j])] -= 1
    for j in range(CHAR):
        if count[j] != 0:
            return False
    return True


def anagram_search_naive(text, pat):
    """
    """
    n = len(text)
    m = len(pat)
    for i in range(n-m+1):
        if are_anagram(pat, text, i):
            return True
    return False


text = "hello"
pat = "lle"
print(anagram_search_naive(text, pat))