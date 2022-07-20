for _ in range(int(input())):
    n, p, k = map(int, input().split(' '))

    a = list(map(int, input().split(' ')))
    a = sorted(a)

    ans = 0

    for i in range(k-1, n):
        if i < k:
            if a[i] <= p:
                ans += 1
            else:
                break
        else:
            if a[i-k] + a[i] <= p:
                ans += 1
                a[i] += a[i-k]
            else:
                break

    print(ans)
