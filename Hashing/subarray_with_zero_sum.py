def subarray_with_zero_sum(arr):
    """
    subaary  means continuous
    """
    prefix_sum = 0
    hashing_set = {}
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == 0 or prefix_sum in hashing_set:
            return True
        hashing_set.add(prefix_sum)
    return False

arr = [10, -10, 5, 8, 9, -10]
print(subarray_with_zero_sum(arr))