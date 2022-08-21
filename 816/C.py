n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += (i+1)*(n-i)
    if i > 0:
        if a[i-1] == a[i]:
            ans -= (n-i)*i

a = {i: a[i] for i in range(n)}

sol = []
for i in range(m):
    j, x = map(int, input().split())
    j -= 1

    aj = a[j]

    if j > 0:
        aj1 = a[j-1]
        if aj1 != aj and aj1 == x:
            ans -= (n-j)*j
        elif aj1 == aj and aj1 != x:
            ans += (n-j)*j

    if j < n-1:
        aj1 = a[j+1]
        if a[j] != aj1 and aj1 == x:
            ans -= (n-(j+1))*(j+1)
        elif a[j] == aj1 and aj1 != x:
            ans += (n-(j+1))*(j+1)

    a[j] = x

    sol.append(ans)

for i in range(m):
    print(sol[i])
