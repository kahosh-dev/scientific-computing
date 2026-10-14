import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

T_ambient, T_initial, k, end_time = 25.0, 90.0, 0.12, 30.0

def euler_cooling(h):
    time = np.arange(0, end_time + h, h)
    T = np.zeros_like(time)
    T[0] = T_initial
    for i in range(len(time) - 1):
        T[i + 1] = T[i] + h * (-k * (T[i] - T_ambient))
    exact = T_ambient + (T_initial - T_ambient) * np.exp(-k * time)
    return time, T, exact

time, temperature, exact = euler_cooling(1.0)
print(f"Euler temperature after 30 min: {temperature[-1]:.2f} C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} C")
print(f"Final absolute error: {abs(temperature[-1]-exact[-1]):.4f} C")

# --- Experiment: change the step size h ---
print("\n[Experiment] step size")
results = {}
for h in (5.0, 2.0, 1.0, 0.5, 0.1):
    t, T, e = euler_cooling(h)
    results[h] = (t, T)
    print(f"h={h}: final {T[-1]:.4f} C, error {abs(T[-1]-e[-1]):.4f} C")
h5 = euler_cooling(5.0)
# h = 10 is unstable? k*h = 1.2 < 2 so still stable but oscillates
t10, T10, e10 = euler_cooling(10.0)
print(f"h=10 (k*h=1.2): values {np.round(T10, 2)}")
t17, T17, _ = euler_cooling(17.0)
print(f"h=17 (k*h=2.04): values {np.round(T17, 2)}  <- unstable")

tt = np.linspace(0, end_time, 300)
plt.plot(tt, T_ambient + (T_initial - T_ambient)*np.exp(-k*tt), "k", label="Exact")
for h in (5.0, 1.0, 0.1):
    plt.plot(*results[h], marker="o" if h > 0.5 else None, markersize=3, label=f"Euler h={h}")
plt.xlabel("Time (minutes)"); plt.ylabel("Temperature (C)")
plt.title("Cooling of a hot object"); plt.legend(); plt.grid(True)
plt.savefig(os.path.join(FIG, "task17_euler.png"), dpi=150, bbox_inches="tight")
