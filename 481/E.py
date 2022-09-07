n, w = map(int, input().split())
a = list(map(int, input().split()))

u = w
l = 0

changes = 0
for i in range(n):
    changes += a[i]

    u = min(u, w-changes)
    l = max(l, -changes)


if u >= l:
    print(u-l+1)
else:
    print(0)
