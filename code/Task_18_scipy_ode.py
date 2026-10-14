import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.integrate import solve_ivp

def charge(Vs, R, C, T=5.0, V0=0.0):
    f = lambda t, V: [(Vs - V[0]) / (R * C)]
    t_eval = np.linspace(0, T, 200)
    sol = solve_ivp(f, (0, T), [V0], t_eval=t_eval, rtol=1e-9, atol=1e-11)
    exact = Vs + (V0 - Vs) * np.exp(-sol.t / (R * C))
    return sol, exact

sol, exact = charge(5.0, 1000.0, 0.001)
print("Solver success:", sol.success)
print(f"Capacitor voltage at 5 s: {sol.y[0, -1]:.4f} V")
print(f"Maximum error against exact solution: {np.max(np.abs(sol.y[0]-exact)):.3e} V")

# --- Experiment: double the resistance (time constant 1 s -> 2 s) ---
sol2, exact2 = charge(5.0, 2000.0, 0.001)
tau1, tau2 = 1.0, 2.0
print("\n[Experiment] R = 2000 ohm")
print(f"Voltage at 1 s: before {np.interp(1, sol.t, sol.y[0]):.3f} V, after {np.interp(1, sol2.t, sol2.y[0]):.3f} V")
print(f"Voltage at 5 s: {sol2.y[0, -1]:.4f} V")
print(f"Theory: V(tau) = 0.632*Vs = {0.632*5:.3f} V")

plt.plot(sol.t, sol.y[0], label="R = 1000 ohm (solve_ivp)")
plt.plot(sol.t, exact, "k--", label="Exact")
plt.plot(sol2.t, sol2.y[0], label="R = 2000 ohm")
plt.axhline(5, color="grey", linewidth=0.7)
plt.xlabel("Time (s)"); plt.ylabel("Capacitor voltage (V)")
plt.title("RC circuit charging"); plt.legend(); plt.grid(True)
plt.savefig(os.path.join(FIG, "task18_rc.png"), dpi=150, bbox_inches="tight")
