# Task 7: Gaussian Elimination and LU Decomposition

**Code:** `code/Task_07_gaussian_lu.py`, `code/Task_07_gaussian_lu_modified.py`
**Figure:** `figures/task07_solutions.png`

## Inputs and operation
A 3×3 coefficient matrix A is factored once with `lu_factor` (LU with row pivoting). Then `lu_solve` reuses the factors for three different measurement vectors b.

## Output
Set 1: x = [5, 5, 5]; Set 2: [5.317, 5.268, 4.756]; Set 3: [4.902, 5.610, 5.537]. All residual norms are about 1e-15 or 0. The direct `np.linalg.solve` answer for set 1 agrees.

## Changing a parameter
I increased the problem to a 400×400 matrix with 500 right-hand sides. Calling `solve` every time took 0.732 s; factoring once and reusing took 0.031 s, about 23 times less. This is because factorization costs roughly n³ operations but each extra solve costs only about n².

## Graph
The bars show the three unknowns for each measurement set. The values change a little between sets, matching the small changes in b.

## Modified program
**Case:** a chain of four masses connected by springs (k = 200 N/m each) fixed to a wall; K u = f.
**Assumptions:** identical springs, small displacements, three different load cases.
**Output:** L and U factors are printed. A 10 N load on the last mass gives displacements 50, 100, 150, 200 mm; a 20 N load on the second mass gives 100, 200, 200, 200 mm.
**Interpretation:** the last mass moves most. In the middle-load case the masses after the loaded one all move the same amount, because the springs beyond it are not stretched.
