for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    l = [[a[i], b[i]] for i in range(n)]
    l = sorted(l, key=lambda x: x[0])

    a, b = map(list, zip(*l))

    for i in range(1, n):
        b[i] += b[i-1]

    l = 0
    u = n
    ans = b[-1]
    while l < u:
        mid = (l+u) // 2

        va = a[mid]
        vb = b[-1] - b[mid]

        ans = min(ans, max(va, vb))
        if va >= vb:
            u = mid
        elif va < vb:
            l = mid + 1

    print(ans)
