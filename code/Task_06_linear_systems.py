import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

# x = Type A servers, y = Type B servers
# Type A: 4 CPU, 8 GB   Type B: 2 CPU, 12 GB
A = np.array([[4.0, 2.0], [8.0, 12.0]])
b = np.array([20.0, 72.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution
print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))

# --- Experiment: new totals, 24 CPU units and 80 GB ---
b2 = np.array([24.0, 80.0])
s2 = np.linalg.solve(A, b2)
print("\n[Experiment] totals 24 CPU / 80 GB ->", s2)

# Graph: each equation is a line, the solution is where they cross
xs = np.linspace(0, 6, 100)
plt.plot(xs, (20 - 4*xs)/2, label="CPU: 4x + 2y = 20")
plt.plot(xs, (72 - 8*xs)/12, label="Memory: 8x + 12y = 72")
plt.plot(*solution, "ko", label=f"Solution ({solution[0]:.0f}, {solution[1]:.0f})")
plt.xlabel("Type A servers (x)"); plt.ylabel("Type B servers (y)")
plt.ylim(0, 10); plt.legend(); plt.grid(True)
plt.title("Two resource equations meet at one point")
plt.savefig(os.path.join(FIG, "task06_lines.png"), dpi=150, bbox_inches="tight")
