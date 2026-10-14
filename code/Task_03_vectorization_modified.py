import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
import timeit

# New case: 1 million ADC readings (0-1023) from a 5 V sensor across a 220 ohm load.
# We want the voltage and the power dissipated, P = V^2 / R.
rng = np.random.default_rng(7)
adc = rng.integers(0, 1024, 1_000_000)
R = 220.0

def loop_version():
    out = []
    for a in adc:
        v = a * 5.0 / 1023
        out.append(v * v / R)
    return out

def vector_version():
    v = adc * 5.0 / 1023
    return v**2 / R

lt = timeit.timeit(loop_version, number=1)
vt = timeit.timeit(vector_version, number=3) / 3
p = vector_version()
print(f"Mean power: {p.mean()*1000:.2f} mW, peak power: {p.max()*1000:.2f} mW")
print(f"Loop {lt:.3f}s, vectorized {vt:.4f}s, speed-up {lt/vt:.0f}x")
