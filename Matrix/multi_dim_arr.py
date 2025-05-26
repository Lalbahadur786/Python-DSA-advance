rows = 4
cols = 3

# Not a recommeded way
arr = [[0] * rows] * cols
arr[0][0] = 1
print(arr)

# Recomended way
arr2 = [[0 for i in range(rows)] for j in range(cols)]
arr2[0][0] = 1
print(arr2)