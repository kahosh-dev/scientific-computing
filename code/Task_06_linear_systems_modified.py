import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

# New case: mesh-current analysis of a circuit with three loops.
# Loop equations (Kirchhoff's voltage law), unknowns I1, I2, I3 in amps:
#  (10+20)I1 -   20 I2        = 12
#  -20 I1 + (20+30+10) I2 - 10 I3 = 0
#          -10 I2 + (10+40) I3    = -6
R = np.array([
    [ 30., -20.,   0.],
    [-20.,  60., -10.],
    [  0., -10.,  50.]
])
V = np.array([12., 0., -6.])

I = np.linalg.solve(R, V)
print("Mesh currents (A):", np.round(I, 5))
print("Residual norm:", np.linalg.norm(V - R @ I))
print("Condition number of R:", round(np.linalg.cond(R), 2))
print(f"Current through shared 20 ohm resistor: {I[0]-I[1]:.5f} A")
print(f"Power in the 20 ohm resistor: {(I[0]-I[1])**2 * 20:.5f} W")
