" Here all the columns and rows are sorted already"

def searcg_elem_in_sorted_matrix(arr, x):
    """
    """
    n = len(arr)
    i = 0
    j = n - 1

    while i < n and j >= 0:
        if arr[i][j] == x:
            return "found"
        elif arr[i][j] > x:
            j -= 1
        else:
            i += 1
    
    return "element not found"

arr = [[10, 20, 30, 40],
		[15, 25, 35, 45],
		[27, 29, 37, 48],
		[32, 33, 39, 50]]
print(searcg_elem_in_sorted_matrix(arr, 35))