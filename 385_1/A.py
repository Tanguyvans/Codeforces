from collections import deque as dq
import math
n, m, k = map(int, input().split())

if n == 1:
    print(0)
else:
    kl = list(map(int, input().split()))
    g = {i: [] for i in range(n)}

    for i in range(m):
        x, y = map(int, input().split())
        g[x-1].append(y-1)
        g[y-1].append(x-1)

    tag = [False for i in range(n)]
    d = dq()

    ans = []
    for i in range(n):
        if tag[i] == False:
            d.append(i)
            tag[i] = True
            nb = 0
            edges = 0
            home = False
            first = True
            if i+1 in kl:
                home = True
            while len(d) > 0:
                pos = d.popleft()
                nb += 1
                for k in g[pos]:
                    edges += 1
                    if tag[k] == False:
                        if home == False:
                            if k+1 in kl:
                                home = True
                        tag[k] = True
                        d.append(k)
            ans.append([nb, home, edges//2])

    ans = sorted(ans, key=lambda a: [-a[1], -a[0]])
    nb0 = ans[0][0]

    sol = 0
    for i in range(len(ans)):
        sol += int((ans[i][0]*(ans[i][0]-1))/2 - ans[i][2])
        if ans[i][1] == False:
            sol += nb0 * ans[i][0]
            nb0 += ans[i][0]

    print(sol)
