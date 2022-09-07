import math

for _ in range(int(input())):
    n = int(input())

    s = math.floor(n/3)
    ans = max(0, s-1)

    n -= (s-1)*3

    if n == 4 or n == 1:
        ans += 2
    elif n == 3 or n == 2:
        ans += 1

    print(ans)
