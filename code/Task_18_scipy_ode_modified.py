import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures")

import numpy as np
from scipy.integrate import solve_ivp

# New case: SIR epidemic model for a school of 1000 students.
#   dS/dt = -beta S I / N,  dI/dt = beta S I / N - gamma I,  dR/dt = gamma I
N, beta, gamma = 1000.0, 0.5, 0.2          # R0 = beta/gamma = 2.5
def sir(t, y, beta=beta, gamma=gamma):
    S, I, R = y
    return [-beta*S*I/N, beta*S*I/N - gamma*I, gamma*I]

def run(beta_val):
    return solve_ivp(sir, (0, 120), [995, 5, 0], args=(beta_val, gamma),
                     t_eval=np.linspace(0, 120, 481), rtol=1e-8)

base = run(0.5)
masks = run(0.3)     # contact reduced, R0 = 1.5
for name, s, b in (("baseline", base, 0.5), ("with masks", masks, 0.3)):
    i = np.argmax(s.y[1])
    print(f"{name}: R0={b/gamma:.2f}, peak infected {s.y[1, i]:.0f} on day {s.t[i]:.0f}, "
          f"total ever infected {s.y[2, -1] + s.y[1, -1]:.0f}")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.plot(base.t, base.y[1], label="Infected, beta=0.5")
plt.plot(masks.t, masks.y[1], label="Infected, beta=0.3")
plt.xlabel("Day"); plt.ylabel("Students"); plt.legend(); plt.grid(True)
plt.title("SIR model: effect of reducing contact")
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "task18_sir.png"), dpi=150, bbox_inches="tight")
