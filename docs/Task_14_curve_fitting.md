# Task 14: Curve Fitting and Approximation

**Code:** `code/Task_14_curve_fitting.py`, `code/Task_14_curve_fitting_modified.py`
**Figure:** `figures/task14_curve_fit.png`

## Inputs and operation
Seven pairs of (concurrent users, response time in ms). `curve_fit` finds a, b, c in y = ax² + bx + c that minimise the sum of squared residuals.

## Output
Fitted model: y = 0.002167x² − 0.1345x + 85.00, RMSE 1.55 ms, prediction at 400 users 377.86 ms. The response time grows faster than linearly with load: the server slows down more and more as users are added.

## Changing a parameter
I changed the model degree:

| degree | RMSE (ms) | prediction at 400 users |
|---|---|---|
| 1 | 18.83 | 312.9 ms |
| 2 | 1.55 | 377.9 ms |
| 3 | 0.14 | 387.9 ms |

The straight line fits badly. The cubic has the smallest error, but with only seven points it may be fitting noise, so the extra accuracy is not necessarily real. Predictions at 400 users, outside the data, also differ by about 10 ms between degrees 2 and 3.

## Graph
The curve bends upward through the points; the straight line misses the ends of the data; the cubic and quadratic are almost identical inside the data range and separate beyond 350 users.

## Modified program
**Case:** daily active users of a campus app over the first 10 weeks, fitted with y = A·e^(kt).
**Output:** users = 97.4·exp(0.2199t), about 24.6 % growth per week, doubling time 3.15 weeks, RMSE 3.8 users, R² = 0.9998. Forecast for week 12: about 1364 users.
**Interpretation:** the fit is very good over this period, but exponential growth cannot continue forever (the number of students is limited), so the week-12 forecast should be treated with caution.
