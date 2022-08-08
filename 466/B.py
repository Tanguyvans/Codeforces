import math

n = int(input())
k = int(input())
a = int(input())
b = int(input())

ans = 0
while n > 1:
    if n % k == 0:
        if a*(n-(n//k)) >= b:
            ans += b
            n //= k
        else:
            ans += (n-1)*a
            n -= n + 1
            break
    else:
        coef = math.floor(n/k)
        delta = n-coef*k
        ans += delta*a
        n -= delta
        if n == 0:
            n += 1
            ans -= a


print(ans)
