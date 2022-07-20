for _ in range(int(input())):
    n, k = map(int, input().split(' '))

    a = list(map(int, input().split(' ')))
    if k >= n:
        print(0)

    else:
        ans = sum(a)
        a = sorted(a, reverse=True)

        for i in range(k):
            ans -= a[i]

        for i in range(k):
            ans += n
            ans -= i

        print(ans)
