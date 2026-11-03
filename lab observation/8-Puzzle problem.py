
from collections import deque

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

q = deque([(start, [])])
visited = {start}

while q:
    state, path = q.popleft()

    if state == goal:
        for s in path + [state]:
            print(s[:3], s[3:6], s[6:])
        break

    z = state.index(0)
    for n in (z-3, z+3, z-1, z+1):
        if 0 <= n < 9 and not (
            (z % 3 == 0 and n == z-1) or
            (z % 3 == 2 and n == z+1)
        ):
            a = list(state)
            a[z], a[n] = a[n], a[z]
            t = tuple(a)
            if t not in visited:
                visited.add(t)
                q.append((t, path + [state]))
else:
    print("No solution")
