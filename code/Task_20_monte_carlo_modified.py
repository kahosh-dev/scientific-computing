import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

# New case: a small project has three tasks done one after another.
# Durations (days) follow triangular distributions (min, most likely, max).
# What is the chance the whole project finishes within 30 days?
rng = np.random.default_rng(2024)
N = 100_000
design = rng.triangular(4, 6, 12, N)
build = rng.triangular(8, 12, 22, N)
testing = rng.triangular(3, 5, 10, N)
total = design + build + testing

print(f"Mean duration: {total.mean():.2f} days, std {total.std():.2f}")
print(f"P(finish within 30 days) = {(total <= 30).mean():.2%}")
print(f"P(finish within 25 days) = {(total <= 25).mean():.2%}")
print(f"90th percentile (deadline with 90% confidence): {np.percentile(total, 90):.1f} days")
print(f"Sum of 'most likely' values: {6+12+5} days (optimistic compared with the mean)")
