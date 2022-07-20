from collections import deque as dq

n, m = map(int, input().split())
matrix = [list(input()) for i in range(n)]

x, y = map(int, input().split())
start = (x-1, y-1)

x, y = map(int, input().split())
end = (x-1, y-1)
start_change = []

d = dq()
d.append([start[0], start[1]])
imp = True

while len(d) > 0:
    x, y = d.popleft()
    rows = [1, 0, 0, -1]
    cols = [0, 1, -1, 0]
    for k in range(4):
        a = x + rows[k]
        b = y + cols[k]

        if a == end[0] and b == end[1] and matrix[a][b] == 'X':
            imp = False
            start = end
            break

        elif 0 <= a <= n-1 and 0 <= b <= m-1 and matrix[a][b] == '.':
            matrix[a][b] = 'X'
            d.append([a, b])

if imp:
    print('NO')
else:
    print('YES')
