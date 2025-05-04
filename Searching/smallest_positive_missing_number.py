# [-3, 4, 1, 2, 3]

def  smallest_positive_missing_number(arr):
    """
    """

    n = len(arr)

    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            correct_idx = arr[i] - 1
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
    
    print(arr)
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    
    return n + 1


arr = [-25, 38, 24, -17, 7, 31, 43, 8, 20, 49, -33, -11, 19, 13, -28, 44, 23, -3, -19, 12, 32, 40, 42, 41, 7, -35, -29, 7, 24, 41, -3, 1, -19, -29, -13, -10, 4, -20, 48]

print(smallest_positive_missing_number(arr))