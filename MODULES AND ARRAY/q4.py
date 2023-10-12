4. Write a NumPy program to create a nxn matrix and display its attributes.

import numpy as np

n = int(input("Enter the value of n for the nxn matrix: "))
matrix = np.arange(1, n**2 + 1).reshape(n, n)
print("Matrix:")
print(matrix)

print("Matrix Shape:", matrix.shape)
print("Number of Dimensions:", matrix.ndim)
print("Total Number of Elements:", matrix.size)
print("Data Type of Elements:", matrix.dtype)
