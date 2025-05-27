def longest_sub_arr_with_sum(arr, target_sum):
    p_sum = 0
    my_dict = dict()
    res = 0
    for i in range(len(arr)):
        p_sum += arr[i]
        
        # check if p_sum == target_sum
        if p_sum == target_sum:
            res = i + 1
        # check if (p_sum - target_sum) has occurred before
        if (p_sum - target_sum) in my_dict:
            res = max(res, i - my_dict[p_sum - target_sum])
        # store the first occurrence of p_sum
        if p_sum not in my_dict:
            my_dict[p_sum] = i
    return res


arr = [8,3,1,5,-6,6,2,2]
sum = 8
print(arr)
print(longest_sub_arr_with_sum(arr, sum))