# Task 19: Numerical Optimization

**Code:** `code/Task_19_optimization.py`, `code/Task_19_optimization_modified.py`
**Figure:** `figures/task19_optimization.png`

## Inputs and operation
Minimise cost = 12x + 18y, where x and y are units of Type A and Type B servers, subject to the capacity constraint 100x + 170y ≥ 1000 and x, y ≥ 0. Solved with `minimize` (SLSQP). A brute-force search then checks whole-number combinations.

## Output
Optimum: x = 0, y = 5.882, capacity exactly 1000, cost 105.88. The best whole-number solution is 0 Type A and 6 Type B (capacity 1020, cost 108). Type B costs 0.106 per unit of capacity while Type A costs 0.12, so B is the better buy and the solver uses only B.

## Changing a parameter
When the price of B rises from 18 to 30, B now costs 0.176 per unit of capacity, which is more than A. The solution flips to 10 Type A and 0 Type B with cost 120 (the same in whole numbers). A small change in one cost coefficient can move the optimum from one corner of the feasible region to another.

## Graph
The shaded area is the set of allowed combinations (above the capacity line). Grey lines are cost levels; the optimum is the point where the lowest cost line just touches the feasible region, on the y-axis.

## Modified program
**Case:** a canteen chooses portions (100 g) of rice, beans and vegetables to minimise cost while giving at least 25 g protein, 600 kcal and 10 g fibre.
**Assumptions:** the costs and nutrient values per 100 g are rough numbers I picked for the exercise, not real prices.
**Output:** 1.765 portions of beans and nothing else; cost 0.882, protein 37.1 g, energy 600 kcal, fibre 26.5 g.
**Interpretation:** the energy requirement is the binding constraint (exactly 600 kcal) while protein and fibre are exceeded. A meal of beans only is not realistic, so in practice we would add upper limits on each food for variety.
