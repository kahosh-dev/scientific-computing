import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

# 24 hourly temperature readings in degrees Celsius
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])
mean_temp = np.mean(temperatures_c)
min_temp = np.min(temperatures_c)
max_temp = np.max(temperatures_c)
temperatures_f = 1.8 * temperatures_c + 32

print(f"Daily mean temperature: {mean_temp:.2f} C")
print(f"Minimum temperature: {min_temp:.2f} C")
print(f"Maximum temperature: {max_temp:.2f} C")
print("First six Fahrenheit readings:", temperatures_f[:6])

# --- Experiment: simulate a heat wave by adding 5 C to every reading ---
hot = temperatures_c + 5
print("\n[Experiment] +5 C heat wave")
print(f"Mean: {hot.mean():.2f} C, min: {hot.min():.2f} C, max: {hot.max():.2f} C")
print(f"Max in Fahrenheit: {1.8*hot.max()+32:.2f} F")

plt.plot(range(24), temperatures_c, marker="o", label="Normal day")
plt.plot(range(24), hot, marker="s", linestyle="--", label="Heat wave (+5 C)")
plt.axhline(mean_temp, color="grey", linewidth=0.8)
plt.xlabel("Hour of day"); plt.ylabel("Temperature (C)")
plt.title("Hourly temperatures at the weather station")
plt.legend(); plt.grid(True)
plt.savefig(os.path.join(FIG, "task02_temperatures.png"), dpi=150, bbox_inches="tight")
