import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

calculated = 0.1 + 0.2
expected = 0.3
print("0.1 + 0.2 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:", np.isclose(calculated, expected))

true_value = np.sqrt(2)
approx_value = 1.414
absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)
print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")

xs = [1e-4, 1e-8, 1e-12]
for x in xs:
    direct = (np.sqrt(1 + x) - 1) / x
    stable = 1 / (np.sqrt(1 + x) + 1)
    print(f"x={x:.0e}: direct={direct:.12f}, stable={stable:.12f}")

# --- Experiment: push x much smaller and measure the relative error of 'direct' ---
print("\n[Experiment] smaller x and relative error of the direct formula")
xs2 = np.array([1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14, 1e-15])
direct = (np.sqrt(1 + xs2) - 1) / xs2
stable = 1 / (np.sqrt(1 + xs2) + 1)
rel = np.abs(direct - stable) / np.abs(stable)
for x, d, s, r in zip(xs2, direct, stable, rel):
    print(f"x={x:.0e}: direct={d:.12f}, stable={s:.12f}, rel. error={r:.2e}")

plt.loglog(xs2, rel + 1e-18, marker="o")
plt.xlabel("x"); plt.ylabel("Relative error of direct formula")
plt.title("Cancellation error grows as x shrinks")
plt.grid(True, which="both")
plt.savefig(os.path.join(FIG, "task04_cancellation.png"), dpi=150, bbox_inches="tight")
