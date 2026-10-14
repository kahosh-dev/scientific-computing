# Task 16: Numerical Integration

**Code:** `code/Task_16_numerical_integration.py`, `code/Task_16_numerical_integration_modified.py`
**Figure:** `figures/task16_integration.png`

## Inputs and operation
Smart-meter power readings (kW) every 2 hours over 12 hours. Energy is the area under the power-time curve. The trapezoidal rule uses straight segments; Simpson's rule uses parabolas.

## Output
Trapezoidal: 15.700 kWh. Simpson: 15.800 kWh. Difference 0.100 kWh. The household used about 15.7 to 15.8 kWh in the 12 hours. Power peaked at 1.8 kW around 06:00.

## Changing a parameter
I tested both rules on sin(x) from 0 to π, where the exact answer is 2, using different numbers of points:

| points | trapezoid error | Simpson error |
|---|---|---|
| 3 | 4.3e-1 | 9.4e-2 |
| 9 | 2.6e-2 | 2.7e-4 |
| 33 | 1.6e-3 | 1.0e-6 |

Doubling the interval count reduces the trapezoid error about 4 times and the Simpson error about 16 times. Simpson is better for smooth functions.

## Graph
Left: the shaded area under the power curve is the energy. Right: both error lines fall as points increase on a log-log plot; the Simpson line is steeper and lower.

## Modified program
**Case:** inflow into a water tank, measured every 15 minutes for 2 hours.
**Output:** 3157.5 L (trapezoid) and 3175.0 L (Simpson), average flow 26.46 L/min. The running total reaches 772.5 L after 30 min, 1777.5 L after 60 min and 3157.5 L after 120 min. A 3000 L tank would be full.
**Interpretation:** the two methods differ by only 17.5 L (about 0.6 %), so either is fine for planning. The tank fills fastest between minute 30 and 60, when the flow is highest.
