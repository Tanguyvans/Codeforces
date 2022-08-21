import math

n, k = map(int, input().split())

if n == 1:
    m = 0
else:
    m = 0
    while 2**(m+1) <= n:
        m += 1

ans = 0
r = n
for i in range(1, m+1):
    mid = int(math.ceil(r/2))
    ans += mid * (k**(i-1))
    r -= mid
    if i == m:
        ans += r * (k**(i-1))

print(ans)
