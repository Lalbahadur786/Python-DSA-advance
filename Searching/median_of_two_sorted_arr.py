# Find Median of two sorted array
# remember n size <= m size
# This is modified binary algorithm
# left A, left B, right A, right B


def median_of_sorted_arr(arr1, arr2):
    """
    """
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1  # swapping low size to n1
    
    n = len(arr1)
    m = len(arr2)
    s = 0
    e = n
    realmergedinarraysize = (n + m + 1) // 2
    while (s <= e):
        mid = (s + e) // 2
        leftAsize = mid 
        leftBsize = realmergedinarraysize - mid

        # chek overflow indices
        leftA = arr1[leftAsize - 1] if leftAsize > 0 else float("-inf")
        leftB = arr2[leftBsize - 1] if leftBsize > 0 else float("-inf")
        rightA = arr1[leftAsize] if leftAsize < n else float("inf")
        rightB = arr2[leftBsize] if leftBsize < m else float("inf")

        # check if criteria passing for checking median
        if leftA <= rightB and rightA >= leftB:
            if (n  + m) % 2 == 0:
                return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
            else:
                return max(leftA, leftB)
        elif leftA > rightB:
            e = mid - 1
        else:
            s = mid + 1

arr1 = [5, 10, 15, 25, 32]
arr2 = [10, 20, 15, 35, 40, 60, 70]

print(median_of_sorted_arr(arr2, arr1))