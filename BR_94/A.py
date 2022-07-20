from collections import deque as dq
r = 8
c = 8

start = []
end = []

g = [list(input()) for i in range(r)]
s = [0 for i in range(r)]
ms = 9
js = []
for i in range(r):
    for j in range(c):
        if g[i][j] == 'M':
            start = [i, j]
            a = []
        elif g[i][j] == 'A':
            end = [i, j]
            a = []
        elif g[i][j] == '.':
            a = []
        elif g[i][j] == 'S':
            a = [1]
            ms = min(i, ms)
            if j not in js:
                js.append(j)

        if i == 0:
            g[i][j] = a
        else:
            for k in range(len(g[i-1][j])):
                a.append(int(g[i-1][j][k])+1)
            g[i][j] = a


d = dq()
vis = [[-1 for i in range(c)] for j in range(r)]
d.append([start[0], start[1], 1, vis])
tag = [[False for i in range(c)] for j in range(r)]
while len(d) > 0:
    x, y, nb, vis = d.popleft()
    vis[x][y] = nb
    tag[x][y] = True
    row = [1, 0, 0, -1, 1, 1, -1, -1, 0]
    col = [0, 1, -1, 0, 1, -1, 1, -1, 0]
    if nb < 8:
        moves = 9
    else:
        moves = 8
    for k in range(moves):
        a = x+row[k]
        b = y+col[k]
        if 0 <= a < r and 0 <= b < c:
            if nb not in g[a][b] and nb+1 not in g[a][b]:
                if moves == 9 and ms+nb < 8 and b in js:
                    vis[a][b] = nb+1
                    d.append([a, b, nb+1, vis])
                elif vis[a][b] == -1:
                    vis[a][b] = nb+1
                    d.append([a, b, nb+1, vis])

for i in range(r):
    continue
    print(*tag[i])

x = end[0]
y = end[1]
if tag[x][y] == True:
    print('WIN')
else:
    print('LOSE')
