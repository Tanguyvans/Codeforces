import math

for _ in range(int(input())):
    n, m = map(int, input().split())
    n -= 1
    m -= 1

    ans = n + m

    ans += min(n + min(1, m), m + min(1, n))

    print(ans)
