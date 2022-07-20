from re import I


import math

for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = 10**10

    up = int(math.ceil(n**(1/2)))
    for i in range(up, 0, -1):
        if n/i == int(n/i):
            if n/i <= k:
                ans = min(ans, i, int(n/i))
            elif i <= k:
                ans = min(ans, int(n/i))

    print(ans)
