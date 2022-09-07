import math

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    d = {0: 0, 1: 0, 2: 0}
    for i in range(n):
        d[a[i] % 3] += 1

    ans = 0
    for k, v in d.items():
        if k == 0:
            ans += v

        elif k == 1:
            vi = min(d[k], d[k+1])
            d[k] -= vi
            d[k+1] -= vi
            ans += vi
            ans += math.floor(d[k]/3)
        else:
            ans += math.floor(d[k]/3)

    print(ans)
