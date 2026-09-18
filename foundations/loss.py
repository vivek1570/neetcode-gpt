import numpy as np
from numpy.typing import NDArray
from math import log

class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: true labels (0 or 1)
        # y_pred: predicted probabilities
        # Hint: clip y_pred to [1e-7, 1 - 1e-7] to avoid log(0)
        # return round(your_answer, 4)
        n=len(y_true)
        y_pred = np.clip(y_pred, 1e-7, 1 - 1e-7)
        ans=0
        for i in range(n):
            if y_true[i]==1:
                ans+=log(y_pred[i])
            else:
                ans+=log(1-y_pred[i])
        ans=ans/n
        ans=0-ans
        return round(ans,4)
        pass

    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: one-hot encoded true labels (shape: n_samples x n_classes)
        # y_pred: predicted probabilities (shape: n_samples x n_classes)
        # Hint: clip y_pred to [1e-7, 1 - 1e-7] to avoid log(0)
        # return round(your_answer, 4)
        ans=0
        n=len(y_true)
        for i in range(n):
            m=len(y_true[i])
            y_pred[i] = np.clip(y_pred[i], 1e-7, 1 - 1e-7)
            for j in range(m):
                ans+=(y_true[i][j]*log(y_pred[i][j]))
        ans=ans/n
        ans=0-ans
        return round(ans,4)
        pass
