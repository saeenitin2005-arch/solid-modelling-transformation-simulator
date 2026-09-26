import numpy as np
import math


def translation_matrix(tx, ty, tz):
    """Create a 4x4 translation matrix."""

    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ], dtype=float)


def scaling_matrix(sx, sy, sz):
    """Create a 4x4 scaling matrix."""

    return np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ], dtype=float)


def rotation_x_matrix(angle_degrees):
    """Create a 4x4 X-axis rotation matrix."""

    angle = math.radians(angle_degrees)

    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(angle), -math.sin(angle), 0],
        [0, math.sin(angle), math.cos(angle), 0],
        [0, 0, 0, 1]
    ], dtype=float)


def rotation_y_matrix(angle_degrees):
    """Create a 4x4 Y-axis rotation matrix."""

    angle = math.radians(angle_degrees)

    return np.array([
        [math.cos(angle), 0, math.sin(angle), 0],
        [0, 1, 0, 0],
        [-math.sin(angle), 0, math.cos(angle), 0],
        [0, 0, 0, 1]
    ], dtype=float)


def rotation_z_matrix(angle_degrees):
    """Create a 4x4 Z-axis rotation matrix."""

    angle = math.radians(angle_degrees)

    return np.array([
        [math.cos(angle), -math.sin(angle), 0, 0],
        [math.sin(angle), math.cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], dtype=float)