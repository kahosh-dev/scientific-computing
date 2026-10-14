import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.integrate import simpson

# New case: flow rate (litres/min) into a water tank, measured every 15 minutes for 2 hours.
t_min = np.arange(0, 135, 15, dtype=float)
flow = np.array([20, 26, 31, 35, 33, 28, 22, 18, 15])

vol_trap = np.trapezoid(flow, t_min)
vol_simp = simpson(flow, x=t_min)
print(f"Water collected (trapezoid): {vol_trap:.1f} L")
print(f"Water collected (Simpson):   {vol_simp:.1f} L")
print(f"Difference: {abs(vol_trap-vol_simp):.1f} L")
print(f"Average flow: {vol_simp/(t_min[-1]-t_min[0]):.2f} L/min")

# running total (cumulative) volume
from scipy.integrate import cumulative_trapezoid
cum = cumulative_trapezoid(flow, t_min, initial=0)
for t, c in zip(t_min[::2], cum[::2]):
    print(f"after {t:3.0f} min: {c:7.1f} L")
print("Tank (3000 L) full?", vol_simp >= 3000)
