import math

n, m = map(int, input().split())
a = list(map(int, input().split()))
q = int(input())
for i in range(q):
    xs, ys, xf, yf, k = map(int, input().split())

    if abs(xf-xs) % k != 0 or abs(yf-ys) % k != 0:
        print('NO')
    elif xs <= a[ys-1] or xf <= a[yf-1]:
        print('NO')
    else:
        nb = 0
        for i in range(ys-1, yf-1):
            nb = max(nb, a[i])

        nb -= xs
        u = (n-xs)//k
        l = nb/k

        if u > l:
            print('YES')
        else:
            print('NO')
