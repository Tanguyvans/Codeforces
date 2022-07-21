n, k = map(int, input().split())

a = list(map(int, input().split()))
t = list(map(int, input().split()))

ones = 0
ans = 0
sol = 0
for i in range(n):
    sol += a[i]*(1-t[i])
    if i >= k:
        sol -= a[i-k]*(1-t[i-k])

    ones += a[i]*t[i]
    ans = max(sol, ans)

print(ones+ans)
