for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for i in range(n-1):
        if a[i] == 0 and ans > 0:
            ans += 1
        else:
            ans += a[i]

    print(ans)
