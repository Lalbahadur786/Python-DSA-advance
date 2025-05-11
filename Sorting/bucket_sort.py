def bucket_sort(arr, num_buckets):
    """
    """
    rs = max(arr) + 1
    buckets = [[] for i in range(num_buckets)]

    for x in arr:
        i = (num_buckets * x) // rs
        buckets[i].append(x)
    
    # now sort buckets which insertion sort 
    # Here using python inbuilt
    for i in range(num_buckets):
        buckets[i].sort()
    
    idx = 0
    for i in range(num_buckets):
        for j in range(len(buckets[i])):
            arr[idx] = buckets[i][j]
            idx += 1


arr = [i for i in range(25, 0, -1)]
bucket_sort(arr, 5)
print(arr)

