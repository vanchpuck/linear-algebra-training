import numpy as np
import math


def multiply_by_diagonal_matrix(matrix: np.array, diagonal_matrix: np.array) -> np.array:
    copy = np.copy(matrix)
    for i, b_vec in enumerate(copy):
        copy[i] = copy[i] * diagonal_matrix[i]
    return copy


def projected_representation(matrix: np.array, vec: np.array) -> np.array:
    """
    :param matrix: matrix (M) with orthogonal rows
    :param vec: vector with domain equals to a column label set of M
    :return: coord repr of the projection x onto the Row M in terms of rows of M
    """
    u, e, v = np.linalg.svd(matrix.T, full_matrices=False)
    x = multiply_by_diagonal_matrix(v, np.array(list(map(lambda x: math.pow(x, -1), e)))).dot(u.T).dot(vec)
    return x


def projection_length_squared(matrix: np.array, vec: np.array) -> np.array:
    """
    :param matrix: matrix (M) with orthogonal rows
    :param vec: vector with domain equals to a column label set of M
    :return: squared norm of the projection of x into the Row M
    """
    proj_vec = projected_representation(matrix, vec)
    return np.dot(proj_vec, proj_vec)


def distance_squared(matrix: np.array, vec: np.array) -> np.array:
    """
    :param matrix: matrix (M) with orthogonal rows
    :param vec: vector with domain equals to a column label set of M
    :return: squared norm of the distance from vec to Row M
    """
    proj_len = projection_length_squared(matrix, vec)
    vec_len = np.dot(vec, vec)
    return vec_len - proj_len


def project(matrix: np.array, vec: np.array) -> np.array:
    """
    :param matrix: matrix (M) with orthogonal rows
    :param vec: vector with domain equals to a column label set of M
    :return: projection of vec into the Row M
    """
    print(matrix.shape)
    print(projected_representation(matrix, vec).shape)
    return np.dot(matrix.T, projected_representation(matrix, vec))


def normalize(matrix: np.array) -> np.array:
    """
    :param matrix: matrix to normalize
    :return: matrix normalized to be a source for an image
    """
    min = np.amin(matrix)
    max = np.amax(matrix)
    return (matrix - min) * 255.0 / (max - min)
