import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
import timeit

rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)

def loop_version(data):
    squared = []
    for value in data:
        seconds = value / 1000.0
        squared.append(seconds ** 2)
    return squared

def vectorized_version(data):
    seconds = data / 1000.0
    return seconds ** 2

loop_time = timeit.timeit(lambda: loop_version(latency_ms), number=1)
vector_time = timeit.timeit(lambda: vectorized_version(latency_ms), number=3) / 3
result = vectorized_version(latency_ms)

print("First five squared latency values:", result[:5])
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")

# --- Experiment: how does the speed-up change with the data size? ---
print("\n[Experiment] different sizes")
sizes = [1_000, 10_000, 100_000, 1_000_000]
speedups = []
for n in sizes:
    d = rng.uniform(5, 250, n)
    lt = timeit.timeit(lambda: loop_version(d), number=1)
    vt = timeit.timeit(lambda: vectorized_version(d), number=5) / 5
    speedups.append(lt / vt)
    print(f"n={n:>9,}: loop {lt:.5f}s, vectorized {vt:.6f}s, speed-up {lt/vt:.1f}x")

plt.semilogx(sizes, speedups, marker="o")
plt.xlabel("Number of measurements"); plt.ylabel("Speed-up (loop time / vectorized time)")
plt.title("Vectorization speed-up vs data size")
plt.grid(True)
plt.savefig(os.path.join(FIG, "task03_speedup.png"), dpi=150, bbox_inches="tight")
