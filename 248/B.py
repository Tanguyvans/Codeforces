n = int(input())
v0 = list(map(int, input().split()))
u0 = sorted(v0)

v = [0 for i in range(n+1)]
u = [0 for i in range(n+1)]

for i in range(1, n+1):
    v[i] = v0[i-1] + v[i-1]
    u[i] = u0[i-1] + u[i-1]

m = int(input())
for i in range(m):
    tp, l, r = map(int, input().split())

    if tp == 1:
        print(v[r]-v[l-1])

    else:
        print(u[r]-u[l-1])
