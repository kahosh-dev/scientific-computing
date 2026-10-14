# Task 5: Matrix Algebra and Matrix Operations

**Code:** `code/Task_05_matrix_algebra.py`, `code/Task_05_matrix_algebra_modified.py`
**Figure:** `figures/task05_transform.png`

## Inputs and operation
The inputs are the four corners of a unit square, a rotation angle (45°) and scale factors (2 horizontally, 1.5 vertically). A rotation matrix and a scaling matrix are multiplied (`rotation @ scale`) to give one transformation matrix, which is applied to every point (`points @ T.T`).

## Output
Transformed corners: (0,0), (1.414,1.414), (0.354,2.475), (−1.061,1.061). The determinant of the transformation is 3.0, which equals 2 × 1.5 (rotation has determinant 1, scaling multiplies area by 2 × 1.5). So the new shape has three times the area of the square.

## Changing a parameter
Angle 90° and scale (1, 3): the corners become (0,0), (0,1), (−3,1), (−3,0). The square is turned a quarter circle and stretched into a 3 × 1 rectangle. The determinant is still 3.

## Graph
The black square is the original, the red shape is the 45° version (a tilted parallelogram) and the blue dashed one is the 90° rectangle. All start at the origin because the origin is mapped to itself by a linear transformation.

## Modified program
**Case:** a game sprite (triangle) rotated 30° about its own centre and then mirrored left to right.
**Assumptions:** rotation about the centroid (2, 1); mirror about the y-axis.
**Output:** new vertices (3.232, −0.866), (−0.232, 1.134), (3.0, 2.732). Area before and after is 6.0.
**Interpretation:** rotation has determinant +1 and the mirror −1. The negative sign tells us the orientation of the shape flipped, while the area (absolute value) did not change.
