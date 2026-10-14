import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.optimize import root

def solve_all(R, guesses):
    eq = lambda z: [z[0]**2 + z[1]**2 - R**2, z[1] - (z[0]**2 - 1)]
    out = []
    for g in guesses:
        s = root(eq, g)
        out.append((g, s.x, eq(s.x), s.success))
    return out

for g, x, res, ok in solve_all(2.0, ([1.0, 1.0], [-1.0, 1.0])):
    print("Initial guess:", g)
    print("Intersection:", x)
    print("Residuals:", [float(r) for r in res])
    print("Converged:", ok)
    print()

# Algebra check: with u = x^2, u^2 - u - 3 = 0, so x = +-sqrt((1+sqrt(13))/2)
u = (1 + np.sqrt(13)) / 2
print("Exact x:", np.sqrt(u), " exact y:", u - 1)

# --- Experiment: smaller circle, radius 1.5, plus a poor guess near the origin ---
print("\n[Experiment] radius 1.5")
for g, x, res, ok in solve_all(1.5, ([1.0, 1.0], [-1.0, 1.0], [0.0, 0.0])):
    print("guess", g, "->", np.round(x, 5), "converged:", ok)

th = np.linspace(0, 2*np.pi, 400)
xs = np.linspace(-2.2, 2.2, 400)
plt.plot(2*np.cos(th), 2*np.sin(th), label="Circle r=2")
plt.plot(1.5*np.cos(th), 1.5*np.sin(th), label="Circle r=1.5")
plt.plot(xs, xs**2 - 1, label="Parabola")
for R in (2.0, 1.5):
    for _, x, _, _ in solve_all(R, ([1.0, 1.0], [-1.0, 1.0])):
        plt.plot(*x, "ko")
plt.axis("equal"); plt.ylim(-2.5, 2.5); plt.grid(True); plt.legend()
plt.title("Circle and parabola intersections")
plt.savefig(os.path.join(FIG, "task12_intersections.png"), dpi=150, bbox_inches="tight")
