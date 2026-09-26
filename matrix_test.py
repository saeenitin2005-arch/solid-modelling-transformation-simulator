import numpy as np

from transformations import translation_matrix


# Original point
point = np.array([
    [2],
    [3],
    [4],
    [1]
])


# Create translation matrix
T = translation_matrix(5, 2, 1)


# Apply transformation
new_point = T @ point


print("Translation Matrix:")
print(T)

print("\nOriginal Point:")
print(point)

print("\nTransformed Point:")
print(new_point)