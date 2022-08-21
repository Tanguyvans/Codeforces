n, m = map(int, input().split())

a = list(map(int, input().split()))
a = sorted(a, reverse=True)

sol = {i: 0 for i in range(m)}

for i in range(m):
    sol[i] = sol[(i-1+m) % m] + a[-i-1]
    print(sol[i], end=' ')

s = sol[m-1]
for i in range(m, n):
    s += a[-i-1]
    pos = (i % m)
    sol[pos] += s
    print(sol[pos], end=' ')
