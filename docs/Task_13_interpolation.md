# Task 13: Interpolation

**Code:** `code/Task_13_interpolation.py`, `code/Task_13_interpolation_modified.py`
**Figure:** `figures/task13_interpolation.png`

## Inputs and operation
Seven hourly temperatures from 08:00 to 14:00. `interp1d` joins the points with straight lines; `CubicSpline` joins them with smooth cubic pieces. Both are evaluated every 10 minutes.

## Output
At 10:30 the linear estimate is 23.25 °C and the cubic estimate is 23.36 °C. The two methods differ by about 0.1 °C here.

## Changing a parameter
I removed the 11:00 reading (true value 24.0 °C) and predicted it from the others: linear gave 23.75 °C (error 0.25), cubic gave 24.11 °C (error 0.11). The spline did better because the temperature curve bends smoothly.

## Graph
Dots are measurements. The linear line has corners at each measurement, the spline is smooth. Both pass through all the dots. After 13:00 the spline curves over the peak of the day.

## Modified program
**Case:** calibration table of a pressure sensor (voltage in V to pressure in kPa).
**Output:** 1.25 V gives 19.25 kPa (linear) or 19.09 kPa (spline); 2.75 V gives 65.75 / 65.78 kPa; 3.9 V gives 101.20 / 101.42 kPa. In a leave-one-out test the mean error was 0.679 kPa for linear and 0.132 kPa for the spline.
**Interpretation:** the sensor response is curved, so the spline is the better choice for the lookup table. Interpolation should only be used inside the table range (0.5–4.5 V); outside it we would be extrapolating, which is unreliable.
