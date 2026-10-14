# BIT 2118 Scientific Computing: Group Work

My individual repository for the BIT 2118 group tasks (Tasks 2 to 20). The tasks were discussed in a group, but the code, experiments and write-ups here are my own submission.

## Folder layout

```
code/      Python programs. Each task has the original program with a parameter
           experiment at the end, and a *_modified.py file for a new real-world case
figures/   Graphs saved by the programs (PNG)
docs/      One write-up per task (inputs, operation, output, parameter change,
           graph interpretation, modified case)
```

## How to run

```
pip install -r requirements.txt
python code/Task_02_numpy_arrays.py     # one task
./run_all.sh                            # everything
```

Figures are written to `figures/` (the programs do not open windows). Timings in Tasks 3 and 7 depend on the computer, so your numbers will differ a little from the ones in the write-ups.

## Task index

| Task | Topic | Write-up | Modified case |
|---|---|---|---|
| 2 | NumPy arrays | [doc](docs/Task_02_numpy_arrays.md) | Soil-moisture sensor |
| 3 | Vectorization | [doc](docs/Task_03_vectorization.md) | Power from ADC readings |
| 4 | Floating-point errors | [doc](docs/Task_04_numerical_errors.md) | Bank fee accumulation |
| 5 | Matrix algebra | [doc](docs/Task_05_matrix_algebra.md) | Game sprite transformation |
| 6 | Linear systems | [doc](docs/Task_06_linear_systems.md) | Circuit mesh currents |
| 7 | LU decomposition | [doc](docs/Task_07_gaussian_lu.md) | Spring-mass chain |
| 8 | Iterative methods | [doc](docs/Task_08_iterative_linear.md) | Heated rod |
| 9 | Eigenvalues | [doc](docs/Task_09_eigenvalues.md) | Friendship network |
| 10 | Bisection / fixed point | [doc](docs/Task_10_bisection_fixed_point.md) | Loan interest rate |
| 11 | Newton / secant | [doc](docs/Task_11_newton_secant.md) | Bond yield |
| 12 | Nonlinear equations | [doc](docs/Task_12_nonlinear_equations.md) | Ball hitting a hill |
| 13 | Interpolation | [doc](docs/Task_13_interpolation.md) | Pressure sensor calibration |
| 14 | Curve fitting | [doc](docs/Task_14_curve_fitting.md) | App user growth |
| 15 | Differentiation | [doc](docs/Task_15_numerical_differentiation.md) | Car acceleration |
| 16 | Integration | [doc](docs/Task_16_numerical_integration.md) | Water tank volume |
| 17 | Euler method | [doc](docs/Task_17_euler_ode.md) | Fish population |
| 18 | SciPy ODEs | [doc](docs/Task_18_scipy_ode.md) | School epidemic (SIR) |
| 19 | Optimization | [doc](docs/Task_19_optimization.md) | Canteen meal cost |
| 20 | Monte Carlo | [doc](docs/Task_20_monte_carlo.md) | Project deadline risk |

Task 1 (Data Science Essentials with Python) is the self-paced prerequisite and has no code here.
