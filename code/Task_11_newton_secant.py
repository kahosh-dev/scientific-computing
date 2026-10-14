import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.optimize import root_scalar

def make(cash_flows):
    npv = lambda rate: sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))
    d_npv = lambda rate: sum(-t * cf / (1 + rate)**(t + 1) for t, cf in enumerate(cash_flows) if t > 0)
    return npv, d_npv

def irr(cash_flows, x0=0.10):
    npv, d_npv = make(cash_flows)
    newton = root_scalar(npv, fprime=d_npv, x0=x0, method="newton", xtol=1e-12)
    secant = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)
    bis = root_scalar(npv, bracket=[0.0, 1.0], method="bisect", xtol=1e-12)
    return newton, secant, bis

cash_flows = [-10000, 3000, 3500, 4000, 2500]
npv, d_npv = make(cash_flows)
newton, secant, bis = irr(cash_flows)
print(f"IRR using Newton-Raphson: {newton.root:.6%}  ({newton.iterations} iterations)")
print(f"IRR using Secant method: {secant.root:.6%}  ({secant.iterations} iterations)")
print(f"IRR using Bisection (for comparison): {bis.root:.6%}  ({bis.iterations} iterations)")
print(f"NPV at Newton solution: {npv(newton.root):.6f}")

# --- Experiment: bigger inflow in year 4 and a worse starting guess ---
cf2 = [-10000, 3000, 3500, 4000, 4500]
n2, s2, b2 = irr(cf2, x0=0.5)
print(f"\n[Experiment] last inflow 4500, x0=0.5 -> Newton {n2.root:.4%}, Secant {s2.root:.4%}")

r = np.linspace(0, 0.4, 200)
plt.plot(r*100, [npv(x) for x in r], label="original")
plt.plot(r*100, [make(cf2)[0](x) for x in r], label="year-4 inflow 4500")
plt.axhline(0, color="k", linewidth=0.8)
plt.xlabel("Discount rate (%)"); plt.ylabel("NPV")
plt.title("NPV against discount rate"); plt.legend(); plt.grid(True)
plt.savefig(os.path.join(FIG, "task11_npv.png"), dpi=150, bbox_inches="tight")
