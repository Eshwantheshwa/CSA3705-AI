
from itertools import permutations

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(cost)
best_cost = float('inf')
best_route = None

for p in permutations(range(1, n)):
    route = (0,) + p + (0,)
    total = sum(cost[route[i]][route[i+1]]
                for i in range(n))

    if total < best_cost:
        best_cost = total
        best_route = route

print("Best route:", best_route)
print("Minimum cost:", best_cost)
