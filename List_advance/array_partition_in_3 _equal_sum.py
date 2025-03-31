def get_three_equal_sum(arr, n):
    """
    """
    rs = sum(arr)
    curr_sum = 0
    res = []
    if rs % 3 != 0:
        return [-1, -1]
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum == rs / 3:
            res.append(i)
            curr_sum = 0
    return res

arr = [5, 2, 6, 1, 1, 1, 0, 5]
n = len(arr)
print(get_three_equal_sum(arr, n))
        
