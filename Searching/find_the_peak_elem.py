# [10, 20, 5, 7, 8] # peak elem is 20 . greater than its neighbour

def find_peak_elem_naive(arr):
    """
    O(n), O(1)
    """
    # check if only elem in arr
    if len(arr) == 1:
        return arr[0]
    
    # Check left most peak
    if arr[0] > arr[1]:
        return arr[0]
    
    # Check right most peak
    if arr[-1] > arr[-2]:
        return arr[-1]
    
    # find the peak in middle  elemsts
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return arr[i]
    return -1

# arr = [10, 20, 5, 7, 6]
# print(find_peak_elem_naive(arr))


def find_peak_elem_using_bin_search(arr):
    """
    """
    l = 0
    h = len(arr) - 1

    while(l <= h):
        mid = (l + h) // 2

        if ((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1])):
            # comparing first, last elm edge cases and middle
            break

        if mid > 0 and arr[mid] < arr[mid - 1]:
            h = mid - 1
        else:
            l = mid + 1
    return mid

arr = [1, 2, 0, 2, 6, 12, 9]

print(find_peak_elem_using_bin_search(arr))