import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.optimize import root_scalar

# New case: yield to maturity of a bond.
# Face value 1000, coupon 6% paid yearly, 5 years left, market price 950.
face, coupon_rate, years, price = 1000.0, 0.06, 5, 950.0
coupon = face * coupon_rate

def bond_price(y):
    t = np.arange(1, years + 1)
    return np.sum(coupon / (1 + y)**t) + face / (1 + y)**years

f = lambda y: bond_price(y) - price
df = lambda y: np.sum(-np.arange(1, years+1) * coupon / (1 + y)**(np.arange(1, years+1) + 1)) \
               - years * face / (1 + y)**(years + 1)

newton = root_scalar(f, fprime=df, x0=0.05, method="newton", xtol=1e-12)
secant = root_scalar(f, x0=0.04, x1=0.08, method="secant", xtol=1e-12)
print(f"YTM (Newton): {newton.root:.5%} in {newton.iterations} iterations")
print(f"YTM (Secant): {secant.root:.5%} in {secant.iterations} iterations")
print(f"Price at YTM: {bond_price(newton.root):.4f}")
print(f"Current yield (coupon/price): {coupon/price:.3%}")
