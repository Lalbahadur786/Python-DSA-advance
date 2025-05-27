from collections import defaultdict
def distinct_elem_in_every_window(arr, k):
    """
    """
    my_dict = defaultdict(lambda: 0)

    distinct_count = 0

    # first traverse k elems
    for i in range(k):
        if my_dict[arr[i]] == 0:
            distinct_count += 1
       
        my_dict[arr[i]] += 1
    
    print(distinct_count)

    for i in range(k, len(arr)):
        if my_dict[arr[i - k]] == 1:
            distinct_count -= 1
        my_dict[arr[i - k]] -= 1
    
        if my_dict[arr[i]] == 0:
            distinct_count += 1
        my_dict[arr[i]] += 1

        print(distinct_count)

arr = [10, 10, 20, 20, 30, 40, 40]
distinct_elem_in_every_window(arr, 3)