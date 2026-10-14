import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.interpolate import interp1d, CubicSpline

hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])

linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)

ten_minute_times = np.arange(8, 14 + 1/6, 1/6)
linear_estimates = linear(ten_minute_times)
cubic_estimates = cubic(ten_minute_times)

target_time = 10.5
print(f"Linear estimate at 10:30: {float(linear(target_time)):.2f} C")
print(f"Cubic estimate at 10:30: {float(cubic(target_time)):.2f} C")

# --- Experiment: remove the 11:00 reading and see how well each method guesses it ---
mask = hours != 11
lin2 = interp1d(hours[mask], temperature[mask])
cub2 = CubicSpline(hours[mask], temperature[mask])
print("\n[Experiment] hide the 11:00 value (true 24.0 C)")
print(f"Linear guess: {float(lin2(11)):.2f} C, error {abs(float(lin2(11))-24):.2f}")
print(f"Cubic guess : {float(cub2(11)):.2f} C, error {abs(float(cub2(11))-24):.2f}")

plt.scatter(hours, temperature, label="Hourly measurements", zorder=3)
plt.plot(ten_minute_times, linear_estimates, label="Linear")
plt.plot(ten_minute_times, cubic_estimates, label="Cubic spline")
plt.xlabel("Hour of day"); plt.ylabel("Temperature (C)")
plt.title("Temperature interpolation"); plt.legend(); plt.grid(True)
plt.savefig(os.path.join(FIG, "task13_interpolation.png"), dpi=150, bbox_inches="tight")
