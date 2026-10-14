# Task 12: Polynomial and Nonlinear Equation Solving

**Code:** `code/Task_12_nonlinear_equations.py`, `code/Task_12_nonlinear_equations_modified.py`
**Figure:** `figures/task12_intersections.png`

## Inputs and operation
Two equations: circle x² + y² = 4 and parabola y = x² − 1. `scipy.optimize.root` is called with different starting guesses and searches for (x, y) where both residuals are zero.

## Output
Starting at (1, 1) gives (1.5175, 1.3028); starting at (−1, 1) gives (−1.5175, 1.3028). Residuals are around 1e-13 and `success` is True. Substituting u = x² gives u² − u − 3 = 0, so x = ±√((1+√13)/2) = ±1.5175, which matches. There are only two intersections.

## Changing a parameter
With radius 1.5 the intersections move to (±1.3133, 0.7247). I also tried a guess of (0, 0): the solver reported `converged: False` and returned (0, 0). At that point the Jacobian matrix is singular, so Newton-type steps cannot be computed. This shows that the starting guess matters.

## Graph
The circle and parabola cross at two points (black dots) on the upper half. The smaller circle meets the parabola closer to the centre.

## Modified program
**Case:** a ball is kicked from the origin along y = x − 0.0109x² and meets a hill modelled as the circle (x − 60)² + y² = 30².
**Output:** first hit at (40.263, 22.593); a second solution at (89.948, 1.760), where the path would leave the hill on the far side. Without the hill, the ball lands at x = 91.74 m.
**Interpretation:** only the first intersection is physically relevant because the ball is stopped by the hill there. Different starting guesses found different roots, so the physical meaning of each root has to be checked.
