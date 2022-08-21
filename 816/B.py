import math
for _ in range(int(input())):
    n, k, b, s = map(int, input().split())

    r = (k-1)*n

    m =

    r2 = max(s-m, r)

    if r2 > r:
        print(-1)
    else:
        for i in range(k):
            mid = max(k-1, r)
            if i == k-1:
                mid += m
            print(mid, end=' ')

        print('')
