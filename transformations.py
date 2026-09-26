import numpy as np


def translation_matrix(tx, ty, tz):
    """
    Create a 4x4 translation matrix.
    """

    return np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])