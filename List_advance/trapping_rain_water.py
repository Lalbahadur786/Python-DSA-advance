def max_water(arr, n):
    """
    """
    left_bar = [0] * n
    right_bar = [0] * n
    res = 0

    # compute left_bar arr for each bar
    left_bar[0] = arr[0]
    for i in range(1, n):
        left_bar[i] = max(arr[i], left_bar[i-1])
    
    # compute right bar arr for each bar 
    right_bar[n - 1] = arr[n - 1]

    for j in range(n-2, -1, -1):
        right_bar[j] = max(arr[j], right_bar[j + 1])
    
    # get the trapping water at each point considering 
    # left bar and right bar

    for i in range(0, n):
        res += min(left_bar[i], right_bar[i]) - arr[i]
    
    return res

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)

print(max_water(arr, n))