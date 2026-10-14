import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import math
from decimal import Decimal
import numpy as np

# New case: a banking system adds a 0.01 service fee 1,000,000 times.
# The true total is exactly 10,000.00.
n = 1_000_000
naive = 0.0
for _ in range(n):
    naive += 0.01

fsum = math.fsum([0.01] * n)
dec = sum(Decimal("0.01") for _ in range(n))
float32 = np.float32(0)
for _ in range(100_000):
    float32 += np.float32(0.01)

print(f"Naive float64 sum : {naive:.10f}  (error {abs(naive-10000):.2e})")
print(f"math.fsum         : {fsum:.10f}  (error {abs(fsum-10000):.2e})")
print(f"Decimal           : {dec}")
print(f"float32 after 100,000 additions (true 1000): {float32:.4f}")
print("Naive total == 10000 ?", naive == 10000, "| isclose:", np.isclose(naive, 10000))
