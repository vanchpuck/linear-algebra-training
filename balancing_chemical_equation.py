import numpy as np
from sympy import *


def get_relation(rref_mtrx, col_idx: int, free_idxs: list):
    col = np.ndarray.flatten(np.array(rref_mtrx.col(col_idx).tolist()))
    row_idx = np.where(col == 1)[0][0]
    row = np.array(rref_mtrx.row(row_idx).tolist()).flatten()

    print(row)
    print(free_idxs)
    print(row[3])
    return col_idx, list(map(lambda idx: -row[idx], free_idxs))


def free_variable_parameters_vector(rref: Matrix, col_idx):
    vector = (np.array(rref.col(col_idx).tolist()).flatten() * -1)[0:shape(rref)[1] - 1]
    vector[col_idx] = 1
    print(vector)
    return vector


# a = (np.array([1, 0, 0, 0, 1]) * -1).tolist()

# Na_3​PO_4​+MgCl_2 ​→ NaCl + Mg_3(PO_4)_2
# Move everytging to the left side and build an augmented matrix
coefs = np.array([
    [3, 1, 4, 0, 0],  # Na_3PO_4
    [0, 0, 0, 1, 2],  # MgCl_2
    (np.array([1, 0, 0, 0, 1]) * -1).tolist(),  # NaCl
    (np.array([0, 2, 8, 3, 0]) * -1).tolist(),  # Mg_3(PO_4)_2
    #------------------
    np.zeros(5)  # constants
]).T
augmented = Matrix(coefs)

rref = augmented.rref()
print(f"RREF: {rref}")
rref_matrix = rref[0]
leading = rref[1]
print(f"Leading: {leading}")
free = list(set(range(0, 4)).difference(set(leading)))
print(f"Free: {free}")
parameters = list(map(lambda col_idx: (col_idx, free_variable_parameters_vector(rref_matrix, col_idx)), free))
print(f"Solution in parametric form: {parameters}")
