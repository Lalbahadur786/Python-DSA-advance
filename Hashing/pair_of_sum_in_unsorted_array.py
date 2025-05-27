def pair_sum_in_unsorted_array(arr, target_sum):
    u_set = set()
    for elem in arr:
        if target_sum-elem in u_set:
            return True
        u_set.add(elem)
    return False


arr = [140, 15, 36, 78, 16]
print(pair_sum_in_unsorted_array(arr, 32))
