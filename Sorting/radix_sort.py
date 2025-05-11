
def counting_sort(arr, exp):
    """
    """
    output = [0] * len(arr)
    count = [0] * 10
    #count the digits occurance
    for i in range(0, len(arr)):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # calculate_prefix sum
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = len(arr) - 1
    # traversing in reverse order
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    """
    """
    # sort numbers by digits
    max_num = max(arr)
    exp = 1
    while max_num / exp > 1:
        counting_sort(arr, exp)
        exp *= 10

arr = [319, 10, 5, 212, 14, 8]
radix_sort(arr)
print(arr)