import math

n, k = map(int, input().split())

u = n
l = k

while l < u:
    mid = (u+l)//2
    s1 = -1
    sol = 0
    i = 0
    while s1 != sol:
        s1 = sol
        sol += math.floor(mid/k**i)
        i += 1

    if sol > n:
        u = mid
    elif sol < n:
        l = mid + 1
    else:
        l = u = mid

print(u)
