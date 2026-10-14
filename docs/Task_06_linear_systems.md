# Task 6: Solution of Systems of Linear Equations

**Code:** `code/Task_06_linear_systems.py`, `code/Task_06_linear_systems_modified.py`
**Figure:** `figures/task06_lines.png`

## Inputs and operation
Coefficient matrix A = [[4, 2], [8, 12]] (CPU and memory used by one server of each type) and totals b = [20, 72]. `np.linalg.solve(A, b)` finds how many servers of each type are running.

## Output
Type A servers: 3, Type B servers: 4. Checking `A @ solution` gives [20, 72] and the residual is 0, so the answer reproduces the observed totals exactly.

## Changing a parameter
I changed the totals to 24 CPU units and 80 GB. The solution became 4 servers of each type. The matrix A is the same, only b changed, so the solution moved.

## Graph
Each equation is a straight line in the (x, y) plane. They cross at one point, (3, 4), which is the only pair satisfying both resource totals.

## Modified program
**Case:** mesh-current analysis of a three-loop circuit using Kirchhoff's voltage law.
**Assumptions:** resistor values as given in the code comments; sources of 12 V and 6 V.
**Output:** I1 = 0.5015 A, I2 = 0.1522 A, I3 = −0.0896 A. Residual norm about 1.8e-15; condition number 3.8 (well-conditioned).
**Interpretation:** the negative I3 just means the real current flows opposite to the direction we assumed. The shared 20 Ω resistor carries 0.349 A and dissipates about 2.44 W.
