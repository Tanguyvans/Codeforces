n, k = map(int, input().split())

a = list(map(int, input().split()))
b = sorted(a)

d = {}
s = 0
for i in range(n):
    if b[i] not in d:
        d[b[i]] = s

    s += 1

sol = [d[a[i]] for i in range(n)]

for i in range(k):
    x, y = map(int, input().split())

    if d[a[x-1]] > d[a[y-1]]:
        sol[x-1] -= 1
    elif d[a[y-1]] > d[a[x-1]]:
        sol[y-1] -= 1

print(*sol)
