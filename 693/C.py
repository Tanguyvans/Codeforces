for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    vec = [0 for i in range(n)]
    ans = 0
    for i in range(n-1, -1, -1):
        ai = a[i]
        sol = ai
        if ai + i < n:
            sol += vec[ai+i]

        vec[i] = sol
        ans = max(sol, ans)

    print(ans)
