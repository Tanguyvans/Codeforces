import math

for _ in range(int(input())):
    n, k = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))

    if k >= n:
        ans = int(sum(a) + (k*n)-n*(n+1)/2)
    else:
        d = sum(a[0:k])
        ans = int(d + k*(k-1)/2)
        for i in range(1, n-k+1):
            d -= a[i-1]
            d += a[i+k-1]
            ans = max(ans, int(d + k*(k-1)/2))

    print(ans)
