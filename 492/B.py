import math

n = int(input())
a = list(map(int, input().split()))

time = int(math.ceil(a[0]/n))*n
ans = 1

for i in range(1, n):
    t = max(int(math.ceil((a[i]-i)/n)), 0)

    if i + t*n < time:
        time = i + t*n
        ans = i+1

print(ans)
