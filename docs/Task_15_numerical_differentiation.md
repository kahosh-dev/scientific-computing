# Task 15: Numerical Differentiation

**Code:** `code/Task_15_numerical_differentiation.py`, `code/Task_15_numerical_differentiation_modified.py`
**Figure:** `figures/task15_differentiation.png`

## Inputs and operation
GPS positions in metres at t = 0 to 6 s. Speed is estimated with a forward difference at the first point, central differences for interior points and a backward difference at the last point.

## Output
Estimated speeds rise from 4.80 m/s at t = 0 to 8.00 m/s at t = 6 s (for example 5.65 m/s at t = 2 s). The vehicle is speeding up steadily.

## Changing a parameter
To see the effect of the step size h, I differentiated sin(x) at x = 1, where the true answer is cos(1) = 0.5403023059:

- Forward difference error drops roughly in proportion to h (4.3e-2 at h = 0.1 to 4.2e-6 at h = 1e-5).
- Central difference error drops with h² (9e-4 at h = 0.1 to 1.1e-11 at h = 1e-5).
- Below about h = 1e-8 the errors get worse again (5.9e-8 at 1e-10, 4e-5 at 1e-12) because of round-off, the same cancellation problem seen in Task 4.

So there is a best h: not too large (truncation error) and not too small (round-off error).

## Graph
Left: estimated speed against time, increasing roughly linearly. Right: the error curves form a "V". Reading from large h towards small h, the error falls steadily, the central difference staying well below the forward one, until around h = 1e-8 where round-off takes over and both curves climb again.

## Modified program
**Case:** a car's speed logged every 2 s while accelerating (0 to 78 km/h); `np.gradient` gives the acceleration in m/s².
**Output:** the acceleration peaks at 1.94 m/s² at t = 4 s and drops to 0.07 m/s² at t = 20 s. The average over the whole run is 1.08 m/s².
**Interpretation:** the car accelerates hardest at the start and then levels off as it approaches its top speed (about 21.7 m/s). The average hides the fact that the acceleration changes a lot during the run.
