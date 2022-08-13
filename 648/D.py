from collections import deque as dq

for _ in range(int(input())):

    n, m = map(int, input().split())

    matrix = [list(input()) for i in range(n)]

    flag = False

    goods = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'B':
                matrix[i][j] = '.'
                rows = [-1, 0, 0, 1]
                cols = [0, 1, -1, 0]
                for k in range(4):
                    a = rows[k]+i
                    b = cols[k]+j
                    if 0 <= a < n and 0 <= b < m:
                        if matrix[a][b] == 'G':
                            flag = True
                            break
                        elif matrix[a][b] == '.':
                            matrix[a][b] = '#'

            elif matrix[i][j] == 'G':
                goods.append((i, j))

    if flag:
        print('No')
    elif matrix[n-1][m-1] == '#' and goods:
        print('No')
    else:
        d = dq()
        d.append((n-1, m-1))
        matrix[n-1][m-1] = '1'

        while len(d) > 0:
            x, y = d.popleft()
            rows = [-1, 0, 0, 1]
            cols = [0, 1, -1, 0]
            for k in range(4):
                a = rows[k]+x
                b = cols[k]+y
                if 0 <= a < n and 0 <= b < m:
                    if matrix[a][b] == '.':
                        matrix[a][b] = '1'
                        d.append((a, b))

                    elif matrix[a][b] == 'G':
                        matrix[a][b] = '1'
                        d.append((a, b))

        for good in goods:
            x, y = good

            if matrix[x][y] != '1':
                flag = True
                break

        if flag:
            print('No')

        else:
            print('Yes')
