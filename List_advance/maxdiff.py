def max_diff(arr):
    res = arr[1] - arr[0]
    minval = arr[0]
    for i in arr:
        res = max(res, i-minval)
        minval = min(minval, i)
    print(res)

arr = [5, 10, 2 , 8, 13]
max_diff(arr)