def reverse_col(matrix):
        n1 = len(matrix)
        m1= len(matrix[0])
        k = 0
        l = 0
        for i in range(n1):
                for j in range(m1//2):
                        matrix[i][j], matrix[i][m1-1-j] = matrix[i][m1-1-j], matrix[i][j]

        return matrix

matrix = [[1, 2, 3], [5, 6, 7], [11, 10, 9], [13, 14, 15]]
print(reverse_col(matrix))