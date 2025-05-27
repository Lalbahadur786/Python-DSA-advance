""" In this prohram will subtract arr1 - arr2 
    and temp_arr becomes problem of finding
    longest subarry with sum 0"""

def longest_common_sub_arr_in_binary_arr(arr1, arr2):
    """
    """
    # first subtract arr1 - arr2 (or vice versa)
    temp_arr = []
    for i in range(len(arr1)):
        temp_arr.append(arr1[i] - arr2[i])
    
    # now problem reduced to find longest subarr with sum 0
    res = 0
    p_sum = 0
    my_dict = dict()
    
    for i  in range(len(temp_arr)):
        p_sum += temp_arr[i]
        if p_sum == 0:
            res = i + 1
        if p_sum in my_dict:
            res = max(res, i - my_dict[p_sum])
        if p_sum not in my_dict:
            my_dict[p_sum] = i
    return res

arr1 = [0, 0, 1, 1, 1, 0, 0, 1]
arr2 = [0, 1, 0, 0, 1, 0, 1, 0]
print(longest_common_sub_arr_in_binary_arr(arr1, arr2))