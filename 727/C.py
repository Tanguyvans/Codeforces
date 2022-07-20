import math

n, k, x = map(int, input().split())

a = list(map(int, input().split()))

a = sorted(a)

b = []
a0 = a[0]
ans = 1
for i in range(1, n):
    if a[i] - a0 > x:
        ans += 1
        b.append(a[i]-a0)

    a0 = a[i]

b = sorted(b)
i = 0
if b:
    while k > 0:
        if b[i] % x == 0:
            if (b[i]//x)-1 <= k:
                k -= (b[i]//x)-1
                ans -= 1
            else:
                break
        else:
            if b[i]//x <= k:
                k -= b[i]//x
                ans -= 1
            else:
                break

        if i == len(b)-1:
            break

        i += 1

print(ans)
