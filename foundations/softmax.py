import numpy as np
from numpy.typing import NDArray
import math


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        length = len(z)
        final_ans = np.zeros(length)
        sum_exp = 0
        for i in range(length):
            sum_exp += math.exp(z[i]-max(z))
        
        for j in range(length):
            final_ans[j] = math.exp(z[j]-max(z))/sum_exp

        return np.round(final_ans, 4)
        
