from collections import deque as dq

n, m = map(int, input().split())

g = [list(input()) for i in range(n)]

d = dq()

vis = [[-1 for i in range(m)]for j in range(n)]

nb = 0
cycle = False
for i in range(n):
    for j in range(m):
        if vis[i][j] == -1:
            d.append([i, j])
            vis[i][j] = nb
            letter = g[i][j]
            while len(d) > 0:
                x, y = d.popleft()
                rows = [1, 0, 0, -1]
                cols = [0, 1, -1, 0]
                count = 0
                for k in range(4):
                    a = x+rows[k]
                    b = y+cols[k]
                    if 0 <= a < n and 0 <= b < m and vis[a][b] == -1 and letter == g[a][b]:
                        vis[a][b] = nb
                        d.append([a, b])

                    elif 0 <= a < n and 0 <= b < m and vis[a][b] == nb and letter == g[a][b]:
                        count += 1

                if count >= 2:
                    cycle = True

            nb += 1

if cycle:
    print('Yes')
else:
    print('No')
