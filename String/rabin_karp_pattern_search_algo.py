d = 256

def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i, j = 0, 0
    p = 0 # hash value of pattern
    t = 0 # hash value for txt
    h = 1

    # Calcu;are h = pow(d, M-1)%q
    for i in range(M - 1):
        h = (h * d) % q
    
    # Calculate hash of pattern and first window
    for i in range(M):
        p = (d * p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q
    
    # Slide the pattern over text one by one
    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
            else: j+= 1

            if j == M:
                print(i, end=" ")
        
        if i < N-M:
            t = (d *(t-ord(txt[i])*h) + ord(txt[i+M]))%q
            if t < 0:
                t = t+q

txt = "ABCDABCD"
pat = "CD"
q = 101
search(pat, txt, q)