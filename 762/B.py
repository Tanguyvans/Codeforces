from logging import root
import math

for _ in range(int(input())):
    n = float(input())

    sq = math.floor(n**(1/2))
    cb = math.floor(n**(1/3))

    double = math.floor(n**(1/(2*3)))

    if (cb+1) ** 3 <= n:
        cb += 1
    if (double+1) ** (2*3) <= n:
        double += 1

    ans = sq + cb - double
    print(ans)
