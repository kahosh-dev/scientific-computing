import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

# New case: logistic population growth, dP/dt = r P (1 - P/K)
# Fish in a pond: P0 = 50, r = 0.4 per month, carrying capacity K = 1000.
r, K, P0, end = 0.4, 1000.0, 50.0, 24.0

def euler(h):
    t = np.arange(0, end + h, h)
    P = np.zeros_like(t); P[0] = P0
    for i in range(len(t) - 1):
        P[i + 1] = P[i] + h * r * P[i] * (1 - P[i] / K)
    exact = K / (1 + (K / P0 - 1) * np.exp(-r * t))
    return t, P, exact

for h in (4.0, 1.0, 0.25):
    t, P, ex = euler(h)
    print(f"h={h}: P(24) = {P[-1]:.2f}, exact {ex[-1]:.2f}, max error {np.max(np.abs(P-ex)):.2f}")

t, P, ex = euler(1.0)
half = t[np.argmax(P >= K/2)]
print(f"Population first passes K/2 = 500 at about month {half:.0f} (exact {np.log(K/P0-1)/r:.1f})")
