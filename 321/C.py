from collections import deque as dq
n, m = map(int, input().split())
a = list(map(int, input().split()))

g = [[] for i in range(n)]
for i in range(n-1):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

tag = [False for i in range(n)]
cons = [0 for i in range(n)]


d = dq()
d.append(0)
tag[0] = True
cons[0] = a[0]
ans = 0
while len(d) > 0:
    pos, ch = d.popleft(), 0
    if cons[pos] > m:
        continue
    for i in g[pos]:
        if not tag[i]:
            cons[i] = cons[pos] + a[i] if a[i] > 0 else 0
            tag[i] = True
            d.append(i)
            ch += 1

    if ch == 0 and cons[pos] <= m:
        ans += 1

print(ans)
