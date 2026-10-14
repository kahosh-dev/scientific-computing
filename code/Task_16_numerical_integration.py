import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.integrate import simpson

time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])

energy_trapezoid = np.trapezoid(power_kw, time_hours)
energy_simpson = simpson(power_kw, x=time_hours)
print(f"Energy using trapezoidal rule: {energy_trapezoid:.3f} kWh")
print(f"Energy using Simpson's rule: {energy_simpson:.3f} kWh")
print(f"Difference between estimates: {abs(energy_simpson-energy_trapezoid):.3f} kWh")

# --- Experiment: test both rules on a known integral, sin(x) from 0 to pi (exact = 2) ---
print("\n[Experiment] integral of sin(x) on [0, pi], exact value 2")
ns = [3, 5, 9, 17, 33]
et, es = [], []
for n in ns:
    x = np.linspace(0, np.pi, n)
    t_ = np.trapezoid(np.sin(x), x); s_ = simpson(np.sin(x), x=x)
    et.append(abs(t_ - 2)); es.append(abs(s_ - 2))
    print(f"n={n:2d}: trapezoid error {et[-1]:.2e}, Simpson error {es[-1]:.2e}")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(time_hours, power_kw, marker="o"); ax[0].fill_between(time_hours, power_kw, alpha=0.3)
ax[0].set_xlabel("Time (h)"); ax[0].set_ylabel("Power (kW)"); ax[0].set_title("Area = energy used"); ax[0].grid(True)
ax[1].loglog(ns, et, "o-", label="Trapezoid"); ax[1].loglog(ns, es, "s-", label="Simpson")
ax[1].set_xlabel("Number of points"); ax[1].set_ylabel("Absolute error"); ax[1].legend(); ax[1].grid(True, which="both")
ax[1].set_title("Accuracy on sin(x)")
plt.savefig(os.path.join(FIG, "task16_integration.png"), dpi=150, bbox_inches="tight")
