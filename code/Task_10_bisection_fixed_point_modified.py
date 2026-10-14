import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.optimize import root_scalar

# New case: a loan of 5,000 is repaid with 24 monthly payments of 235.
# What monthly interest rate r does the lender charge?
# Payment formula: pay = P * r / (1 - (1+r)^-n)  ->  solve f(r) = 0
P, n, pay = 5000.0, 24, 235.0

def f(r):
    return P * r / (1 - (1 + r)**(-n)) - pay

sol = root_scalar(f, bracket=[1e-6, 0.10], method="bisect", xtol=1e-12)
r = sol.root
print(f"Monthly rate: {r:.6%}   (found in {sol.iterations} bisection steps)")
print(f"Nominal annual rate: {12*r:.3%}")
print(f"Effective annual rate: {(1+r)**12 - 1:.3%}")
print(f"Total repaid: {n*pay:.2f}, interest paid: {n*pay-P:.2f}")

# Fixed-point version: r = (pay/P) * (1 - (1+r)^-n)
r_fp = 0.01
for k in range(1, 500):
    r_new = (pay / P) * (1 - (1 + r_fp)**(-n))
    if abs(r_new - r_fp) < 1e-12:
        break
    r_fp = r_new
print(f"Fixed-point rate: {r_fp:.6%} after {k} iterations")
