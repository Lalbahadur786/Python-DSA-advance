
def more_than_n_by_k_occur(arr, k):
    """
    """

    r=len(arr)//k
    print(f"r: {r}")
    d={}
    c=0
    for i in arr:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1
    print(d.values())
    for i in d.values():
        if i>r:
            print(i)
            c+=1
    return c
    

arr = [0, 5, 6, 6, 0, 4, 3, 1, 5, 3, 2, 6, 1, 2]

k = 11
print(more_than_n_by_k_occur(arr, k))
