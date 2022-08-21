for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    mx = a[0]
    sol = 0
    for i in range(1, n):
        if a[i] < mx:
            sol = max(sol, mx-a[i])
        else:
            mx = a[i]

    ans = 0
    i = 1
    while sol > 0:
        sol -= 2**(i-1)
        i += 1
        ans += 1

    print(ans)
