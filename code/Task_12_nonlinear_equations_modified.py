import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.optimize import root

# New case: a ball is kicked from the origin and flies along y = x - 0.0109 x^2 (metres).
# A hill is modelled by the circle (x-60)^2 + y^2 = 30^2. Where does the ball hit the hill?
def eq(z):
    x, y = z
    return [y - (x - 0.0109 * x**2),
            (x - 60)**2 + y**2 - 30**2]

for guess in ([35.0, 20.0], [85.0, 10.0], [60.0, 25.0]):
    s = root(eq, guess)
    print("guess", guess, "->", np.round(s.x, 3), "residual", np.round(eq(s.x), 8), "ok:", s.success)

# Same problem as a single polynomial is harder; check ball landing point instead:
land = np.roots([-0.0109, 1, 0])
print("Ball lands (no hill) at x =", np.round(land, 2))
