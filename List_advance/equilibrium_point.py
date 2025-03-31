"""
A number said to be at eqilibrium point when
its left items sum == right items sum
"""

def is_equalibrium_point_present(arr, n):
    """
    """
    right_sum = sum(arr)
    left_sum = 0
    for i in range(0, n):
        right_sum -= arr[i]
        if left_sum == right_sum:
            return True
        left_sum += arr[i]
    return False

arr = [4, 2, -2, 6, 1]
n = len(arr)
print(is_equalibrium_point_present(arr, n))
