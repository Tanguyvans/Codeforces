for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    prev = (0, 10**10)
    ans = 0
    for i in range(n):
        sol = (a[i]-x, a[i]+x)
        if prev[0] <= sol[0] <= prev[1] or prev[0] <= sol[1] <= prev[1] or sol[0] <= prev[0] <= sol[1] or sol[0] <= prev[1] <= sol[1]:
            prev = (max(prev[0], sol[0]), min(prev[1], sol[1]))
        else:
            ans += 1
            prev = (a[i]-x, a[i]+x)

    print(ans)
