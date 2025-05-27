""" To find longest subarray with equal number of one and zero
    simply replace one with -1 and make it problem of finding
    longest subarray with sum zero"""


def longest_sub_arr_with_equal_zero_and_one(arr):
    """
    """
    # Replace 1 with -1
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1
    
    # from here onwords it becoms
    # find longest subarray with sum zero
    p_sum = 0
    res = 0
    my_dict = dict()
    for i in range(len(arr)):
        p_sum += arr[i]
        if p_sum == 0:
            res = i + 1
        if p_sum - 0 in my_dict:
            res = max(res, i - my_dict[p_sum-0])
        if p_sum not in my_dict:
            my_dict[p_sum] = i
    return res

arr = [0, 1, 1, 1, 0, 0, 1, 0]
print(longest_sub_arr_with_equal_zero_and_one(arr))