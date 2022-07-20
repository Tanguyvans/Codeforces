from collections import deque as dq

for _ in range(int(input())):
    n = int(input())

    g = {i: [] for i in range(n)}

    for i in range(n):
        x, y = map(int, input().split())

        g[x-1].append(y-1)
        g[y-1].append(x-1)

    vis = [-1 for i in range(n)]

    d = dq()
    imp = False
    sol = []
    for i in range(n):
        if vis[i] == -1:
            nodes = 1
            vis[i] = 1
            d.append(i)
            while len(d) > 0:
                pos = d.popleft()
                count = 0
                for k in g[pos]:
                    count += 1
                    if vis[k] == -1:
                        nodes += 1
                        d.append(k)
                        vis[k] = 1

                if count > 2:
                    imp = True
                    break

            if nodes % 2 != 0:
                imp = True
        if imp:
            break

    if imp:
        print('NO')
    else:
        print('YES')
