s, n = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

a = sorted(a, key=lambda a: a[0])
imp = False
for i in range(n):
    if a[i][0] < s:
        s += a[i][1]
    else:
        imp = True

if imp:
    print('NO')
else:
    print('YES')
