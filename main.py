import matplotlib.pyplot as plt
import numpy as np

from transformations import (
    translation_matrix,
    scaling_matrix,
    rotation_z_matrix
)


# ==========================================
# 1. CREATE CUBE VERTICES
# ==========================================

vertices = np.array([
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
], dtype=float)


# ==========================================
# 2. CUBE EDGES
# ==========================================

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]


# ==========================================
# 3. CREATE TRANSFORMATION MATRICES
# ==========================================

translation = translation_matrix(2, 1, 1)

scaling = scaling_matrix(2, 2, 2)

rotation = rotation_z_matrix(45)


# ==========================================
# 4. COMBINE TRANSFORMATIONS
# ==========================================

transformation = translation @ rotation @ scaling


# ==========================================
# 5. APPLY TRANSFORMATION
# ==========================================

transformed_vertices = (
    transformation @ vertices.T
).T


# ==========================================
# 6. CREATE 3D VIEW
# ==========================================

fig = plt.figure(figsize=(10, 7))

ax = fig.add_subplot(
    111,
    projection="3d"
)


# ==========================================
# 7. DRAW ORIGINAL CUBE
# ==========================================

for start, end in edges:

    ax.plot(
        [vertices[start, 0], vertices[end, 0]],
        [vertices[start, 1], vertices[end, 1]],
        [vertices[start, 2], vertices[end, 2]],
        linewidth=2
    )


# ==========================================
# 8. DRAW TRANSFORMED CUBE
# ==========================================

for start, end in edges:

    ax.plot(
        [
            transformed_vertices[start, 0],
            transformed_vertices[end, 0]
        ],
        [
            transformed_vertices[start, 1],
            transformed_vertices[end, 1]
        ],
        [
            transformed_vertices[start, 2],
            transformed_vertices[end, 2]
        ],
        linewidth=2
    )


# ==========================================
# 9. LABELS
# ==========================================

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

ax.set_title(
    "Solid Modelling Transformation Simulator"
)


# ==========================================
# 10. DISPLAY
# ==========================================

plt.show()