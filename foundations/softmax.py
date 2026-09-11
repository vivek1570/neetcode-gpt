import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        maxi=max(z)
        divident_sum=0
        for x in z:
            divident_sum+=math.exp(x-maxi)
        ans=[]
        for x in z:
            ans.append(round(((float(math.exp(x-maxi)))/divident_sum),4))
        return ans

        pass
