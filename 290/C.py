from collections import deque as dq
n = int(input())
matrix = [list(input()) for i in range(n)]

alpha = "abcdefghijklmnopqrstuvwxyz"
seq = {}

for i in range(n-1):
    j = 0
    while True:
        if not matrix[i][j] or not matrix[i+1][j]:
            break
        if matrix[i][j] == matrix[i+1][j]:
            j += 1
        else:
            if matrix[i][j] not in seq:
                seq[matrix[i][j]] = [matrix[i+1][j]]
            break

vis = {i: -1 for i in seq.keys()}

d = dq()

count = 1
ans = ''
imp = False
for k, v in seq.items():
    sol = ''
    if vis[k] == -1 and v:
        vis[k] = count
        d.extend(v)
        while len(d) > 0:
            pos = d.popleft()
            sol += pos
            for k2, v2 in seq[pos].items():
                if vis[k2] != count:
                    vis[k2] = count
                    d.extend(v2)
                else:
                    imp = True
                    break

        count += 1
