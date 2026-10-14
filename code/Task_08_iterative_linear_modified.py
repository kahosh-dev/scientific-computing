import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
import os

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

# New case: a metal rod with 19 interior points, ends held at 80 C and 30 C.
n = 19
A = 2*np.eye(n) - np.eye(n, k=1) - np.eye(n, k=-1)
b = np.zeros(n); b[0] = 80; b[-1] = 30

xj, ej = jacobi(A, b, tol=1e-6, max_iter=5000)
xg, eg = gauss_seidel(A, b, tol=1e-6, max_iter=5000)
exact = np.linalg.solve(A, b)
print("Jacobi iterations:", len(ej), "| Gauss-Seidel iterations:", len(eg))
print("Max difference from exact (Gauss-Seidel):", np.abs(xg - exact).max())

pos = np.arange(0, n + 2)
profile = np.concatenate([[80], exact, [30]])
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.plot(pos, profile, marker="o")
plt.xlabel("Position along rod"); plt.ylabel("Temperature (C)")
plt.title("Steady-state temperature along a rod")
plt.grid(True)
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "task08_rod_profile.png"), dpi=150, bbox_inches="tight")
