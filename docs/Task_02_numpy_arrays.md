# Task 2: NumPy Arrays and Numerical Computation

**Code:** `code/Task_02_numpy_arrays.py`, `code/Task_02_numpy_arrays_modified.py`
**Figure:** `figures/task02_temperatures.png`

## Inputs and operation
The input is a NumPy array of 24 hourly temperatures in °C. The program takes the mean, minimum and maximum, then converts every value to Fahrenheit with F = 1.8C + 32 in a single expression (no loop).

## Output
```
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```
In words: the day averaged about 23 °C, the coldest hour was 17.5 °C (early morning) and the hottest was 29.4 °C (around 12:00).

## Changing a parameter
I added 5 °C to every reading to imitate a heat wave. Mean, min and max each went up by exactly 5 (28.12, 22.50, 34.40 °C), and the maximum became 93.92 °F. The shape of the curve did not change, it just moved up, because adding a constant shifts every value equally.

## Graph
The solid line is the normal day, the dashed line the heat wave. Both rise from sunrise, peak in the early afternoon and fall in the evening. The vertical gap between them is constant at 5 °C.

## Modified program (different real-world case)
**Case:** soil-moisture sensor on a farm (`Task_02_numpy_arrays_modified.py`).
**Assumptions:** one reading per hour, in % volumetric water content; the soil needs irrigation below 30 %.
**Input:** 24 moisture readings between 26 % and 41 %.
**Output:** mean 34.00 %, min 26 %, max 41 %, and 7 hours below the threshold (hours 9 to 15). A 0–1 "wetness index" was computed for the whole array at once.
**Interpretation:** the soil dries out during the hottest part of the day, so irrigation should be scheduled from about 09:00 to 15:00.
