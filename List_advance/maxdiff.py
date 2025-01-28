def max_diff(arr):
    res = arr[1] - arr[0]
    minval = arr[0]
    for i in arr:
        res = max(res, i-minval)
        minval = min(minval, i)
    print(res)

arr = [2, 8, 7, 6, 5]
max_diff(arr)