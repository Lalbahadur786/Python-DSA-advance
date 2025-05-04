# find the lomuto partition at p 
# while p (index) == k - 1 then return p 
# 20, 10 3 K=3 here smalles kth element is 20

def lomuto_partition(arr, l, r):
    """
    """
    p = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= p:
            # then swap the numbers
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # Now fix the position of pivot elem
    arr[i], arr[r] = arr[r], arr[i]
    return i


def find_kth_smallest_num(arr, k):
    """
    """
    l = 0
    r = len(arr) - 1
    while l <= r:
        p_idx = lomuto_partition(arr, l, r)
        if p_idx == k-1:
            return arr[p_idx]
        elif p_idx > k - 1:
            r = p_idx - 1
        else:
            l = p_idx + 1
    return -1

arr = [10, 5, 4, 15, 2, 0, 101]

print(find_kth_smallest_num(arr, 6))

