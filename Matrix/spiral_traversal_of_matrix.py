" Spiral print of matrix"

def spiral_print(m, n, arr):
    k = 0
    l = 0

    while k < m and l < n:
        # first print first row
        for i in range(l, n):
            print(arr[k][i], end=" ")
        k += 1
        # second print last column
        for i in range(k, m):
            print(arr[i][n - 1], end=" ")
        n -= 1
        # Third bottom row (right to left)
        if  k < m:
            for i in  range(n - 1, (l - 1), -1):
                print(arr[m - 1][i], end=" ")
            
            m -= 1
        
        # fourth print first column
        if l < n:
            for i in range(m - 1, k-1, -1):
                print(arr[i][l], end=" ")
            
            l += 1


arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

R = len(arr)
C = len(arr[0])
spiral_print(R, C, arr)
 