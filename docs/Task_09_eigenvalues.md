# Task 9: Eigenvalues and Eigenvectors

**Code:** `code/Task_09_eigenvalues.py`, `code/Task_09_eigenvalues_modified.py`
**Figure:** `figures/task09_centrality.png`

## Inputs and operation
A 4×4 adjacency matrix of an undirected network with nodes A, B, C, D. `np.linalg.eig` returns eigenvalues and eigenvectors. The eigenvector for the largest eigenvalue, made positive and normalised to sum to 1, is used as an importance score for each node.

## Output
Dominant eigenvalue 2.5616. Scores: A 0.2192, B 0.2808, C 0.2808, D 0.2192. B and C connect to all other nodes, so they score highest. The check ‖Av − λv‖ is about 2e-15, so the eigenpair is correct.

## Changing a parameter
I added a link between A and D. Now every node has three links, the dominant eigenvalue becomes exactly 3, and all four scores are 0.25. When the network is perfectly symmetric nobody stands out.

## Graph
Paired bars compare the two networks. In the original, B and C are taller than A and D; after the new link all bars are equal.

## Modified program
**Case:** friendship network of six students (8 friendships).
**Output:** dominant eigenvalue 2.8422. Cynthia scores highest (0.2242, 4 links), then Dennis and Esther (0.1969 each, 3 links), Felix 0.1386, Amina and Brian 0.1217.
**Interpretation:** Cynthia links the two small groups together. Felix has the same number of links as Amina and Brian (2) but scores higher because one of his friends (Dennis) is well connected. So the score depends on who you know, not only on how many you know.
