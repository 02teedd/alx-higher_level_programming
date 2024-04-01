#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
    return []
squared_matrix = [[0 for _ in row] for row in matrix]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if isinstance(matrix[i][j], int):
        squared_matrix[i][j] = matrix[i][j] * matrix[i][j]
      else:
          squared_matrix[i][j] = matrix[i][j]

  return squared_matrix
