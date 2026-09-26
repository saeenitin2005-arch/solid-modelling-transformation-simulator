import matplotlib.pyplot as plt
import math


# ==========================================
# ROTATION FUNCTIONS
# ==========================================

def rotate_x(x, y, z, angle):
    """
    Rotate a point around the X-axis.
    """

    new_x = x

    new_y = (
        y * math.cos(angle)
        - z * math.sin(angle)
    )

    new_z = (
        y * math.sin(angle)
        + z * math.cos(angle)
    )

    return new_x, new_y, new_z


def rotate_y(x, y, z, angle):
    """
    Rotate a point around the Y-axis.
    """

    new_x = (
        x * math.cos(angle)
        + z * math.sin(angle)
    )

    new_y = y

    new_z = (
        -x * math.sin(angle)
        + z * math.cos(angle)
    )

    return new_x, new_y, new_z


def rotate_z(x, y, z, angle):
    """
    Rotate a point around the Z-axis.
    """

    new_x = (
        x * math.cos(angle)
        - y * math.sin(angle)
    )

    new_y = (
        x * math.sin(angle)
        + y * math.cos(angle)
    )

    new_z = z

    return new_x, new_y, new_z


# ==========================================
# ORIGINAL CUBE
# ==========================================

x = [0, 1, 1, 0, 0, 1, 1, 0]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 0, 0, 0, 1, 1, 1, 1]


# Cube edges

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]


# ==========================================
# ROTATION SETTINGS
# ==========================================

angle_degrees = 45

angle = math.radians(angle_degrees)


# ==========================================
# ROTATE ALL CUBE VERTICES
# ==========================================

x_rotated = []
y_rotated = []
z_rotated = []


for i in range(len(x)):

    new_x, new_y, new_z = rotate_z(
        x[i],
        y[i],
        z[i],
        angle
    )

    x_rotated.append(new_x)
    y_rotated.append(new_y)
    z_rotated.append(new_z)


# ==========================================
# CREATE 3D VIEW
# ==========================================

fig = plt.figure(figsize=(10, 7))

ax = fig.add_subplot(
    111,
    projection="3d"
)


# ==========================================
# DRAW ORIGINAL CUBE
# ==========================================

for start, end in edges:

    ax.plot(
        [x[start], x[end]],
        [y[start], y[end]],
        [z[start], z[end]],
        linewidth=2
    )


# ==========================================
# DRAW ROTATED CUBE
# ==========================================

for start, end in edges:

    ax.plot(
        [x_rotated[start], x_rotated[end]],
        [y_rotated[start], y_rotated[end]],
        [z_rotated[start], z_rotated[end]],
        linewidth=2
    )


# ==========================================
# LABELS
# ==========================================

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

ax.set_title(
    "3D Solid Modelling - Rotation"
)


# ==========================================
# DISPLAY
# ==========================================

plt.show()