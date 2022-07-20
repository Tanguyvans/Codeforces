from math import factorial


n = int(input())
b = list(map(int, input().split()))

l = b[0]
nl = 0
u = b[0]
nu = 0
for i in range(n):
    if b[i] == l:
        nl += 1
    elif b[i] < l:
        l = b[i]
        nl = 1

    if b[i] == u:
        nu += 1
    elif b[i] > u:
        u = b[i]
        nu = 1

if u == l:
    ans = 0
    for i in range(nl-1, 0, -1):
        ans += i

    print(0, ans)
else:
    print(u-l, nl*nu)
