3. Write a NumPy program to test whether all elements in an array evaluate to True.

import numpy as np

input_array = np.array(input("Enter an array (space-separated): ").split(), dtype=bool)

if np.all(input_array):
    print("All elements evaluate to True.")
else:
    print("Not all elements evaluate to True.")
