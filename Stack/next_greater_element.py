def next_greater_elem(arr):
    n = len(arr)
    st = []
    res = [None] * n
    for i in range(n-1, -1, -1):
        while len(st) > 0 and st[-1] <= arr[i]:
            st.pop()
        res[i] = -1 if len(st) == 0 else st[-1]
        st.append(arr[i])
    for num in res:
        print(num, end=" ")

arr = [5, 15, 10, 8, 6, 12]
# arr = [6, 8, 0, 1, 3]
next_greater_elem(arr)