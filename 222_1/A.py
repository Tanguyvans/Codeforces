from collections import deque as dq
n, m, k = map(int, input().split())

g = [[] for i in range(n)]
c = 0
for i in range(n):
    a = input()
    a = [j for j in a]
    for j in range(m):
        if a[j] == '.':
            a[j] = 'X'
            x = (i, j)
            c += 1
        g[i].append(a[j])

d = dq()
d.append(x)
rest = 0
while len(d) > 0:
    i, j = d.popleft()

    if rest == c-k:
        break

    if g[i][j] == 'X':
        if i > 0:
            d.append((i-1, j))
        if j > 0:
            d.append((i, j-1))
        if i < n-1:
            d.append((i+1, j))
        if j < m-1:
            d.append((i, j+1))

        g[i][j] = '.'
        rest += 1

for i in range(n):
    for j in range(m):
        print(g[i][j], end='')
    print('')
