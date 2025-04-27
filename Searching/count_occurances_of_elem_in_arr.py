# Program to find count of x in an arr
# linear approach O(n)
# binary search O(logn + k)
# using binary first occur + last occur upperbound(O(logn))

def first_occurance(arr, l, h, x):
    """
    """
    if l > h:
        return -1
    mid = (l + h) // 2

    if x > arr[mid]:
        return first_occurance(arr, mid+1, h, x)
    elif x < arr[mid]:
        return first_occurance(arr, l, mid-1, x)
    elif mid == 0 or arr[mid - 1] != arr[mid]:
        return mid
    else:
        return first_occurance(arr, l, mid-1, x)


def last_occurance(arr, l, h, x):
    """
    """
    if l > h:
        return -1
    mid = (l + h) // 2

    if x > arr[mid]:
        return last_occurance(arr, mid+1, h, x)
    elif x < arr[mid]:
        return last_occurance(arr, l, mid-1, x)
    elif mid == len(arr)-1 or arr[mid + 1] != arr[mid]:
        return mid
    else:
        return last_occurance(arr, mid+1, h, x)


arr = [10, 20, 20, 20, 20, 20, 30, 30, 40]
first_occur = first_occurance(arr, 0, len(arr)-1, 2)
if first_occur != -1:
    last_occur = last_occurance(arr, 0, len(arr)-1, 2)
    print( last_occur - first_occur + 1)
else:
    print(-1)