class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        f_old=init
        f_new=0
        while iterations>0:
            f_new=f_old-(2*learning_rate*f_old)
            f_old=f_new
            iterations=iterations-1
        return round(f_old,5)
        pass
