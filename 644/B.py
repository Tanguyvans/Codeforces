for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(a)
    ans = a[-1]-a[0]
    for i in range(n-1):
        ans = min(a[i+1]-a[i], ans)

    print(ans)
