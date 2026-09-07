import numpy as np
from numpy.typing import NDArray


class Solution:
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        def sig(x):
            return round((1/(1+math.exp(-x))),5)
        arr=[]
        for x in z:
            arr.append(sig(x))
        return arr
        pass

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        arr=[]
        for x in z:
            arr.append(float(max(0,x)))
        return arr
        pass
