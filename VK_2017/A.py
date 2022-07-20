from collections import deque as dq
import math
n, m = map(int, input().split())

g = {i: [] for i in range(n)}

for i in range(m):
    x, y = map(int, input().split())

    g[x-1].append(y-1)
    g[y-1].append(x-1)


d = dq()
vis = [-1 for i in range(n)]

nb = 0
impossible = False
for i in range(n):
    if vis[i] == -1:
        vis[i] = nb
        d.append(i)

        nodes = 1
        vertex = 0
        while len(d) > 0:
            pos = d.popleft()
            for k in g[pos]:
                if vis[k] == -1:
                    vis[k] = nb
                    d.append(k)
                    nodes += 1
                    vertex += 1
                elif vis[k] == vis[pos]:
                    vertex += 1
                else:
                    impossible = True
                    break
        nb += 1

        if nodes*(nodes-1)/2 != vertex/2:
            impossible = True

        if impossible:
            break

if impossible:
    print('NO')
else:
    print('YES')
