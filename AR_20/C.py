from heapq import heappush, heappop
n, m = map(int, input().split())
g = {i: [] for i in range(n)}

for i in range(m):
    a, b, w = map(int, input().split())

    g[a-1].append([b-1, w])
    g[b-1].append([a-1, w])

parent = [-1 for i in range(n)]
dist = [float('inf') for i in range(n)]

vis = set()

d = []
d.append((0, 0))
dist[0] = 0

while d:
    w, pos = heappop(d)
    vis.add(pos)
    for i, wi in g[pos]:
        if i not in vis:
            if w + wi < dist[i]:
                dist[i] = w + wi
                parent[i] = pos
                heappush(d, (dist[i], i))

sol = [n-1]
mid = n-1

while parent[mid] != -1:
    sol.append(parent[mid])
    mid = parent[mid]

if sol[-1] != 0:
    print(-1)
else:
    sol.reverse()
    for s in sol:
        print(s+1, end=' ')

    print('')
