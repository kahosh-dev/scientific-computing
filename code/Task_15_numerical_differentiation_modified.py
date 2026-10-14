import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

# New case: a car's speed (km/h) is logged every 2 s while accelerating.
# Estimate acceleration in m/s^2 with np.gradient (central differences inside, one-sided at ends).
t = np.arange(0, 22, 2, dtype=float)
v_kmh = np.array([0, 12, 25, 40, 52, 61, 68, 73, 76, 77.5, 78])
v = v_kmh / 3.6
a = np.gradient(v, t)

for ti, vi, ai in zip(t, v, a):
    print(f"t={ti:4.0f}s  v={vi:5.2f} m/s  a={ai:5.2f} m/s^2")
i = np.argmax(a)
print(f"Peak acceleration {a[i]:.2f} m/s^2 at t={t[i]:.0f} s")
print(f"Average acceleration over the run: {(v[-1]-v[0])/(t[-1]-t[0]):.2f} m/s^2")
