""" This program is to merge intervals with the range"""
# [[1, 5], [2, 3]] = [1, 5]


def merge_intervals(arr):
    """
    """
    # sort the arr by start min
    arr.sort(key = lambda x: x[0])

    res = 0

    for i in range(1, len(arr)):
        if arr[res][1] >= arr[i][0]:
            # this means ranges are over lapping
            arr[res][1] = max(arr[res][1], arr[i][1])
        else:
            res += 1
            arr[res] = arr[i]
    
    for i in range(res + 1):
        print(arr[i], end=" ")

arr = [[1, 2], [2, 3], [3, 5], [100, 200], [5, 10]]
merge_intervals(arr)