import numpy as np
import galois
from dataclasses import dataclass


@dataclass
class TestCase:
    u_basis: np.array
    v_basis: np.array
    vectors_to_decompose: np.array


def direct_sum_decompose(u_basis: np.array, v_basis: np.array, w: np.array):
    """
    :param u_basis: basis of the vector space U
    :param v_basis: basis of the vector space V
    :param w: vectors belonging to the direct sum U + V
    :return: pair (u, v) such that w = u + v and u belongs to U and v belongs to V
    """
    basis_matrix = np.vstack([u_basis, v_basis]).T
    solution = np.linalg.lstsq(basis_matrix, w)
    if solution[1][0] > 0.00000000000000001:
        raise Exception("Vector can't be represented in basis vectors")
    u_vector = solution[0][0:u_basis.shape[0]]
    # print(v_basis.shape[0])
    v_vector = solution[0][-v_basis.shape[0]]
    return u_vector, v_vector


if __name__ == '__main__':
    over_R = TestCase(
        np.array([
            [2, 1, 0, 0, 6, 0],
            [11, 5, 0, 0, 1, 0],
            [3, 1.5, 0, 0, 7.5, 0]
        ]),
        np.array([
            [0, 0, 7, 0, 0, 1],
            [0, 0, 15, 0, 0, 2]
        ]),
        np.array([
            np.array([2, 5, 0, 0, 1, 0]),
            np.array([0, 0, 3, 0, 0, -4]),
            np.array([1, 2, 0, 0, 2, 1]),
            np.array([-6, 2, 4, 0, 4, 5]),
        ])
    )
    gf = galois.GF(2)
    # over_GF2 = TestCase(
    #     np.array([
    #         [1, 1, 0, 1, 0, 1],
    #         [1, 1, 0, 0, 0, 1],
    #         [1, 0, 0, 0, 0, 0],
    #     ]).view(gf),
    #     np.array([
    #         [1, 1, 1, 0, 1, 1]
    #     ]).view(gf),
    #     np.array([
    #         np.array([0, 0, 0, 0, 0, 0]),
    #         np.array([1, 0, 0, 1, 0, 0]),
    #         np.array([1, 1, 1, 1, 1, 1])
    #     ]).view(gf)
    # )
    for test_case in [over_R]:
        for vector_to_decompose in test_case.vectors_to_decompose:
            print(direct_sum_decompose(test_case.u_basis, test_case.v_basis, vector_to_decompose))