def transformSparseMatrix(matrix):
    sparseMatrix = [[], [], []]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                sparseMatrix[0].append(i+1)
                sparseMatrix[1].append(j+1)
                sparseMatrix[2].append(matrix[i][j])
    return sparseMatrix

print(transformSparseMatrix([[3,0,0,0,0],[0,2,2,0,0],[0,0,0,1,3],[0,0,0,2,0],[0,0,0,0,1]]))
# 実行結果: [[1, 2, 2, 3, 3, 4, 5], [1, 2, 3, 4, 5, 4, 5], [3, 2, 2, 1, 3, 2, 1]]