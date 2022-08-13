import math

for _ in range(int(input())):
    n, k, z = map(int, input().split())

    a = list(map(int, input().split()))
    sums = [0 for i in range(n)]
    for i in range(n):
        sums[i] = sums[i-1]+a[i]

    ans = 0

    si = a[0]
    for i in range(1, k+1):
        si += a[i]
        sol = si
        p = i
        ki = k

        coef = (k-p)/2

        if coef > z:
            nb = min(coef, z)
            sol += (a[i-1]+a[i])*nb
            ki -= 2*nb
        else:
            if (k-p) % 2 == 0:
                nb = min(int(coef), z)
                sol += (a[i-1]+a[i])*nb
                ki -= 2*nb
            else:
                nb = min(math.floor(coef), z)
                sol += a[i-1]*(nb+1)+a[i]*nb
                ki -= 2*nb + 1

        sol += sums[ki] - sums[i]
        ans = max(ans, sol)

    print(ans)
