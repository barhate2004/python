import numpy as np

input_list = input("Enter a list of numeric values (comma-separated): ").split(',')
numeric_array = np.array(input_list, dtype=float)
print("NumPy array:", numeric_array)
