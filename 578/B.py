for _ in range(int(input())):
    n, m, k = map(int, input().split())
    h = list(map(int, input().split()))

    imp = False
    for i in range(n-1):
        if h[i] >= h[i+1]-k:
            m += min(h[i], h[i]-(h[i+1]-k))

        elif h[i] + m >= h[i+1]-k:
            m -= (h[i+1]-k-h[i])

        else:
            imp = True

    if imp:
        print('NO')
    else:
        print('YES')
