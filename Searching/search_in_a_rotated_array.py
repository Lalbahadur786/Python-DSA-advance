# Alogorithm
# in rotated sorted array any half would be already sorted
# use binary seach to find elem

def search_in_sorted_rotated_array(arr, x):
    """
    """

    l = 0
    h = len(arr) - 1

    while (l <= h):
        mid = (l + h) // 2
        if  arr[mid] == x:
            return mid
        if arr[l] < arr[mid]:
            # this means left half is sorted
            if arr[l] <= x < arr[mid]:
                h = mid - 1
            else:
                l = mid + 1
        else:
            # this means right half is sorted
            if arr[mid] < x <= arr[h]:
                h = mid - 1
            else:
                l = mid + 1
    return -1

arr = [10, 20, 40, 6, 5, 8]
x = 20
print(search_in_sorted_rotated_array(arr, x))