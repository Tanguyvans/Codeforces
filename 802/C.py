for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    pos = a[0]
    f = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            ans += a[i] - a[i+1]
            pos = min(pos, a[i+1]-f)
        elif a[i] < a[i+1]:
            ans += a[i+1]-a[i]
            f += a[i+1]-a[i]
            pos = min(pos, a[i+1]-f)

    print(ans+abs(pos))
