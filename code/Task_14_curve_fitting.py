import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.optimize import curve_fit

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)

def model(x, a, b, c):
    return a*x**2 + b*x + c

parameters, covariance = curve_fit(model, users, response_ms)
a, b, c = parameters
predicted = model(users, a, b, c)
rmse = np.sqrt(np.mean((response_ms - predicted)**2))
print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 400 users: {model(400, a, b, c):.2f} ms")

# --- Experiment: compare a straight line, the quadratic and a cubic ---
print("\n[Experiment] degree comparison")
fits = {}
for deg in (1, 2, 3):
    p = np.polyfit(users, response_ms, deg)
    r = np.sqrt(np.mean((response_ms - np.polyval(p, users))**2))
    fits[deg] = p
    print(f"degree {deg}: RMSE {r:.2f} ms, prediction at 400 users {np.polyval(p, 400):.1f} ms")

x_plot = np.linspace(users.min(), 400, 300)
plt.scatter(users, response_ms, label="Measurements", zorder=3)
plt.plot(x_plot, model(x_plot, a, b, c), label="Quadratic fit")
plt.plot(x_plot, np.polyval(fits[1], x_plot), "--", label="Straight line")
plt.plot(x_plot, np.polyval(fits[3], x_plot), ":", label="Cubic")
plt.xlabel("Concurrent users"); plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting"); plt.legend(); plt.grid(True)
plt.savefig(os.path.join(FIG, "task14_curve_fit.png"), dpi=150, bbox_inches="tight")
