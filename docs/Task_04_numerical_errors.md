# Task 4: Floating-Point Arithmetic and Numerical Errors

**Code:** `code/Task_04_numerical_errors.py`, `code/Task_04_numerical_errors_modified.py`
**Figure:** `figures/task04_cancellation.png`

## Inputs and operation
Three small studies: (1) comparing 0.1 + 0.2 with 0.3, (2) absolute and relative error of approximating √2 by 1.414, (3) the expression (√(1+x) − 1)/x computed directly and in the algebraically equal stable form 1/(√(1+x) + 1).

## Output
- `0.1 + 0.2 = 0.30000000000000004`; exact comparison is `False`, `np.isclose` gives `True`.
- Absolute error 0.00021356, relative error 0.0151 %.
- For x = 1e-12 the direct formula gives 0.500044 but the stable one gives 0.500000.

Computers store 0.1 and 0.2 in binary and cannot represent them exactly, so the sum is a tiny bit off. In the third study, √(1+x) is almost exactly 1 when x is tiny, so subtracting 1 wipes out most of the correct digits (cancellation).

## Changing a parameter
I made x much smaller (from 1e-2 down to 1e-15) and measured the relative error of the direct formula:

| x | relative error |
|---|---|
| 1e-2 | 1.5e-14 |
| 1e-6 | 1.2e-10 |
| 1e-10 | 8.3e-8 |
| 1e-12 | 8.9e-5 |
| 1e-15 | 0.11 |

At x = 1e-15 the direct answer is off by 11 %, while the stable form stays at 0.5.

## Graph
The log-log plot shows the error rising steadily as x shrinks, almost in a straight line. Smaller x means worse cancellation.

## Modified program
**Case:** a bank adds a 0.01 fee one million times; the true total is 10,000.00.
**Results:** plain float64 loop gives 10000.0000001719 (error 1.7e-7); `math.fsum` and `Decimal` give exactly 10000. A float32 sum of 100,000 fees gives 1000.665 instead of 1000.
**Interpretation:** small errors accumulate when the same rounded value is added many times. For money, use `Decimal` (or whole cents as integers), and never test the total with `==`.
