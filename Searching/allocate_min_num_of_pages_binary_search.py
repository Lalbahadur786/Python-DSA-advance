# Allocate min max num of pages to k students using binary search

def is_possible(arr, n, k, ans):
    """
    """
    req_student, curr_sum = 1, 0

    for i in range(n):
        if arr[i] > ans:
            return False
        
        if curr_sum + arr[i] > ans:
            req_student += 1
            curr_sum = arr[i] # assigning to the next student
        else:
            curr_sum += arr[i]
        if req_student > k:
            return False
    
    return True




def min_pages_binary(arr, n , k):
    """
    """
    s = max(arr)
    e = sum(arr)
    # range [max, sum]
    while s <= e:
        mid = (s + e) // 2
        if is_possible(arr, n, k, mid):
            # then find min numbers
            res = mid
            e = mid - 1
        else:
            s = mid + 1
    return res

arr = [10, 20, 30, 50]
n = len(arr)
k = 2

print(min_pages_binary(arr, n, k))