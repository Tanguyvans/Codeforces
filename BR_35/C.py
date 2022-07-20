from collections import deque as dq

with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    n, m = map(int, fin.readline().split())
    k = int(fin.readline())
    matrix = [[-1 for i in range(m)] for j in range(n)]

    d = dq()

    line = list(map(int, fin.readline().split()))
    for i in range(0, len(line)-1, 2):
        x = line[i]
        y = line[i+1]
        matrix[x-1][y-1] = 0
        d.append([x-1, y-1])

    sol = -1
    sx = -1
    sy = -1
    while len(d) > 0:
        x, y = d.popleft()
        rows = [1, 0, 0, -1]
        cols = [0, 1, -1, 0]
        for i in range(4):
            a = x+rows[i]
            b = y+cols[i]

            if 0 <= a < n and 0 <= b < m:
                if matrix[a][b] == -1:
                    matrix[a][b] = matrix[x][y]+1
                    d.append([a, b])

                    if matrix[a][b] >= sol:
                        sx = a
                        sy = b
                        sol = matrix[a][b]

    if sol == -1:
        fout.write(str(1) + ' ' + str(1))
    else:
        fout.write(str(sx+1) + ' ' + str(sy+1))
