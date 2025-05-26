""" Rotate matrix anit clock by 90 degree"""
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

# first transpose the matrix 
for i in range(len(arr)):
    for j in range (i+1, len(arr)):
        # swap upper diagonal element with lower diagonal elemnet
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)

# Now replace first row with last 2 with third
n = len(arr)
for i in range(n):
      for j, k in zip(range(n//2), range(n-1, n//2-1, -1)):
          arr[j][i], arr[k][i] = arr[k][i], arr[j][i]

print(arr)