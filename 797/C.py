for _ in range(int(input())):
    n = int(input())

    s = list(map(int, input().split(' ')))
    f = list(map(int, input().split(' ')))

    ans = [0 for i in range(n)]
    ans[0] = f[0]-s[0]
    t = 0
    for i in range(1, n):
        t = max(f[i-1], s[i])
        ans[i] = f[i]-t

    print(*ans)
