"""sort arr [0, 0, 2, 2, 0, 0, 1, 1, 2] there types of arr with modification of hoars partition"""

def sort_three_elem_type(arr):
    """
    """
    lo, mid, hi = 0, 0, (len(arr) - 1)

    while mid <= hi:
        if arr[mid] == 0:
            # swap with low position
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1

        elif arr[mid] == 1:
            # just increment mid by 1
            mid += 1
        else:
            # this is num 2 swap with mid and hi
            # decrement hi
            arr[mid] , arr[hi] = arr[hi], arr[mid]
            hi -= 1


arr = [0, 0, 2, 2, 0, 0, 1, 1, 2]
sort_three_elem_type(arr)
print(arr)
