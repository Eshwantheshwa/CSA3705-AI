
import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

h = {'A': 4, 'B': 3, 'C': 1, 'D': 0}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]
    best = {start: 0}

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return

        if g != best[node]:
            continue

        for nxt, cost in graph[node]:
            ng = g + cost

            if ng < best.get(nxt, float('inf')):
                best[nxt] = ng
                heapq.heappush(
                    pq, (ng + h[nxt], ng, nxt, path + [nxt])
                )

    print("No path found")

astar('A', 'D')
