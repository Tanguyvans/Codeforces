for _ in range(int(input())):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    a = [a[i] % k for i in range(n)]
    a = sorted(a)

    ans = 0
    ai = a[0]
    if ai != 0:
        si = k-ai+1
    else:
        si = 0
    ans = max(ans, si)
    for i in range(1, n):
        if ai == a[i] != 0:
            si += k
            ans = max(ans, si)
        elif a[i] != 0:
            ai = a[i]
            si = k-ai+1

            ans = max(ans, si)

    print(ans)
