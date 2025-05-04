def sort_arr_by_hoars(arr):
    # for separating pos & neg numbers
    pivot_val = 0
    i = -1
    j = len(arr) 
    while True:
        i += 1
        if arr[i] < 0:
            i += 1
        
        j -= 1
        if arr[j] > 0:
            j -= 1
        
        if i >= j:
            return
        arr[i], arr[j] = arr[j], arr[i]

arr = [-1, 10, 5, -5, -3, 10, -7, 5]
sort_arr_by_hoars(arr)
print(arr)