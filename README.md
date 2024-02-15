
# OOP python for Held-Karp Algorithm for Traveling Salesman Problem
The Held-Karp algorithm, also known as the Held-Karp dynamic programming algorithm or simply the Held-Karp algorithm,
is used to solve the Traveling Salesman Problem (TSP). The Traveling Salesman Problem involves finding the shortest possible tour that visits
a given set of cities and returns to the starting city. The Held-Karp algorithm efficiently computes the optimal solution for small to moderate-sized instances of the TSP.

## Initialization
- Initialize a table (DP) to store subproblem solutions.
- For each subset of cities S that includes the starting city and has a size of 2 or more, calculate $DP[S][j]$ for each city j in S.

## Recursive Calculation
- For each subset S and each city j in S, calculate $DP[S][j]$ using the recurrence relation:

$DP[S][j] = min_{k in S, k != j} (DP[S - {j}][k] + cost[k][j])$
This formula considers all possible ways to reach city j from the starting city by visiting all cities in S exactly once.

## Final Solution
- The optimal tour cost is given by the minimum value of $min_{j != start} (DP[all cities][j] + cost[j][start]).$
