#Problem 25: Matrix Transposition
#Write a function that transposes a given matrix.

def transpose_mat(matrix):
    trans_mat = [[0 for _ in range(len(matrix))]  for _ in range(len(matrix[0]))]

    for j in range(len(matrix[0])): #nb of columns
        for i in range(len(matrix)): #nb of rows
            trans_mat[j][i] = matrix[i][j]
    
    return trans_mat

mat = [[1,2,3,4,5],
       [1,2,4,5,8]]

print(len(mat[0]))
print(len(mat))
t_mat = transpose_mat(mat)
print(t_mat)
