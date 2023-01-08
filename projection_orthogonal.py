import matplotlib.pyplot as plt
import numpy as np

O = np.array([0, 0, 0])


def draw_vector(axes, vec: np.array, color):
    axes.quiver(O[0], O[1], O[2], vec[0], vec[1], vec[2], color=color)


def get_sigma(b_vec, v_vec) -> float:
    return np.dot(b_vec, v_vec) / np.dot(v_vec, v_vec)


def projection_orthogonal(b_vec: np.array, v_vecs: np.array) -> np.array:
    projections_along = list(map(lambda v: get_sigma(b_vec, v) * v, v_vecs))
    print(f"Projections along v_vecs: {projections_along}")
    projections_along_sum = np.add.reduce(projections_along)
    print(f"Sum on projections along v_vecs: {projections_along_sum}")
    return b_vec - projections_along_sum


b = np.array([1, 1, 1])
v1 = np.array([0, 2, 2])
v2 = np.array([0, 1, -1])


pr_ort = projection_orthogonal(b, np.array([v1, v2]))
print(f"Projection orthogonal to v_vecs: {pr_ort}")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
draw_vector(ax, v1, "r")
draw_vector(ax, v2, "r")
draw_vector(ax, b, "g")
draw_vector(ax, pr_ort, "b")
ax.set_xlim([-1, 4])
ax.set_ylim([-1, 4])
ax.set_zlim([-1, 4])
plt.show()

