import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

points = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])

def transform(points, angle_deg, sx, sy):
    angle = np.deg2rad(angle_deg)
    rotation = np.array([[np.cos(angle), -np.sin(angle)],
                         [np.sin(angle),  np.cos(angle)]])
    scale = np.array([[sx, 0.0], [0.0, sy]])
    T = rotation @ scale
    return points @ T.T, T

transformed_points, T = transform(points, 45, 2.0, 1.5)
print("Original points:\n", points)
print("Transformation matrix:\n", T)
print("Transformed points:\n", transformed_points)
print("Determinant:", np.linalg.det(T))

# --- Experiment: change angle to 90 degrees and scale to (1, 3) ---
t2, T2 = transform(points, 90, 1.0, 3.0)
print("\n[Experiment] 90 deg, scale (1, 3)")
print("Transformed points:\n", np.round(t2, 3))
print("Determinant:", round(np.linalg.det(T2), 3))

def closed(p):
    return np.vstack([p, p[0]])

for p, lab, st in [(points, "Original", "k-"), (transformed_points, "45 deg, scale (2, 1.5)", "r-"),
                   (t2, "90 deg, scale (1, 3)", "b--")]:
    q = closed(p)
    plt.plot(q[:, 0], q[:, 1], st, label=lab)
plt.axis("equal"); plt.grid(True); plt.legend()
plt.title("Unit square before and after transformation")
plt.savefig(os.path.join(FIG, "task05_transform.png"), dpi=150, bbox_inches="tight")
