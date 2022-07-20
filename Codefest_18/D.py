from collections import deque as dq
n = int(input())

g = {i: [] for i in range(1, n+1)}
for i in range(n-1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)


seq = list(map(int, input().split()))
vis = [False for i in range(n)]
d = dq()
d.append(1)
vis[0] = True
index = 1
flag = False
while len(d) > 0:
    pos = d.popleft()
    top = index
    l = []
    for k in g[pos]:
        if vis[k-1] == False:
            vis[k-1] = True
            top += 1
            l.append(k)
    if sorted(l) != sorted(seq[index:top]):
        flag = True
        break
    else:
        d.extend(seq[index:top])
        index = top

if flag:
    print('No')
else:
    print('Yes')
