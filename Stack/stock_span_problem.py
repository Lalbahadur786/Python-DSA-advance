def print_stock_span(arr):
    st = []
    st.append(0)
    print(1, end=" ")
    for i in range(1, len(arr)):
        while len(st) != 0 and arr[st[-1]] <= arr[i]:
            st.pop()
        span = i+1 if len(st) == 0 else i - st[-1]
        print(span, end=" ")
        st.append(i) # Storing indices

arr = [60, 10, 20, 25, 35, 38, 70]
arr = [10, 4, 5, 90, 120, 80]
print_stock_span(arr)