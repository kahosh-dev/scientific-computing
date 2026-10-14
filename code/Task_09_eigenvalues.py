import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

def centrality(A):
    vals, vecs = np.linalg.eig(A)
    i = np.argmax(np.real(vals))
    v = np.abs(np.real(vecs[:, i]))
    return np.real(vals[i]), v / v.sum(), np.real(vecs[:, i])

A = np.array([[0., 1., 1., 0.],
              [1., 0., 1., 1.],
              [1., 1., 0., 1.],
              [0., 1., 1., 0.]])
nodes = ["A", "B", "C", "D"]

lam, c, v = centrality(A)
print("Dominant eigenvalue:", lam)
print("Eigenvector-based importance:")
for n, s in zip(nodes, c):
    print(f"{n}: {s:.4f}")
print("Verification error:", np.linalg.norm(A @ v - lam * v))

# --- Experiment: add a link between A and D ---
A2 = A.copy(); A2[0, 3] = A2[3, 0] = 1
lam2, c2, _ = centrality(A2)
print("\n[Experiment] added link A-D")
print("Dominant eigenvalue:", round(lam2, 4))
for n, s in zip(nodes, c2):
    print(f"{n}: {s:.4f}")

x = np.arange(4)
plt.bar(x - 0.2, c, 0.4, label="Original network")
plt.bar(x + 0.2, c2, 0.4, label="With A-D link")
plt.xticks(x, nodes); plt.ylabel("Importance share"); plt.legend()
plt.title("Eigenvector-based node importance")
plt.savefig(os.path.join(FIG, "task09_centrality.png"), dpi=150, bbox_inches="tight")
