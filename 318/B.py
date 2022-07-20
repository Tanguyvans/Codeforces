from collections import deque as dq
n, m = map(int, input().split())

g = {i: [] for i in range(n)}

for i in range(m):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)


d = dq()

vis = [False for i in range(n)]
ans = 100000
imp = True
sol = []
for i in range(n):
    if vis[i] == False:
        imp = True
        d.append([i, -1])
        vis[i] = True
        while len(d) > 0:
            pos, pos_1 = d.popleft()
            for k in g[pos]:
                if not vis[k]:
                    vis[k] = True
                    d.append([k, pos])
                if pos_1 != -1:
                    for kk in g[pos_1]:
                        if kk == k:
                            sol.append([pos_1, pos, k])

if sol:
    for s in sol:
        r = len(g[s[0]])+len(g[s[1]])+len(g[s[2]]) - 6
        ans = min(r, ans)
    print(ans)
else:
    print(-1)
