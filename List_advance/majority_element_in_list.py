def majority_elem(arr, n):
    # An element called to be in majority if 
    # it appears more that > n / 2 times where n is len(arr)

    # using Moore's voting algorithm
    # finding candidate elem with majority
    res = 0
    count = 1
    for i in range(1, n):
        if arr[res] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            res = i
            count = 1
    
    count = 0
    for i in range(0, n):
        if arr[res] == arr[i]:
            count += 1
    
    if count > n // 2:
        return res

arr = [8, 8, 6, 6, 6]
n = len(arr)
idx = majority_elem(arr, n)
print(f"found on index: {idx}, Majority elem is: {arr[idx]}")
    
