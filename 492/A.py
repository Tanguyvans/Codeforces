import math
n = int(input())

bills = [100, 20, 10, 5, 1]

ans = 0

for bi in bills:
    nb = math.floor(n/bi)
    ans += nb
    n -= nb*bi

print(ans)
