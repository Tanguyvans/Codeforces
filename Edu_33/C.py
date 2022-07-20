from collections import deque as dq

n, m = map(int, input().split())
a = list(map(int, input().split()))

g = [[] for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

d = dq()
tag = [False for i in range(n)]
sol = []

for i in range(n):
    ans = 0
    if tag[i] == False:
        d.append(i)
        tag[i] = True
        ans = a[i]

    while len(d) > 0:
        pos = d.popleft()
        for j in g[pos]:
            if not tag[j]:
                d.append(j)
                tag[j] = True
                ans = min(ans, a[j])

    if ans > 0:
        sol.append(ans)

print(sum(sol))
