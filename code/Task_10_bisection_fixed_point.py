import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.optimize import root_scalar

def make_model(amp):
    f = lambda T: T - 25 - amp*np.exp(-T/20)
    g = lambda T: 25 + amp*np.exp(-T/20)
    return f, g

def run(amp, start=30.0):
    f, g = make_model(amp)
    sol = root_scalar(f, bracket=[20, 60], method="bisect", xtol=1e-10)
    T = start; hist = [T]
    for _ in range(200):
        Tn = g(T); hist.append(Tn)
        if abs(Tn - T) < 1e-10:
            break
        T = Tn
    return sol, hist

sol, hist = run(10)
print(f"Bisection equilibrium temperature: {sol.root:.6f} C  ({sol.iterations} iterations)")
print(f"Fixed-point equilibrium temperature: {hist[-1]:.6f} C")
print("Fixed-point iterations:", len(hist) - 1)

# --- Experiment: change the heating term from 10 to 30 ---
sol2, hist2 = run(30)
print(f"\n[Experiment] amplitude 30 -> bisection {sol2.root:.6f} C, "
      f"fixed point {hist2[-1]:.6f} C in {len(hist2)-1} iterations")

f, _ = make_model(10)
f2, _ = make_model(30)
temps = np.linspace(20, 60, 300)
plt.plot(temps, f(temps), label="amplitude 10")
plt.plot(temps, f2(temps), label="amplitude 30")
plt.axhline(0, color="k", linewidth=0.8)
plt.axvline(sol.root, linestyle="--", color="C0"); plt.axvline(sol2.root, linestyle="--", color="C1")
plt.xlabel("Temperature (C)"); plt.ylabel("Heat-balance function f(T)")
plt.title("Equilibrium temperature"); plt.legend(); plt.grid(True)
plt.savefig(os.path.join(FIG, "task10_equilibrium.png"), dpi=150, bbox_inches="tight")
