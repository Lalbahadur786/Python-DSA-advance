
def reverse(arr, s, e):
    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1


def left_rotate_by_d_places(arr, d, n):
    if d == 0:
        return arr
    reverse (arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)


arr = [10, 20, 30, 40, 50, 60, 70]
n = len(arr)
d = 2
left_rotate_by_d_places(arr, d, n)
print(arr)


    
    