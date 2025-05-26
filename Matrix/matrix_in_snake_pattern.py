arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [10, 11, 12]]


for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i % 2 != 0:
            print(arr[i][len(arr[i])-1-j], end=" ")
        else:
            print(arr[i][j], end=" ")

