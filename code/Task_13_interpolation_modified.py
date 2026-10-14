import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.interpolate import interp1d, CubicSpline

# New case: calibration table of a pressure sensor (output voltage -> pressure in kPa).
volts = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
kpa = np.array([0.0, 12.5, 26.0, 41.0, 57.5, 74.0, 90.0, 104.0, 115.0])

lin = interp1d(volts, kpa)
spl = CubicSpline(volts, kpa)

for v in (1.25, 2.75, 3.9):
    print(f"{v:.2f} V -> linear {float(lin(v)):.2f} kPa, spline {float(spl(v)):.2f} kPa")

# Leave-one-out check: hide each interior point and predict it
errs_l, errs_s = [], []
for i in range(1, len(volts) - 1):
    m = np.arange(len(volts)) != i
    errs_l.append(abs(float(interp1d(volts[m], kpa[m])(volts[i])) - kpa[i]))
    errs_s.append(abs(float(CubicSpline(volts[m], kpa[m])(volts[i])) - kpa[i]))
print(f"Mean leave-one-out error: linear {np.mean(errs_l):.3f} kPa, spline {np.mean(errs_s):.3f} kPa")
