for _ in range(int(input())):
    n = int(input())

    a = []
    b = []

    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    ans = 0
    start = a[0]
    for i in range(1, n):
        ans += max(0, a[i]-b[i-1])
        start = min(start, b[i-1], a[i])

    start = min(start, b[-1], a[0])
    ans += max(a[0]-b[-1], 0)
    ans += start
    print(ans)
