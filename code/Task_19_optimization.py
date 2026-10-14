import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.optimize import minimize

def solve(cost_a, cost_b, cap_a, cap_b, need):
    cost = lambda z: cost_a*z[0] + cost_b*z[1]
    cons = {"type": "ineq", "fun": lambda z: cap_a*z[0] + cap_b*z[1] - need}
    sol = minimize(cost, x0=[5, 3], method="SLSQP", bounds=[(0, None), (0, None)], constraints=cons)
    best = None
    for a in range(0, 30):
        for b in range(0, 30):
            if cap_a*a + cap_b*b >= need:
                c = cost_a*a + cost_b*b
                if best is None or c < best[0]:
                    best = (c, a, b, cap_a*a + cap_b*b)
    return sol, best

sol, best = solve(12, 18, 100, 170, 1000)
x, y = sol.x
print("Optimization success:", sol.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {100*x + 170*y:.2f}")
print(f"Minimum planning cost: {sol.fun:.2f}")
print("Best nearby integer solution (cost, A, B, capacity):", best)

# --- Experiment: Type B gets more expensive (18 -> 30) ---
sol2, best2 = solve(12, 30, 100, 170, 1000)
print("\n[Experiment] cost of B = 30")
print(f"Continuous: A={sol2.x[0]:.3f}, B={sol2.x[1]:.3f}, cost {sol2.fun:.2f}")
print("Integer best:", best2)
print("Cost per unit of capacity: A =", 12/100, " B(18) =", round(18/170, 4), " B(30) =", round(30/170, 4))

# Feasible region picture
xs = np.linspace(0, 12, 200)
plt.plot(xs, (1000 - 100*xs)/170, label="Capacity = 1000")
for c, ls in ((120, "--"), (160, ":")):
    plt.plot(xs, (c - 12*xs)/18, ls, color="grey", label=f"Cost = {c}")
plt.plot(x, y, "ro", label="Optimum")
plt.fill_between(xs, (1000 - 100*xs)/170, 12, alpha=0.1)
plt.xlim(0, 12); plt.ylim(0, 8)
plt.xlabel("Type A units"); plt.ylabel("Type B units")
plt.title("Feasible region and cost lines"); plt.legend(); plt.grid(True)
plt.savefig(os.path.join(FIG, "task19_optimization.png"), dpi=150, bbox_inches="tight")
