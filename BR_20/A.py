import math
m, n = map(int, input().split(' '))

ans = 0

if m % 2 == 0:
    ans = m*n/2
elif n % 2 == 0:
    ans = m*n/2
else:
    ans = (m-1)*n/2
    ans += math.floor(n/2)

print(int(ans))
