import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np

def overload(capacity, mean, std, N, seed=42):
    rng = np.random.default_rng(seed)
    d = rng.normal(mean, std, N)
    return d > capacity

N = 100_000
ov = overload(1000.0, 850.0, 120.0, N)
print(f"Estimated overload probability: {ov.mean():.4%}")
print(f"Number of overload cases: {ov.sum()} out of {N}")

# exact answer from the normal distribution, for checking
from scipy.stats import norm
exact = 1 - norm.cdf(1000, 850, 120)
print(f"Exact probability (normal CDF): {exact:.4%}")

# --- Experiment: higher capacity, and fewer simulations ---
print("\n[Experiment]")
for cap in (900, 1000, 1100, 1200):
    p = overload(cap, 850, 120, N).mean()
    print(f"capacity {cap}: simulated {p:.4%}, exact {1-norm.cdf(cap, 850, 120):.4%}")
for n in (100, 1_000, 10_000, 1_000_000):
    print(f"N={n:>9,}: {overload(1000, 850, 120, n).mean():.4%}")

# estimate of pi to show the same idea
rng = np.random.default_rng(1)
pts = rng.random((200_000, 2))
inside = (pts**2).sum(axis=1) <= 1
print("Pi estimate with 200,000 points:", 4 * inside.mean())

running = np.cumsum(ov) / np.arange(1, N + 1)
idx = np.unique(np.logspace(1, np.log10(N), 200).astype(int)) - 1
plt.semilogx(idx + 1, running[idx], label="Simulation")
plt.axhline(exact, color="r", linestyle="--", label="Exact value")
plt.xlabel("Number of simulations"); plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk")
plt.legend(); plt.grid(True)
plt.savefig(os.path.join(FIG, "task20_monte_carlo.png"), dpi=150, bbox_inches="tight")
