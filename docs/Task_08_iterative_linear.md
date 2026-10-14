# Task 8: Iterative Methods for Linear Systems

**Code:** `code/Task_08_iterative_linear.py`, `code/Task_08_iterative_linear_modified.py`
**Figures:** `figures/task08_convergence.png`, `figures/task08_rod_profile.png`

## Inputs and operation
A 5×5 tridiagonal matrix (steady-state heat model) and a right-hand side b = [100, 0, 0, 0, 20] representing boundary temperatures of 100 °C on the left and 20 °C on the right. Jacobi updates every unknown from the previous iteration; Gauss-Seidel uses new values as soon as they are computed. Stop when the largest change is below 1e-8.

## Output
Both methods and the direct solver give the temperatures 86.67, 73.33, 60.00, 46.67, 33.33 °C. Jacobi needed 150 iterations, Gauss-Seidel 75, so Gauss-Seidel was about twice as fast.

## Changing a parameter
- Tolerance 1e-3 instead of 1e-8: Jacobi 70 iterations, Gauss-Seidel 35. A looser tolerance stops earlier but the answer is less accurate.
- Right boundary 50 °C instead of 20 °C: exact temperatures become 91.67, 83.33, 75.00, 66.67, 58.33 °C. The whole profile is warmer and the temperature drop between neighbours is smaller.

## Graph
The convergence plot has a log vertical axis. Both curves are straight lines going down, i.e. the error shrinks by a constant factor every step. The Gauss-Seidel line is steeper, which explains its smaller iteration count.

## Modified program
**Case:** a metal rod with 19 interior points, ends held at 80 °C and 30 °C.
**Assumptions:** steady state, uniform rod, no heat loss from the sides.
**Output:** Jacobi 1161 iterations, Gauss-Seidel 579; largest difference from the exact answer is 4e-5 °C.
**Interpretation:** the temperature falls in a straight line from 80 °C to 30 °C (see `task08_rod_profile.png`). Compared with the 5-point case, the iteration count is much higher: the more unknowns, the slower these simple methods converge.
