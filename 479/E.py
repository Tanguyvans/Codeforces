from collections import deque as dq
n, m = map(int, input().split())

g = [[] for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())

    g[x-1].append(y-1)
    g[y-1].append(x-1)


d = dq()

tag = [False for i in range(n)]
ans = 0
for i in range(n):
    cycle = False
    if not tag[i]:
        cycle = True
        tag[i] = True
        d.append(i)

    while len(d) > 0:
        pos = d.popleft()
        if len(g[pos]) != 2:
            cycle = False
        for j in g[pos]:
            if not tag[j]:
                tag[j] = True
                d.append(j)

    if cycle:
        ans += 1

print(ans)
