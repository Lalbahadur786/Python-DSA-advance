# Sliding window technique

def k_max_sum(arr, k, n):
    """
    """
    # first compute sum for  the first window
    res = 0
    curr = 0
    for i in range(0, k):
        curr += arr[i]
    res = curr
    
    # Now slide the window one by one

    for i in range(k, n):
        curr = curr + arr[i] - arr[i - k]
        res = max(res, curr)
    return res

arr = [10, 5, 7, 8, 7, 5]
n = len(arr)
k = 2
print(k_max_sum(arr, k, n))

