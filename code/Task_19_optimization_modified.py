import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.optimize import minimize

# New case: a school canteen mixes rice (x), beans (y) and vegetables (z), in 100 g portions.
# Minimise cost while meeting minimum protein, energy and fibre for the meal.
#            rice  beans  veg
cost    = np.array([0.30, 0.50, 0.40])        # per 100 g
protein = np.array([2.7,  21.0,  2.0])        # g per 100 g
energy  = np.array([130., 340.,  35.])        # kcal per 100 g
fibre   = np.array([0.4,  15.0,  2.5])        # g per 100 g

cons = [
    {"type": "ineq", "fun": lambda z: protein @ z - 25},
    {"type": "ineq", "fun": lambda z: energy @ z - 600},
    {"type": "ineq", "fun": lambda z: fibre @ z - 10},
]
sol = minimize(lambda z: cost @ z, x0=[3, 1, 1], method="SLSQP",
               bounds=[(0, 8)]*3, constraints=cons)
x = sol.x
print("Success:", sol.success)
print("Portions (rice, beans, veg):", np.round(x, 3))
print(f"Cost per meal: {sol.fun:.3f}")
print(f"Protein {protein@x:.1f} g, energy {energy@x:.0f} kcal, fibre {fibre@x:.1f} g")
