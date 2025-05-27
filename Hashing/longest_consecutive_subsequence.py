""" Find subsequance of consecutive number
the order of elems may defer"""

def longest_consecutive_subsequence(arr):
    """
    """
    # Create a set of array elems
    s = set()
    res = 0
    for elem in arr:
        s.add(elem)

    # iterate through arr
    for i  in range(len(arr)):
        if arr[i] - 1 not in s:
            curr = 1
            j = arr[i]
            while j in s:
                j += 1
            res = max(res, j - arr[i])
    return res

# arr = [5, 7, 4, 6, 4, 3, 10, 2]
arr = [4, 3, 2, 1]
print(longest_consecutive_subsequence(arr))