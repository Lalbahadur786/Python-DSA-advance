def previous_greater_elem(arr):
    st = []

    for i in range(len(arr)):
        while len(st) > 0 and st[-1] <= arr[i]:
            st.pop()
        previous_gt = -1 if len(st) == 0 else st[-1]
        print(previous_gt, end=" ")
        st.append(arr[i]) # storing values

arr = [20, 30, 10, 5, 15]
previous_greater_elem(arr)