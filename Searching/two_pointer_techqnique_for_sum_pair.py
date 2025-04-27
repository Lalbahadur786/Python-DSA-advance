# This is two pointer technique to find pair for sum X
# Only works for sorted array  in O(n) time

def is_pair(arr, sum):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == sum:
            return True
        elif arr[i] + arr[j] > sum:
            j -= 1
        else:
            i += 1
    return False

arr = [10, 15, 20, 25, 28, 30]
print(is_pair(arr, 53))