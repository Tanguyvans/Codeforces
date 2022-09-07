n, m = map(int, input().split())

a = [list(map(int, input().split())) for i in range(m)]
for i in range(m):
    a[i].append(i+1)
a = sorted(a, key=lambda x: [x[1], x[0]])

sol = [0 for i in range(n)]
imp = False
for i in range(m):
    si, di, ci, pos = a[i]
    if sol[di-1] != 0:
        imp = True
        break
    else:
        sol[di-1] = m+1

    for j in range(si-1, di-1):
        if sol[j] == 0:
            sol[j] = pos
            ci -= 1

            if ci == 0:
                break

    if ci != 0:
        imp = True
        break

if imp:
    print(-1)
else:
    print(*sol)
