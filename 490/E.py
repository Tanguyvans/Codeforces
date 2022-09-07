from collections import deque as dq

n, m, s = map(int, input().split())

g = {i: [] for i in range(n)}

for i in range(m):
    x, y = map(int, input().split())
    g[y-1].append(x-1)

vis = [-1 for i in range(n)]
