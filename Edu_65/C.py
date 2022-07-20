from collections import deque as dq
n, m = map(int, input().split())

g = {i: [] for i in range(1, n+1)}

for i in range(m):
    a = list(map(int, input().split()))
    for j in range(1, a[0]+1):
        g[a[j]].append(i)


d = dq()
vis = [False for i in range(m)]
seq = []

for i in range(1, n+1):
    if vis[i] == False:
        d.append(i)
        vis[i] = True
        nb = 1
        while len(d) > 0:
            pos = d.popleft()
            print(g, pos)
            for k in g[pos]:
                if vis[k] == False:
                    vis[k] = True
                    d.append(k)
                    nb += 1

        seq.append(nb)

print(seq)
