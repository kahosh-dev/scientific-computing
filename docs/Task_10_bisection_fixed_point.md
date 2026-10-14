# Task 10: Root Finding, Bisection and Fixed-Point Methods

**Code:** `code/Task_10_bisection_fixed_point.py`, `code/Task_10_bisection_fixed_point_modified.py`
**Figure:** `figures/task10_equilibrium.png`

## Inputs and operation
The heat balance f(T) = T − 25 − 10·e^(−T/20) equals zero at equilibrium. Bisection starts from an interval where f changes sign and halves it (xtol = 1e-10). Fixed-point iteration rewrites the equation as T = 25 + 10·e^(−T/20) and repeats from T = 30. (I used the bracket [20, 60] instead of [20, 40]; both contain the root.)

## Output
Bisection: 27.525211 °C in 39 iterations. Fixed point: 27.525211 °C in 13 iterations. Both methods agree. The equilibrium is a bit above the 25 °C ambient value because of the extra heating term.

## Changing a parameter
I replaced 10 by 30 (a stronger heat source). The equilibrium rises to 31.279175 °C and fixed point needs 22 iterations instead of 13. Fixed-point iteration converges at a speed set by |g′(T)| at the root. It is about 0.13 for amplitude 10 and about 0.31 for amplitude 30, so the larger heat term is still convergent (below 1) but slower.

## Graph
f(T) is an increasing curve that crosses zero once. The dashed vertical lines mark the roots (27.5 and 31.3 °C). The curve for amplitude 30 is shifted down, so it crosses zero further right.

## Modified program
**Case:** finding the interest rate of a loan: 5,000 borrowed, repaid with 24 monthly payments of 235.
**Assumptions:** equal monthly payments, interest charged monthly.
**Output:** monthly rate 0.986883 % (37 bisection steps), nominal annual 11.843 %, effective annual 12.507 %. Total repaid 5,640, so 640 is interest. The fixed-point version found the same rate but took 134 iterations.
**Interpretation:** the rate per month looks small but compounds to more than 12 % per year. Bisection is slow but guaranteed to work once the root is bracketed.
