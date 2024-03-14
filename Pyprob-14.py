#Problem 14: Matrix Operations
#Write functions to perform basic matrix operations such as addition, subtraction, and multiplication.

def add_mat(mat1,mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices should have the same dimensions!")

    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))] #initializing the result with zeros

    for i in range(len(mat1[0])): # i number of columns
        for j in range(len(mat1)): # j number of rows
            result[j][i]= mat1[j][i]+mat2[j][i]
    return result

def sub_mat(mat1,mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices should have the same dimensions!")
    
    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))] #initializing the result with zeros

    for i in range(len(mat1[0])): # i number of columns
        for j in range(len(mat1)): # j number of rows
            result[j][i]= mat1[j][i]-mat2[j][i]
    return result

def mutl_mat(mat1,mat2):
    if len(mat1[0]) != len(mat2):
        raise ValueError("Matrices should have (n*m - m*p) dimensions!")

    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))] #initializing the result with zeros

    for i in range(len(mat1)): # i number of rows
        for j in range(len(mat2[0])): # j number of columns
            for k in range(len(mat2)):
                result[i][j]+= mat1[i][k]*mat2[k][j]
    return result

matrix1 = [[1, 2, 3, 5],
           [4, 5, 6, 5],
           [7, 8, 9, 5]]

matrix2 = [[9, 8, 7,5],
           [6, 5, 4,5],
           [3, 2, 1,5]]

matrix3 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1],
           [1, 4, 2]]

result_matrix = add_mat(matrix1, matrix2)
result_matrix_sub = sub_mat(matrix1, matrix2)
result_matrix_mult = mutl_mat(matrix1,matrix3)

print('****************************')
for row in result_matrix:
    print(row)
print('****************************')
for row in result_matrix_sub:
    print(row)
print('****************************')
for row in result_matrix_mult:
    print(row)
