from collections import deque as dq
import math

h, w = map(int, input().split())

g = [[] for i in range(h)]
pos = ()
c = 0
for i in range(h):
    a = input()
    for j in range(w):
        if a[j] == '*':
            pos = (i, j)
            c += 1
        g[i].append(a[j])


d = dq()
d.append(pos)

flag = False

hh = []
ww = []

while len(d) > 0:
    x, y = d.popleft()
    if x+1 == math.ceil(h/2) or x+1 == math.floor(h/2):
        if y+1 == math.ceil(w/2) or y+1 == math.floor(w/2):
            flag = True
    if g[x][y] == '*':
        if x > 0:
            if g[x-1][y] == '*':
                if y not in hh:
                    hh.append(y)
            d.append((x-1, y))
        if y > 0:
            if g[x][y-1] == '*':
                if x not in ww:
                    ww.append(x)
            d.append((x, y-1))
        if x < h-1:
            if g[x-1][y] == '*':
                if y not in hh:
                    hh.append(y)
            d.append((x+1, y))
        if y < w-1:
            if g[x][y-1] == '*':
                if x not in ww:
                    ww.append(x)
            d.append((x, y+1))

        g[x][y] = '.'
        c -= 1


if not flag:
    print('NO')
elif c != 0:
    print('NO')
elif len(hh) != 1:
    print('NO')
elif len(ww) != 1:
    print('NO')
else:
    print('YES')
