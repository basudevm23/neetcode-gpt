class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x_current = init
        for i in range(iterations):
            f_derivative = 2*x_current
            x_current -= learning_rate*f_derivative
        return round(x_current, 5)