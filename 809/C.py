for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if n % 2 != 0:
        sol = 0
        for i in range(1, n-1):
            if i % 2 == 0:
                continue

            sol += max(0, max(a[i-1], a[i+1])+1 - a[i])

        print(sol)

    else:
        sol = 0
        for i in range(1, n-2):
            if i % 2 == 0:
                continue

            sol += max(0, max(a[i-1], a[i+1])+1 - a[i])

        ans = sol
        for i in range(n-3, -1, -2):
            sol += (a[i] - max(a[i-1]+1, a[i+1]+1, a[i])) + \
                (max(a[i+2]+1, a[i]+1, a[i+1]) - a[i+1])

            ans = min(ans, sol)

        print(ans)
