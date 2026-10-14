# Task 20: Random Numbers and Monte Carlo Methods

**Code:** `code/Task_20_monte_carlo.py`, `code/Task_20_monte_carlo_modified.py`
**Figure:** `figures/task20_monte_carlo.png`

## Inputs and operation
Demand on a server is modelled as a normal random variable with mean 850 and standard deviation 120. Capacity is 1000. 100,000 random demands are generated (seed 42) and the fraction above 1000 estimates the overload probability.

## Output
Estimated probability 10.616 % (10,616 overloads in 100,000). The exact value from the normal distribution is 10.565 %, so the simulation is close. About one in ten periods would overload the server.

## Changing a parameter
- Capacity 900 / 1000 / 1100 / 1200 gives 33.6 % / 10.6 % / 1.9 % / 0.17 % overload (exact 33.8 / 10.6 / 1.9 / 0.18 %). Extra capacity cuts risk quickly.
- Number of simulations N = 100 / 1,000 / 10,000 / 1,000,000 gives 2.0 % / 10.1 % / 10.5 % / 10.57 %. With few simulations the estimate is poor.
- The same idea estimates π: 200,000 random points gave 3.146.

## Graph
The running estimate jumps around for small N and settles near the dashed exact line as the number of simulations grows (log horizontal axis).

## Modified program
**Case:** project duration with three sequential tasks (design, build, testing) with triangular distributions (4-6-12, 8-12-22, 3-5-10 days).
**Output:** mean duration 27.33 days (std 3.69). Chance to finish within 30 days: 76.28 %; within 25 days: 28.39 %. The 90th percentile is 32.3 days.
**Interpretation:** adding up the "most likely" values gives 23 days, but the mean is 27 days because the distributions are skewed to the right (delays are more extreme than early finishes). A deadline with 90 % confidence needs about 32 days.
