def max_sum_subarray(arr, n):
    # subarray = contigues elments set
    res = max_ending = arr[0]
    for i in range(1 , n):
        # max of summing prev elements set sum or self
        max_ending = max(max_ending + arr[i], arr[i])
        res = max(max_ending, res)
    return res


arr = [-3, 8, -2, 4, -5, 6]

print(max_sum_subarray(arr, len(arr)))