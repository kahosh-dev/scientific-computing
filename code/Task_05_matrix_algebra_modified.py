import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

# New case: a game sprite (triangle) must be rotated 30 degrees about its own centre,
# then mirrored left-right, as for a character turning around.
sprite = np.array([[0.0, 0.0], [4.0, 0.0], [2.0, 3.0]])
centre = sprite.mean(axis=0)

a = np.deg2rad(30)
R = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
M = np.array([[-1.0, 0.0], [0.0, 1.0]])   # mirror about the y-axis

shifted = sprite - centre
result = (shifted @ R.T) @ M.T + centre
print("Sprite centre:", centre)
print("Transformed sprite:\n", np.round(result, 3))
print("Determinant of R:", round(np.linalg.det(R), 3), "(rotation keeps area)")
print("Determinant of mirror:", np.linalg.det(M), "(negative = orientation flipped)")

# Area check using the shoelace formula
def area(p):
    x, y = p[:, 0], p[:, 1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))
print("Area before:", area(sprite), " after:", round(area(result), 3))
