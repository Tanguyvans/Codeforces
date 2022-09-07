import math

n = int(input())

a = list(map(int, input().split()))

s = 0
si = 0
for i, ai in enumerate(a):

    mid = math.floor(n/ai)
    if mid > si:
        s = i
        si = mid
    elif mid == si and n - ai*mid > n - si*(a[s]):
        s = i
        si = mid

sol = [s+1 for i in range(si)]
r = n - si*(a[s])

for i in range(len(sol)):

    for j in range(sol[i], len(a)):
        if (r + a[sol[i]-1] - a[j]) >= 0:
            r += a[sol[i]-1] - a[j]
            sol[i] = j+1

if sol:
    print(''.join(str(x) for x in sol))
else:
    print(-1)
