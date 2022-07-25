n, m = map(int, input().split())

g = {i: [] for i in range(1, n+1)}

for i in range(m):
    a, b, w = map(int, input().split())

    g[a].append([b, w])
    g[b].append([a, w])

pos = 1
vis = [float('inf') for i in range(n+1)]

vis[1] = 0

for i in range(n):
    for k, w in g[pos]:
        vis[k] = min(vis[k], w)

    for j in

print(vis)
