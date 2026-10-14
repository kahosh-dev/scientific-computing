# Task 17: Ordinary Differential Equations, Euler Method

**Code:** `code/Task_17_euler_ode.py`, `code/Task_17_euler_ode_modified.py`
**Figure:** `figures/task17_euler.png`

## Inputs and operation
Newton's law of cooling dT/dt = −k(T − T_ambient) with k = 0.12 per minute, ambient 25 °C, starting at 90 °C, step h = 1 min, for 30 min. Each step uses T(n+1) = T(n) + h·f(T(n)). The exact solution is T = 25 + 65·e^(−0.12t).

## Output
Euler after 30 min: 26.40 °C; exact: 26.78 °C; error 0.372 °C. The object cools towards the room temperature; Euler cools slightly too fast.

## Changing a parameter
Step size h versus final error:

| h | final T (°C) | error (°C) |
|---|---|---|
| 5.0 | 25.2662 | 1.5098 |
| 2.0 | 26.0595 | 0.7165 |
| 1.0 | 26.4041 | 0.3720 |
| 0.5 | 26.5870 | 0.1890 |
| 0.1 | 26.7378 | 0.0383 |

Halving h roughly halves the error (first-order method). For very large steps the method misbehaves: with h = 10 (k·h = 1.2) the values jump around (90, 12, 27.6, 24.5), and with h = 17 (k·h > 2) it becomes unstable: the values swing between large positive and negative numbers and the swings grow (90, −42.6, 95.3), which is physically impossible for cooling.

## Graph
The black curve is the exact solution. Euler with h = 0.1 lies on top of it; h = 1 is slightly off; h = 5 is clearly too low in the early part.

## Modified program
**Case:** logistic population growth of fish in a pond (P0 = 50, r = 0.4 per month, carrying capacity 1000).
**Output:** at 24 months Euler gives 1003.06 (h = 4), 999.53 (h = 1) and 998.94 (h = 0.25) against the exact 998.71. The maximum error over the run drops from 261 to 82 to 21.
**Interpretation:** the population grows slowly, then quickly, then levels off near 1000. With h = 4 Euler even overshoots the capacity slightly. Euler with h = 1 lags in the fast-growth phase: it reaches 500 fish around month 9 while the exact curve reaches it at month 7.4.
