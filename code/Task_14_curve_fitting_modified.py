import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.optimize import curve_fit

# New case: daily active users of a campus app during its first 10 weeks.
# Early growth looks exponential, so we fit y = A * exp(k t).
weeks = np.arange(1, 11, dtype=float)
users = np.array([120, 150, 185, 240, 290, 370, 450, 570, 700, 880], dtype=float)

def expo(t, A, k):
    return A * np.exp(k * t)

(A, k), cov = curve_fit(expo, weeks, users, p0=(100, 0.2))
pred = expo(weeks, A, k)
rmse = np.sqrt(np.mean((users - pred)**2))
ss_res = np.sum((users - pred)**2); ss_tot = np.sum((users - users.mean())**2)
print(f"Model: users = {A:.1f} * exp({k:.4f} t)")
print(f"Weekly growth factor: {np.exp(k):.3f} (about {100*(np.exp(k)-1):.1f}% per week)")
print(f"Doubling time: {np.log(2)/k:.2f} weeks")
print(f"RMSE: {rmse:.1f} users, R^2: {1 - ss_res/ss_tot:.4f}")
print(f"Forecast for week 12: {expo(12, A, k):.0f} users")
print("Parameter standard errors:", np.round(np.sqrt(np.diag(cov)), 4))
