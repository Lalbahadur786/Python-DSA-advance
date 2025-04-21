# you have infine size sorted array. find position of serached elem

# Naive approach

def search_pos_of_elem_naive(arr, x):
    """
    Time complexity
    time = O(pos)
    space - O(1)
    """

    i = 0
    while True:
        if arr[i] == x:
            return i
        if arr[i] > x:
            return -1
        i += 1

arr = [10, 50, 70, 78, 80, 100, 1000, 2000]
x = 100

# print(search_pos_of_elem_naive(arr, x))


def bsearch(arr, l, h, x):
    """
    """
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = l + 1
        else:
            h = h - 1
    return -1

def search_pos_of_elem_optimal(arr, x):
    """
    increase i counter by 2
    """

    if arr[0] == x:
        return 0
    i = 1

    while i < len(arr) and arr[i] < x:
        i *= 2
    
    if i < len(arr) and arr[i] == x:
        return i
    return bsearch(arr, (i // 2)+1, i-1, x)

arr = [10, 50, 70, 78, 80, 100, 1000, 2000, 78457]
x = 78457
print(search_pos_of_elem_optimal(arr, x))