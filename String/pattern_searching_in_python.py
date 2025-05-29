def python_pattern_search(txt, pat):
    """
    """
    pos = txt.find(pat)

    while pos >= 0:
        print(pos)
        pos = txt.find(pat, pos+1)
    
string = "ABCDABCD"
pat = "CD"
python_pattern_search(string, pat)