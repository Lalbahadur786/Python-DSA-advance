""" Count sort O(n+k) used when elems from sort range"""

def count_sort(arr, k):
    """
    """
    out_arr = [0] * len(arr)
    count = [0] * k

    # count occurance of elems
    for num in arr:
        count[num] += 1

    # calculate prefix sum
    for i in range(1, k):
        count[i] += count[i - 1]
    
    # prepare out arr in reverse order
    for num in reversed(arr):
        out_arr[count[num] - 1] = num
        count[num] -= 1
    
    # copy out_arr in arr
    for i in range(len(arr)):
        arr[i] = out_arr[i]

arr = [1,4,4,1,0,1]
count_sort(arr, 5)
print(arr)