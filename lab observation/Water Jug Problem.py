
from collections import deque

q = deque([(0, 0)])
visited = {(0, 0)}

while q:
    a, b = q.popleft()
    print(a, b)

    if a == 2 or b == 2:
        print("Goal reached")
        break

    states = [
        (4, b), (a, 3), (0, b), (a, 0),
        (a-min(a, 3-b), b+min(a, 3-b)),
        (a+min(b, 4-a), b-min(b, 4-a))
    ]

    for s in states:
        if s not in visited:
            visited.add(s)
            q.append(s)
