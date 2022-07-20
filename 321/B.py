n, d = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]

a = sorted(a, key=lambda x: (x[0], x[1]))
i = 0
j = 0
ans = 0
sol = 0
while i < n and j < n:
    start = a[i][0]
    while True:
        if j >= n:
            break
        if a[j][0]-start >= d:
            break
        sol += a[j][1]
        j += 1
    ans = max(ans, sol)
    sol -= a[i][1]
    i += 1

print(ans)
