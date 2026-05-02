import numpy as np
from numpy.typing import NDArray
import math


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        length_array = len(z)
        new_array = np.zeros(length_array)
        for i in range(length_array):
            new_array[i] = 1 / (1 + math.exp(-z[i]))
        return np.round(new_array, 5)


            

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        length = len(z)
        result_array = np.zeros(length)
        for i in range(length):
            result_array[i] = max(z[i], 0)
        return result_array
