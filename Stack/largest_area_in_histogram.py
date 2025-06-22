def get_max_area(arr):
    st = []
    res = 0
    n = len(arr)
    for i in range(n):
        while st and arr[st[-1]] >= arr[i]:
            tp = st[-1]
            st.pop()
            curr_width = (i - st[-1] -1) if st else i
            res = max(res, curr_width*arr[tp])
        st.append(i)
    
    while st: # pop remaining item # all itms would be smallest
        tp = st[-1]
        st.pop()
        curr_width = (n - st[-1] -1) if st else n
        res = max(res, curr_width*arr[tp])
    return res

arr = [60, 20, 50, 40, 10, 50, 60]
print(get_max_area(arr))
