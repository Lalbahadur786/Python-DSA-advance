def normal_max_kandane_algo(arr, n):
    max_ending = res = arr[0]

    for i in range(1, n):
        max_ending = max(max_ending + arr[i], arr[i])
        res = max(max_ending, res)
    return res

def max_sum_circular_subarray(arr, n):
    # this problem has two part
    # first calculate normal max subarray
    # second subtract max_sub from min_sub_ array (circular sum)
    max_standard_sum = normal_max_kandane_algo(arr, n)
    if max_standard_sum < 0:
        # this means circular subarray would be also in minus (wrong value)
        return max_standard_sum
    arr_sum = 0
    for i in range (0, n):
        arr_sum += arr[i]
        arr[i] = -arr[i]
    max_min_circular_subarray = arr_sum +  normal_max_kandane_algo(arr, n)

    return max(max_min_circular_subarray, max_standard_sum)

arr = [8, -4, 3, -5, 4]
n = len(arr)
print(max_sum_circular_subarray(arr, n))