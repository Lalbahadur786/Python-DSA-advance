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

def get_largest_rect_in_matrix(mat):
    res = get_max_area(mat[0])
    for i in range(1, len(mat)):
        for j in range(len(mat[i])):
            # adding c-c value creating histogram
            if mat[i][j]:
                mat[i][j] += mat[i-1][j]
        res = max(res, get_max_area(mat[i]))
    return res

arr = [[1, 0, 0, 1, 1], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1]]
print(get_largest_rect_in_matrix(arr))