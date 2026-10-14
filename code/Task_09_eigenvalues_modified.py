import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

# New case: friendship network of 6 students. Who is the most influential?
names = ["Amina", "Brian", "Cynthia", "Dennis", "Esther", "Felix"]
edges = [(0,1),(0,2),(1,2),(2,3),(3,4),(3,5),(4,5),(2,4)]
A = np.zeros((6, 6))
for i, j in edges:
    A[i, j] = A[j, i] = 1

vals, vecs = np.linalg.eig(A)
i = np.argmax(vals.real)
v = np.abs(vecs[:, i].real)
score = v / v.sum()
degree = A.sum(axis=1)

print("Dominant eigenvalue:", round(vals[i].real, 4))
print(f"{'Name':8s} {'Links':>5s} {'Eigenvector score':>18s}")
for n, d, s in sorted(zip(names, degree, score), key=lambda t: -t[2]):
    print(f"{n:8s} {int(d):5d} {s:18.4f}")
print("Eigenvalues sorted:", np.round(np.sort(vals.real)[::-1], 3))
