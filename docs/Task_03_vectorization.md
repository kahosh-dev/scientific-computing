# Task 3: Mathematical Functions and Vectorization

**Code:** `code/Task_03_vectorization.py`, `code/Task_03_vectorization_modified.py`
**Figure:** `figures/task03_speedup.png`

## Inputs and operation
One million simulated latency values between 5 and 250 ms (random generator with seed 42). Each is divided by 1000 (ms to s) and squared. This is done twice: once with a Python `for` loop and once with a vectorized NumPy expression. `timeit` measures both.

## Output
```
Loop time: 0.3623 s
Vectorized time: 0.0221 s
Approximate speed-up: 16.4x
```
The two methods give the same numbers but the vectorized one is many times faster. The exact timings depend on the computer and change slightly between runs.

## Changing a parameter
I varied the number of measurements:

| n | loop (s) | vectorized (s) | speed-up |
|---|---|---|---|
| 1,000 | 0.00011 | 0.000003 | 40x |
| 10,000 | 0.00097 | 0.000009 | 105x |
| 100,000 | 0.01063 | 0.000106 | 100x |
| 1,000,000 | 0.15307 | 0.004929 | 31x |

The speed-up is large at every size. It is not perfectly steady, probably because of memory and cache effects with big arrays and timing noise, so I would not read too much into the exact ratios.

## Graph
The curve shows speed-up against data size on a log axis. It is above 30x everywhere, which shows that vectorization pays off for both small and large data.

## Modified program
**Case:** power dissipated by a 220 Ω load from 1 million ADC readings (0–1023, 5 V reference) using P = V²/R.
**Result:** mean power 37.91 mW, peak 113.64 mW; the loop took 1.05 s and the vectorized version 0.019 s (about 55x faster).
**Interpretation:** the average power is a third of the peak, so the load is not constantly at full voltage; the vectorized form makes this kind of check cheap even on very large sensor logs.
