def subarray_with_given_sum(arr, target_sum):
    """
    """
    s, curr = 0, 0
    for e in range(len(arr)):
        curr += arr[e]
        while curr > target_sum:
            curr -= arr[s]
            s += 1
        if curr == target_sum:
            return True
    return False

arr = [10, 48, 65, -7, 85, 6]
print(subarray_with_given_sum(arr, 78))