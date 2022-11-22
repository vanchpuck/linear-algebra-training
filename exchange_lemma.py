import numpy as np
import util


def exchange_vectors_practice(s: np.array, b: np.array):
    """
    :param s: set of vectors
    :param b: set of linearly independent vectors such that Span s = Span b
    :return: set of vectors t that includes b, possibly some of s such that |a| = |b| and Span t = Span s
    """
    # set to keep certain vectors from being ejected
    a = np.array([])
    # s_minus = s
    for i, b_vec in enumerate(b):
        print(f'Injecting: {b_vec}')
        a = b_vec if a.size == 0 else np.vstack([b_vec, a])
        for j, s_vec in enumerate(s):
            s_minus = np.delete(s, j, 0)
            coefficient_matrix = np.vstack([a, s_minus]).T
            # check linear dependence
            solution = np.linalg.lstsq(coefficient_matrix, s_vec)
            if util.check_lstsq_solution(coefficient_matrix, s_vec, solution[0]):
                # generator v is a linear combination of other generators in S => Span (S - {v}) = Span S
                print(f'Ejecting: {s_vec}')
                s = s_minus
                break
    return np.vstack([s, a])


if __name__ == '__main__':
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    result = exchange_vectors_practice(
        np.array([[2, 4, 0], [1, 0, 3], [0, 4, 4], [1, 1, 1]]),
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    )
    print(result)
