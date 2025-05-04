# find the chocloate packerts where the diff or min and max chocloate distribution  is minimal

def chocolate_distribution(arr, m):
    """
    """
    # if child are zero or no chocolate packets
    if m == 0 or len(arr) == 0:
        return 0
    # if num of choco packets are less then childs
    if len(arr) < m:
        return -1
    
    # sort the arr
    arr.sort()

    # Prepare result with first diff
    res = arr[m - 1] - arr[0]
    # for for loop till len(arr) - m + 1

    for i in range(1, len(arr) - (m + 1)):
        res = min(res, arr[i+m-1] - arr[i])
    
    return res


arr = [7, 3, 2, 4, 9, 12, 56]
arr = [3, 4, 1, 9, 56, 7, 9, 12]
print(chocolate_distribution(arr, 5))

    
