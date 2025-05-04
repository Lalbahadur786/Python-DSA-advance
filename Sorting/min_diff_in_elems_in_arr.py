# Return  min diff between a pair of elements

def min_diff_in_arr(arr):
    """
    """
    # Sort the array
    arr.sort()
    res = float("inf")
    # Traverse array in linear time
    for i in range(1, len(arr)):
        res = min(res, (arr[i] - arr[i - 1]))
    
    return res

arr = [11, 0, 41, 75, 62, 21]

print(min_diff_in_arr(arr))