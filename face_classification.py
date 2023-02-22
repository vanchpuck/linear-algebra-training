from PIL import Image
import numpy as np
import os
from functools import reduce
from image_util import distance_squared


FACES_DIR = "faces"
UNCLASSIFIED_DIR = "unclassified"

img_vecs = np.array(list(map(lambda path: np.asarray(Image.open(f'{FACES_DIR}/{path}')).flatten().astype('float'), sorted(os.listdir(FACES_DIR)))))

centroid = reduce(lambda a, b: a + b, img_vecs) / len(img_vecs)

centered_img_vecs = np.array(list(map(lambda img_vec: (img_vec - centroid), img_vecs)))

eigenfaces = np.linalg.svd(centered_img_vecs, full_matrices=False)[2][:10]

uncl_img_vecs = np.array(list(map(lambda path: np.asarray(Image.open(f'{UNCLASSIFIED_DIR}/{path}')).flatten().astype('float'), sorted(os.listdir(UNCLASSIFIED_DIR)))))

centered_uncl_img_vecs = np.array(list(map(lambda img_vec: (img_vec - centroid), uncl_img_vecs)))

print("Faces distances:")
for i, vec in enumerate(centered_img_vecs):
    sqr_dist = distance_squared(eigenfaces, vec)
    print(f"{i} - {sqr_dist}")

print("Unclassified images distances:")
for i, vec in enumerate(centered_uncl_img_vecs):
    sqr_dist = distance_squared(eigenfaces, vec)
    print(f"{i} - {sqr_dist}")
