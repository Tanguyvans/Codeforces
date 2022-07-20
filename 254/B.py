from collections import deque as dq
n, m = map(int, input().split())

g = {i: [] for i in range(n)}
for i in range(m):
    x, y = map(int, input().split())

    g[x-1].append(y-1)
    g[y-1].append(x-1)

vis = [False for i in range(n)]

d = dq()
ans = 1
for i in range(n):
    if not vis[i]:
        d.append(i)
        vis[i] = True
        nb = 0
        while len(d) > 0:
            pos = d.popleft()
            flag = False
            for k in g[pos]:
                if vis[k] == False:
                    d.append(k)
                    vis[k] = True
                    nb += 1

        if nb > 0:
            ans *= 2**nb
print(ans)
