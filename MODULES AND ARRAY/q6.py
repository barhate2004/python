Given a 2 D Array of N X M Dimension, Write a function that accepts this array as well as two
numbers N and M. The method should return the top-left N X M sub matrix .
import numpy as np

def get_sub_matrix(matrix, n, m):
    if n <= matrix.shape[0] and m <= matrix.shape[1]:
        sub_matrix = matrix[:n, :m]
        return sub_matrix
    else:
        return None

N = int(input("Enter the value of N: "))
M = int(input("Enter the value of M: "))

input_matrix = np.array(input("Enter a 2D matrix (row-wise, space-separated): ").split(), dtype=int).reshape(N, -1)

sub_matrix = get_sub_matrix(input_matrix, N, M)
if sub_matrix is not None:
    print("Top-left sub-matrix:")
    print(sub_matrix)
else:
    print("Invalid dimensions for sub-matrix.")
