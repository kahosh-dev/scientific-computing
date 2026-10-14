import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

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

A = np.array([[ 2., -1.,  0.,  0.,  0.],
              [-1.,  2., -1.,  0.,  0.],
              [ 0., -1.,  2., -1.,  0.],
              [ 0.,  0., -1.,  2., -1.],
              [ 0.,  0.,  0., -1.,  2.]])
b = np.array([100., 0., 0., 0., 20.])

x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)
print("Jacobi temperatures:", np.round(x_j, 4))
print("Gauss-Seidel temperatures:", np.round(x_gs, 4))
print("Direct solution:", np.round(x_exact, 4))
print("Iterations -> Jacobi:", len(err_j), " Gauss-Seidel:", len(err_gs))

# --- Experiment: loosen the tolerance to 1e-3 and change the right boundary to 50 C ---
_, ej = jacobi(A, b, tol=1e-3)
_, eg = gauss_seidel(A, b, tol=1e-3)
print("\n[Experiment] tol=1e-3 -> Jacobi:", len(ej), " Gauss-Seidel:", len(eg))
b3 = np.array([100., 0., 0., 0., 50.])
print("Right boundary 50 C, exact:", np.round(np.linalg.solve(A, b3), 3))

plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration"); plt.ylabel("Maximum change")
plt.title("Convergence of iterative temperature solution")
plt.legend(); plt.grid(True)
plt.savefig(os.path.join(FIG, "task08_convergence.png"), dpi=150, bbox_inches="tight")
