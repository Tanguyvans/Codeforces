from collections import deque as dq
n, m = map(int, input().split())
g = [list(input()) for i in range(n)]
breeders = []
me = []
exit = []
for i in range(n):
    for j in range(m):
        if g[i][j] == 'S':
            me = [i, j]
        elif g[i][j] == 'E':
            exit = [i, j]
        elif g[i][j] not in '0T':
            breeders.append([i, j])

d = dq()
d.append([exit[0], exit[1], 0])

vis = [[-1 for i in range(m)] for j in range(n)]

while len(d) > 0:
    x, y, nb = d.popleft()
    vis[x][y] = nb

    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]

    for k in range(4):
        a = x+row[k]
        b = y+col[k]
        if 0 <= a < n and 0 <= b < m and vis[a][b] == -1 and g[a][b] != 'T':
            vis[a][b] = nb+1
            d.append([a, b, nb+1])


x, y = me
final_time = vis[x][y]
ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] not in 'SET0' and -1 < vis[i][j] <= final_time:
            ans += int(g[i][j])

print(ans)
