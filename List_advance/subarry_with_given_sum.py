def subarray_with_given_sum(arr, n, sum):
    """
    """
    # This is dynamic window sliding technic
    s, curr = 0, 0

    for e in range(0, n):
        # start with windo of s = 0 and e till curr becomes > sum
        curr += arr[e]
        if curr > sum:
            # curr > sum this means remove elems from left one by one until == sum
            curr -= arr[s]
            s += 1
        if curr == sum:
            return True
    return False

arr = [10, 5, 7, 8, 9]
n = len(arr)
sum = 15
print(subarray_with_given_sum(arr, n, sum))
        