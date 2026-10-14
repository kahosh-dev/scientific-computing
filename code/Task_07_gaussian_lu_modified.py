import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.linalg import lu_factor, lu_solve

# New case: a chain of 4 masses joined by springs and fixed to a wall (stiffness in N/m).
# K u = f gives the displacement u (m) for a load f (N). K stays the same, loads change.
k = 200.0
K = k * np.array([
    [ 2., -1.,  0.,  0.],
    [-1.,  2., -1.,  0.],
    [ 0., -1.,  2., -1.],
    [ 0.,  0., -1.,  1.]
])
loads = {
    "light load": np.array([0., 0., 0., 10.]),
    "middle load": np.array([0., 20., 0., 0.]),
    "all masses": np.array([5., 5., 5., 5.]),
}
lu, piv = lu_factor(K)
P, L, U = __import__("scipy.linalg", fromlist=["lu"]).lu(K)
print("L =\n", np.round(L, 3))
print("U =\n", np.round(U, 3))
for name, f in loads.items():
    u = lu_solve((lu, piv), f)
    print(f"{name}: displacements (mm) = {np.round(u*1000, 3)}, residual {np.linalg.norm(f-K@u):.1e}")
