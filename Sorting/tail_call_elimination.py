def hoares_partition(arr, l, h):
    # Partition
    p = arr[l]
    i = l - 1
    j = h + 1
    while True:
        i += 1
        if arr[i] < p:
            i += 1
        j -= 1
        if arr[j] > p:
            j -= 1
        
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


# Normal recurion call quick sort
def quick_sort(arr, l, h):
    if l < h:
        p = hoares_partition(arr, l, h)
        quick_sort(arr, l, p)
        quick_sort(arr, p+1, h)

arr = [8, 4, 7, 9, 3, 10, 5]
# quick_sort(arr, 0, len(arr)-1)
# print(arr)

# tail elimination quick sort
def quick_sort(arr, l, h):
    while l < h:
        p = hoares_partition(arr, l, h)
        quick_sort(arr, l, p)
        l = p+1 # tail recurive elimination

arr = [8, 4, 7, 9, 3, 10, 5]
quick_sort(arr, 0, len(arr)-1)
print(arr)