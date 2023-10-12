4. Create a module that takes n Numpy arrays of same dimensions sums them and return the answer.

import numpy as np

def sum_arrays(*arrays):
    if len(arrays) < 2:
        return None
    result = arrays[0]
    for array in arrays[1:]:
        result += array
    return result
