from PIL import Image
import numpy as np
from image_util import normalize
import matplotlib.pyplot as plt


def get_low_rank_approximation(left_sing_vecs: np.array, sing_values: np.array, right_sing_vecs: np.array, rank: int) -> np.array:
    n_left_singular_vecs = left_sing_vecs[0:left_sing_vecs.shape[1], 0:rank]
    n_right_singular_vecs = right_sing_vecs[0:rank, 0:right_sing_vecs.shape[0]]
    n_singular_values_array = sing_values[0:rank, 0:rank]
    return n_left_singular_vecs.dot(n_singular_values_array.dot(n_right_singular_vecs))


def get_rms_plot_data(original_matrix: np.array, left_sing_vecs: np.array, sing_values: np.array, right_sing_vecs: np.array) -> np.array:
    low_rank_approximations = map(
        lambda i: get_low_rank_approximation(left_sing_vecs, sing_values, right_sing_vecs, i), range(1, sing_values.shape[1])
    )
    diff = map(lambda apprx: original_matrix - apprx, low_rank_approximations)
    rms = map(lambda diff_val: np.sqrt(np.mean(diff_val**2)), diff)
    return np.array(list(rms))


IMG_PATH = "image_svd/penguin.png"
singular_value_power_threshold = 0.7

img_vec = np.asarray(Image.open(IMG_PATH))
print(img_vec.shape)

left_singular_vecs, singular_values, right_singular_vecs = np.linalg.svd(img_vec)
print(left_singular_vecs.shape)
print(singular_values.shape)
print(right_singular_vecs.shape)

singular_values_array = np.zeros((img_vec.shape[0], img_vec.shape[1]), int)
np.fill_diagonal(singular_values_array, singular_values)
print(singular_values_array.shape)

schatten_norm = np.sum(singular_values)
normalized_singular_values = map(lambda x: x / schatten_norm * 100, singular_values)
significant_singular_values = np.array(list(filter(lambda y: y > singular_value_power_threshold, normalized_singular_values)))
n = significant_singular_values.shape[0]
print(f"n: {n}")

approximation_vec = get_low_rank_approximation(left_singular_vecs, singular_values_array, right_singular_vecs, n)

img = Image.fromarray(np.uint8(normalize(approximation_vec)), 'L')
img.show()

plt.plot(singular_values)
plt.ylabel('singular value')
plt.show()

# rms_data = get_rms_plot_data(img_vec, left_singular_vecs, singular_values_array, right_singular_vecs)
# plt.plot(rms_data)
# plt.ylabel('rank approximation')
# plt.ylabel('singular value')
# plt.show()
