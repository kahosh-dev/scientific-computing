import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
import time
from scipy.linalg import lu_factor, lu_solve

A = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 3.0]])
measurement_sets = [np.array([15.0, 10.0, 10.0]),
                    np.array([16.0, 11.0, 9.0]),
                    np.array([14.0, 12.0, 11.0])]

lu, piv = lu_factor(A)
for i, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)
    residual = b - A @ x
    print(f"Measurement set {i}")
    print("Solution:", x)
    print("Residual norm:", np.linalg.norm(residual))
    print()
print("Direct solution for first set:", np.linalg.solve(A, measurement_sets[0]))

# --- Experiment: a bigger matrix (400 x 400) and 500 right-hand sides ---
rng = np.random.default_rng(1)
n, m = 400, 500
A_big = rng.random((n, n)) + n * np.eye(n)
B = rng.random((n, m))

t0 = time.perf_counter()
for j in range(m):
    np.linalg.solve(A_big, B[:, j])
t_solve = time.perf_counter() - t0

t0 = time.perf_counter()
lu_b, piv_b = lu_factor(A_big)
for j in range(m):
    lu_solve((lu_b, piv_b), B[:, j])
t_lu = time.perf_counter() - t0
print(f"\n[Experiment] {m} solves, {n}x{n}: solve each time {t_solve:.3f}s, LU once {t_lu:.3f}s, ratio {t_solve/t_lu:.1f}x")

x_all = np.array([lu_solve((lu, piv), b) for b in measurement_sets])
width = 0.25
for k in range(3):
    plt.bar(np.arange(3) + k*width, x_all[:, k], width, label=f"x{k+1}")
plt.xticks(np.arange(3) + width, ["Set 1", "Set 2", "Set 3"])
plt.ylabel("Solution value"); plt.legend(); plt.grid(True, axis="y")
plt.title("Solutions for three measurement vectors (A factored once)")
plt.savefig(os.path.join(FIG, "task07_solutions.png"), dpi=150, bbox_inches="tight")
