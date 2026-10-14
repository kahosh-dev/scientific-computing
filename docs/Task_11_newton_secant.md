# Task 11: Root Finding, Newton-Raphson and Secant Methods

**Code:** `code/Task_11_newton_secant.py`, `code/Task_11_newton_secant_modified.py`
**Figure:** `figures/task11_npv.png`

## Inputs and operation
Cash flows: −10,000 now, then 3,000, 3,500, 4,000 and 2,500 over four years. The IRR is the rate at which the net present value (NPV) is zero. Newton-Raphson uses the derivative of NPV; the secant method only uses function values from two starting rates (5 % and 20 %). I also ran bisection for comparison.

## Output
All three methods give an IRR of 11.542461 %. Newton took 4 iterations, secant 7, bisection 40. The NPV at the solution is 0.000000. So the investment earns about 11.5 % per year.

## Changing a parameter
I increased the last inflow from 2,500 to 4,500 and started Newton at a poor guess of 50 %. The IRR rose to 17.0937 % and both methods still converged. A bigger final payment raises the return.

## Graph
NPV falls as the discount rate increases and crosses zero at the IRR. The orange curve (bigger inflow) is higher and crosses zero at a larger rate.

## Modified program
**Case:** yield to maturity of a bond: face value 1,000, 6 % annual coupon, 5 years, market price 950.
**Output:** YTM = 7.22687 % (Newton 5 iterations, secant 6). The price at that yield is exactly 950. The simple current yield is 6.316 %.
**Interpretation:** the bond sells below face value, so a buyer earns more than the coupon rate: the 6.3 % coupon income plus the gain when it is redeemed at 1,000.
