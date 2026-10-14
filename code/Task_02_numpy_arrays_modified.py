import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

# New case: soil-moisture sensor on a farm, one reading per hour (% volumetric water)
moisture = np.array([
    41, 40, 39, 38, 37, 36, 35, 33, 31, 29, 28, 27,
    26, 26, 27, 29, 31, 33, 35, 37, 38, 39, 40, 41
], dtype=float)

threshold = 30.0
dry = moisture < threshold
print(f"Mean moisture: {moisture.mean():.2f} %")
print(f"Min: {moisture.min():.0f} %  Max: {moisture.max():.0f} %")
print(f"Hours below {threshold:.0f} %: {dry.sum()}")
print("Hours needing irrigation:", np.where(dry)[0])

# Scale readings to a 0-1 'wetness index' using the whole array at once
index = (moisture - moisture.min()) / (moisture.max() - moisture.min())
print("Wetness index (first 6):", np.round(index[:6], 3))
