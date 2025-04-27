# Allocate min num pages to students

def min_pages(arr, n , k):
    """
    """
    # if only one student
    if k == 1:
        return sum(arr[0:n])
    
    # if only one book
    if n == 1:
        return arr[0]
    
    res = float("inf")

    for i in range(1, n):
        res = min(res, max(min_pages(arr, i, k-1), sum(arr[i:n])))
    return res

arr = [10, 20, 30, 50]
n = len(arr)
k = 2

print(min_pages(arr, n, k))
