from collections import deque as dq

n = int(input())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

vis = [-1 for i in range(n)]
prev = [[] for i in range(n)]
g = {i: [] for i in range(n)}
for i in range(n):
    g[i].append(a[i]-1)

d = dq()
for i in range(n):
    if vis == -1:
        d.append(i)
        vis[i] = a[i]
        while len(d) > 0:
            pos = d.popleft()
            for k in d[pos]:
                if vis[k] == -1:
                    vis[k]
