import numpy as np


def check_lstsq_solution(coefficient_matrix: np.array, dependent_variable: np.array, solution: np.array):
    residual = dependent_variable - coefficient_matrix.dot(solution)
    return residual.dot(residual) < 0.00000000000000001
