# Task 18: Numerical Solution of ODEs Using SciPy

**Code:** `code/Task_18_scipy_ode.py`, `code/Task_18_scipy_ode_modified.py`
**Figures:** `figures/task18_rc.png`, `figures/task18_sir.png`

## Inputs and operation
RC charging circuit: dV/dt = (Vs − V)/(RC) with Vs = 5 V, R = 1000 Ω, C = 0.001 F (time constant 1 s), V(0) = 0, solved on 0 to 5 s with `solve_ivp` using tight tolerances. The result is compared with the exact curve Vs(1 − e^(−t/RC)).

## Output
Solver success: True. Capacitor voltage at 5 s: 4.9663 V. Maximum error against the exact solution: 9.3e-10 V. The capacitor charges almost fully (99.3 % of 5 V) after five time constants.

## Changing a parameter
Doubling R to 2000 Ω doubles the time constant to 2 s. The voltage at 1 s fell from 3.161 V to 1.967 V, and at 5 s it was 4.590 V instead of 4.966 V. After one time constant the voltage should be 63.2 % of Vs (3.16 V), which matches the original circuit at t = 1 s.

## Graph
Both curves rise quickly at first and flatten as they approach 5 V. The solver curve and the dashed exact curve cannot be told apart. The R = 2000 Ω curve rises more slowly.

## Modified program
**Case:** SIR epidemic model for a school of 1000 students, γ = 0.2 per day, one version with β = 0.5 (R0 = 2.5) and one with β = 0.3 (R0 = 1.5, reduced contact), starting with 5 infected.
**Output:** baseline: peak of 235 infected on day 19, about 893 students infected in total. With reduced contact: peak of 66 on day 40, about 588 infected in total.
**Interpretation:** reducing contact lowers and delays the peak ("flattening the curve"), which would spread the load on the school clinic. It does not prevent the epidemic here because R0 is still above 1.
