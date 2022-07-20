from collections import deque as dq
n, k = map(int, input().split())

g = {i: [] for i in range(n)}

for i in range(k):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)


d = dq()
vis = [-1 for i in range(n)]
nb = 0
ans = 0
for i in range(n):
    sol = 0
    if vis[i] == -1:
        vis[i] = nb
        d.append(i)
        while len(d) > 0:
            pos = d.popleft()
            for j in g[pos]:
                if vis[j] == -1:
                    sol += 1
                    vis[j] = nb
                    d.append(j)

        nb += 1

    ans += sol
    sol = 1

print(k-ans)
