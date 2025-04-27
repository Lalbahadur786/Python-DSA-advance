# This is program is to find whether triplets present for sum

def is_pair(arr, sum, start_index):
    i = start_index
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == sum:
            return True
        elif arr[i] + arr[j] > sum:
            j -= 1
        else:
            i += 1
    return False


def is_triplet_present(arr, sum):
    for i in range(len(arr) - 2): # we can safely skip last 3 items
        if is_pair(arr, sum-arr[i], i+1):
            return True
    return False

arr = [10, 15, 28, 30, 27, 40, 45, 56]
sum = 140

print(is_triplet_present(arr, sum))