import numpy as np
import galois

GF = galois.GF(2)


def choose_secret_vector(a_base, b_base, s1, s2) -> np.array:
    while True:
        vec = np.random.randint(2, size=6).view(GF)
        if np.dot(a_base, vec) == s1 and np.dot(b_base, vec) == s2:
            return vec


# def get_ta_bits


def generate_linearly_independent_pairs(pairs) -> np.array:
    assert len(pairs) <= 4
    while len(pairs) < 4:
        probed_vectors = (np.random.randint(2, size=6), np.random.randint(2, size=6))



if __name__ == '__main__':
    base_pair = (np.array([1, 1, 0, 1, 0, 1]).view(GF), np.array([1, 0, 0, 0, 1, 0]).view(GF))
    ta_1_pair = (np.array([0, 0, 1, 0, 0, 0]).view(GF), np.array([0, 1, 1, 0, 0, 1]).view(GF))
    ta_2_pair = (np.array([0, 0, 0, 0, 1, 0]).view(GF), np.array([1, 0, 1, 0, 1, 1]).view(GF))
    ta_3_pair = (np.array([0, 1, 0, 1, 0, 1]).view(GF), np.array([1, 1, 0, 1, 0, 0]).view(GF))
    ta_4_pair = (np.array([1, 0, 0, 0, 1, 0]).view(GF), np.array([0, 0, 1, 0, 0, 1]).view(GF))

    secret = choose_secret_vector(base_pair[0], base_pair[1], 1, 1)
    print(f"Secret: {secret}")
    ta_1_shares = (np.dot(ta_1_pair[0], secret), np.dot(ta_1_pair[1], secret))
    ta_2_shares = (np.dot(ta_2_pair[0], secret), np.dot(ta_2_pair[1], secret))
    ta_3_shares = (np.dot(ta_3_pair[0], secret), np.dot(ta_3_pair[1], secret))
    ta_4_shares = (np.dot(ta_4_pair[0], secret), np.dot(ta_4_pair[1], secret))

    ta_matrix = np.array([
        ta_1_pair[0],
        ta_1_pair[1],
        ta_3_pair[0],
        ta_3_pair[1],
        ta_4_pair[0],
        ta_4_pair[1],
    ]).view(GF)
    const = np.array([
        ta_1_shares[0],
        ta_1_shares[1],
        ta_3_shares[0],
        ta_3_shares[1],
        ta_4_shares[0],
        ta_4_shares[1],
    ]).view(GF)
    print(ta_matrix)
    print(const)
    res = np.linalg.solve(ta_matrix, const)
    print(res)

    # secret_matrix = np.array([
    #     choose_secret_vector(base_pair[0], base_pair[1], 0, 0),
    #     choose_secret_vector(base_pair[0], base_pair[1], 0, 0),
    #     choose_secret_vector(base_pair[0], base_pair[1], 1, 1),
    #     choose_secret_vector(base_pair[0], base_pair[1], 0, 0),
    # ]).view(GF).T
    # print(secret_matrix)
    # ta_vectors = np.array([
    #     base_pair[0],
    #     base_pair[1],
    #     ta_1_pair[0],
    #     ta_1_pair[1],
    #     ta_2_pair[0],
    #     ta_2_pair[1],
    #     ta_3_pair[0],
    #     ta_3_pair[1],
    #     ta_4_pair[0],
    #     ta_4_pair[1]
    # ]).view(GF)
    #
    # shares = np.dot(ta_vectors, secret_matrix).view(GF)
    # print("Shares:")
    # print(shares)

    # ta_1_bit = np.dot()


    # print(np.linalg.lstsq(np.array([a_base]).view(GF), np.array([1]).view(GF)))
