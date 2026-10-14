import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])

speed = np.zeros_like(position)
speed[0] = (position[1] - position[0]) / (time[1] - time[0])
for i in range(1, len(time) - 1):
    speed[i] = (position[i + 1] - position[i - 1]) / (time[i + 1] - time[i - 1])
speed[-1] = (position[-1] - position[-2]) / (time[-1] - time[-2])

for t, x, v in zip(time, position, speed):
    print(f"t={t:.0f}s, position={x:.1f}m, estimated speed={v:.2f}m/s")

# --- Experiment: how does step size h affect the error? Test on f(x)=sin(x) at x=1 ---
print("\n[Experiment] derivative of sin(x) at x=1 (true value cos(1) = %.10f)" % np.cos(1))
hs = np.array([1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-8, 1e-10, 1e-12])
fwd = (np.sin(1 + hs) - np.sin(1)) / hs
cen = (np.sin(1 + hs) - np.sin(1 - hs)) / (2 * hs)
err_f = np.abs(fwd - np.cos(1)); err_c = np.abs(cen - np.cos(1))
for h, ef, ec in zip(hs, err_f, err_c):
    print(f"h={h:.0e}: forward error {ef:.2e}, central error {ec:.2e}")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(time, speed, marker="o")
ax[0].set_xlabel("Time (s)"); ax[0].set_ylabel("Estimated speed (m/s)")
ax[0].set_title("Speed from GPS positions"); ax[0].grid(True)
ax[1].loglog(hs, err_f, "o-", label="Forward")
ax[1].loglog(hs, err_c, "s-", label="Central")
ax[1].set_xlabel("Step size h"); ax[1].set_ylabel("Absolute error")
ax[1].set_title("Error vs step size"); ax[1].legend(); ax[1].grid(True, which="both")
plt.savefig(os.path.join(FIG, "task15_differentiation.png"), dpi=150, bbox_inches="tight")
