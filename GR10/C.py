for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    m = 0

    for i in range(1, n):
        if a[i-1] <= a[i]:
            m = max(m, a[i])

        else:
            ans += a[i-1]-a[i]

    print(ans)
