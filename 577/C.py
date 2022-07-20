import math

n, k = map(int, input().split())

a = list(map(int, input().split()))

a = sorted(a)

ans = a[n//2]
nb = 1
for i in range(n//2, n-1):
    if k > 0:
        if (a[i+1]-a[i])*nb <= k:
            ans = a[i+1]
            k -= (a[i+1]-a[i])*nb
            nb += 1
        else:
            break

    else:
        break

if k > 0:
    ans += math.floor(k/nb)

print(ans)
