def permute(a, l, r):
    if l == r:
        return print("".join(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

a = list("ABC")
l = 0
r = len(a)
permute(a, l, r)