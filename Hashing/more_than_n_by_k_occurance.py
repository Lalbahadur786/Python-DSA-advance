from collections import Counter

def more_than_n_by_k_occur(arr, k):
    """
    """
    count_dict = Counter(arr)
    for c in count_dict:
        if count_dict[c] > len(arr) // k:
            print(c)

arr = [10, 10, 15, 10, 13, 52, 74, 16]
more_than_n_by_k_occur(arr, 3)        