def subset_sum(arr, n, sum):
    """
    """
    # Base case
    if n == 0:
        return 1 if sum == 0 else 0
    else:
        return subset_sum(arr, n-1, sum) + subset_sum(arr, n-1, sum-arr[n-1])
    

arr = [10, 35, 15]
n = len(arr)
sum = 25
print(subset_sum(arr, n , sum))